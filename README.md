# 🩺 SkinDetect — AI-Powered Skin Disease Detection

A full-stack web application that uses deep learning to analyze skin images and detect dermatological conditions. Built with **Flask**, **TensorFlow/Keras**, and **Bootstrap 5**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Detectable Conditions](#detectable-conditions)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Development Roadmap](#development-roadmap)
- [Disclaimer](#disclaimer)

---

## Overview

SkinDetect allows users to upload a photo of a skin condition and receive an AI-powered preliminary analysis. The system identifies the condition, provides a confidence score, and generates a comprehensive medical report with symptoms, treatments, and prevention tips.

> ⚠️ **This tool is for educational purposes only and is NOT a substitute for professional medical advice.**

---

## ✅ Features (Completed)

### Core Functionality
- **AI Image Analysis** — Upload a skin image and get an instant classification with confidence score
- **Medical Reports** — Detailed reports with symptoms, treatment options, prevention tips, and dermatologist consultation urgency
- **User Authentication** — Secure registration, login, and session management with Flask-Login
- **Prediction Dashboard** — View all past analysis results in a card-based layout
- **Delete Predictions** — Remove individual prediction records and their associated images

### UI/UX
- **Premium Design** — Modern UI with Inter font, glassmorphism cards, smooth animations, and gradient navbar
- **Dark Mode** — Full dark mode toggle with `localStorage` persistence and CSS variable theming
- **Responsive Layout** — Mobile-friendly design using Bootstrap 5 grid system

### Security
- **CSRF Protection** — All forms protected with Flask-WTF CSRF tokens (no session expiry)
- **Secure Uploads** — UUID-based filenames + `secure_filename()` to prevent directory traversal
- **Private Image Storage** — Images stored in `instance/uploads/`, served via authenticated route
- **Access Control** — Users can only view/delete their own predictions (IDOR protection)
- **Upload Limits** — 5 MB max file size, restricted to JPG/PNG formats

### Additional Features
- **Find a Dermatologist** — Embedded Google Maps locator to find nearby dermatology clinics
- **Graceful Error Handling** — Custom CSRF error handler with friendly flash messages

---

## 🔬 Detectable Conditions

The AI model is trained to classify **5 skin conditions**:

| # | Condition | Severity | Description |
|---|-----------|----------|-------------|
| 1 | **Nail Psoriasis** | Moderate | Autoimmune condition affecting fingernails and toenails |
| 2 | **SJS-TEN** | 🔴 Critical | Life-threatening skin reaction requiring emergency care |
| 3 | **Vitiligo** | Mild | Autoimmune loss of skin pigmentation |
| 4 | **Acne Vulgaris** | Mild–Moderate | Common condition from clogged hair follicles |
| 5 | **Hyperpigmentation** | Mild | Darkened patches from excess melanin deposits |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, Flask 2.3 |
| **ML Model** | TensorFlow / Keras (CNN, 128×128 input, 5-class softmax) |
| **Database** | SQLite via SQLAlchemy |
| **Auth** | Flask-Login + Flask-Bcrypt |
| **Security** | Flask-WTF (CSRF) |
| **Frontend** | Bootstrap 5, Bootstrap Icons, Google Fonts (Inter) |
| **Styling** | Custom CSS with CSS variables for theming |

---

## 📁 Project Structure

```
skin_disease_detection/
├── app.py                  # Main Flask application & routes
├── disease_info.py         # Medical knowledge base for 5 conditions
├── train_model.py          # Model training script
├── predict.py              # Standalone prediction utility
├── requirements.txt        # Python dependencies
│
├── model/
│   └── skin_model.h5       # Trained Keras model
│
├── data/                   # Training dataset (5 class folders)
│   ├── Nail_psoriasis/
│   ├── SJS-TEN/
│   ├── Vitiligo/
│   ├── acne/
│   └── hyperpigmentation/
│
├── instance/
│   ├── database.db          # SQLite database (auto-generated)
│   └── uploads/             # User-uploaded images (private)
│
├── static/
│   └── css/
│       └── style.css        # Custom styles + dark mode variables
│
└── templates/
    ├── layout.html          # Base template (navbar, footer, dark mode JS)
    ├── index.html           # Home page with upload form
    ├── login.html           # Login page
    ├── register.html        # Registration page
    ├── dashboard.html       # Prediction history cards
    ├── result.html          # Prediction result page
    ├── report.html          # Full medical report
    └── locator.html         # Find a Dermatologist (Google Maps)
```

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/jayesh-oss/skin_disease_detection.git
cd skin_disease_detection

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

The app will start at **http://127.0.0.1:5000**

### Environment Variables (Optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `secretkey123_dev` | Flask session secret key (set a strong value in production) |

---

## 💡 Usage

1. **Register** an account at `/register`
2. **Login** at `/login`
3. **Upload** a skin image on the home page
4. **View** the AI prediction result with confidence score
5. **Read** the detailed medical report with symptoms, treatments, and prevention tips
6. **Find** a nearby dermatologist via the locator page
7. **Manage** your prediction history on the dashboard (view reports or delete entries)

---

## 🗺️ Development Roadmap

### ✅ Completed

- [x] **V1** — Premium UI redesign (Inter font, animations, medical color palette)
- [x] **V2** — Post-detection medical reports with symptom/treatment/prevention data
- [x] **V3** — Security suite (CSRF, UUID uploads, private storage, IDOR protection)
- [x] **V4** — Dark mode toggle + Find a Dermatologist locator
- [x] **V5** — Fixed model prediction mismatch (was always showing "Melanoma")
- [x] **V6** — Delete prediction functionality + Keras crash fix + CSRF expiry fix

### 🔜 Planned Features

- [ ] **📄 PDF Export** — Download medical reports as PDF using `html2pdf.js`
- [ ] **👤 User Profiles** — Add demographics (age, skin type) for better risk assessment
- [ ] **📊 Admin Dashboard** — Analytics interface with Chart.js (total predictions, disease distribution)
- [ ] **📱 PWA Support** — Progressive Web App for mobile installability
- [ ] **🔄 Model Improvement** — Expand dataset and add more detectable conditions
- [ ] **🚀 Production Deployment** — Deploy to Render/Railway with Gunicorn

---

## ⚠️ Disclaimer

This application provides **preliminary AI-based analysis only**. It is designed for educational and informational purposes. The predictions made by this system:

- Are **not** a medical diagnosis
- Should **not** replace consultation with a qualified dermatologist
- May have **limited accuracy** depending on image quality and conditions

**If the system detects SJS-TEN**, it will display an urgent warning — this is a life-threatening medical emergency requiring immediate hospital care.

---

