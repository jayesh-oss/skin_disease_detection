import os
from flask import Flask, request, render_template, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model('model/skin_model.h5')
class_names = ['Acne', 'Hyperpigmentation', 'Nail_psoriasis', 'SJS-TEN', 'Vitiligo']

# Dictionary for prevention and treatment
disease_info = {
    'Acne': {
        'prevention': "Wash face twice daily, avoid oily skin products.",
        'treatment': "Use benzoyl peroxide, salicylic acid, and consult a dermatologist if severe."
    },
    'Hyperpigmentation': {
        'prevention': "Use sunscreen and avoid sun exposure.",
        'treatment': "Topical treatments like hydroquinone or laser therapy."
    },
    'Nail_psoriasis': {
        'prevention': "Keep nails trimmed and avoid injury.",
        'treatment': "Topical creams and phototherapy."
    },
    'SJS-TEN': {
        'prevention': "Avoid medicines that previously caused reactions.",
        'treatment': "Emergency medical care is needed immediately."
    },
    'Vitiligo': {
        'prevention': "Use sunscreen and avoid cuts/injury to the skin.",
        'treatment': "Topical steroids, light therapy, or skin grafting."
    }
}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            img = image.load_img(filepath, target_size=(128, 128))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            predicted_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction)

            info = disease_info.get(predicted_class, {
                'prevention': "No info available.",
                'treatment': "No info available."
            })

            return render_template('result.html',
                                   prediction=predicted_class,
                                   confidence=confidence,
                                   prevention=info['prevention'],
                                   treatment=info['treatment'],
                                   image_path=url_for('static', filename='uploads/' + file.filename))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
