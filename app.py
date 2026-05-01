import os
import uuid
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from disease_info import get_disease_info

# Flask app setup
app = Flask(__name__)
# In production, use a strong environment variable: os.environ.get('SECRET_KEY', 'default_dev_key')
app.secret_key = os.environ.get("SECRET_KEY", "secretkey123_dev")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Secure Image Storage
app.config['UPLOAD_FOLDER'] = "instance/uploads"
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB upload limit
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
csrf = CSRFProtect(app)

# Load ML model
model = load_model("model/skin_model.h5")
class_names = ['Eczema', 'Melanoma', 'Psoriasis']

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

# Prediction history model
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_filename = db.Column(db.String(255), nullable=False)
    prediction = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You can now login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    history = Prediction.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', history=history)

@app.route('/predict', methods=['POST'])
@login_required
def predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('home'))
        
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('home'))
        
    if file and allowed_file(file.filename):
        # Secure filename generation
        ext = file.filename.rsplit('.', 1)[1].lower()
        secure_name = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{secure_name}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        file.save(filepath)

        img = image.load_img(filepath, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        # Save prediction history (only filename, not full path)
        new_prediction = Prediction(user_id=current_user.id, image_filename=unique_filename, prediction=predicted_class, confidence=confidence)
        db.session.add(new_prediction)
        db.session.commit()

        return render_template('result.html', prediction=predicted_class, confidence=confidence, pred=new_prediction, prediction_id=new_prediction.id)
        
    flash('Invalid file type. Only JPG and PNG are allowed.')
    return redirect(url_for('home'))

@app.route('/report/<int:prediction_id>')
@login_required
def report(prediction_id):
    pred = Prediction.query.get_or_404(prediction_id)
    # Ensure user can only view their own reports
    if pred.user_id != current_user.id:
        flash('Access denied.')
        return redirect(url_for('dashboard'))
    disease = get_disease_info(pred.prediction)
    return render_template('report.html', pred=pred, disease=disease)

@app.route('/image/<filename>')
@login_required
def serve_image(filename):
    """Securely serve images only to the user who uploaded them."""
    # Ensure secure filename check to prevent directory traversal
    secure_name = secure_filename(filename)
    
    # Check if the current user owns this image
    pred = Prediction.query.filter_by(image_filename=secure_name).first()
    if not pred or pred.user_id != current_user.id:
        abort(403) # Forbidden
        
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_name)

@app.route('/locator')
def locator():
    return render_template('locator.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
