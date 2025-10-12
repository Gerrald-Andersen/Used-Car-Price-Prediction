# 📁 `lib/` — Trained Model Storage

This folder contains the **trained machine learning model** used by the **Car Price Prediction Web App**.  
The model stored here is loaded by the Streamlit interface (`webapp.py`) to make real-time predictions on car prices based on user input.

---

## 📦 Contents

| File / Folder           | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `best_regression.pkl`    | The best-performing regression model for predicting used car prices.    |

---

## 🧠 Model Description

- The file `best_regression.pkl` contains a **pre-trained regression model**, serialized using Python's `pickle` module.  
- This model was trained and tuned using various algorithms (e.g., Random Forest, XGBoost, LightGBM, and CatBoost) — the best-performing one was saved under this filename.
- The model predicts the **estimated market price** of a used car based on key input features such as:
  - Car brand and model  
  - Year of manufacture  
  - Mileage  
  - Transmission type  
  - Engine size  
  - Fuel type  
  - Location or market region  

---

## ⚙️ How It Works

1. When a user inputs car details through the **Streamlit web app**, the app:
   - Collects all input fields from the form.  
   - Encodes and scales the features as per the training pipeline.  
   - Loads the trained model from `lib/best_regression.pkl`.  
   - Generates a predicted car price (in local currency).  

2. The prediction result is then displayed instantly in the UI.

---

## ⚖️ License

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
