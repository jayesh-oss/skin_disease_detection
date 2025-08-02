from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sys
import os

# -------------------------------
# Load trained model
model = load_model("model/skin_model.h5")

# Define class names (must match training order)
class_names = ['Acne', 'Hyperpigmentation', 'Nail_psoriasis', 'SJS-TEN', 'Vitiligo']

# -------------------------------
# Load image from command line
if len(sys.argv) != 2:
    print("Usage: python predict.py <path_to_image>")
    exit()

img_path = sys.argv[1]

if not os.path.exists(img_path):
    print("File does not exist.")
    exit()

# -------------------------------
# Load and preprocess image
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = img_array / 255.0  # Normalize
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

# -------------------------------
# Predict
prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction)

# -------------------------------
# Output result
print("\n===============================")
print(f"Predicted Disease: {predicted_class}")
print(f"Confidence: {confidence:.2f}")
print("===============================\n")
