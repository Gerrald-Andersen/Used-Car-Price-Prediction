# 📁 `UI/` — Streamlit Dashboard for Used Car Price Prediction

This folder contains the **Streamlit-based web application** that allows users to input car details and receive real-time price predictions.  
The dashboard integrates preprocessing logic and the trained regression model to provide an **interactive and user-friendly estimation tool** for used car prices in Malaysia.

---

## 🚀 Features

- **User Input Form**: Enter car details such as brand, model, year, mileage, transmission, etc.  
- **Instant Price Prediction**: Uses the trained regression model (`best_regression.pkl`) to output estimated prices.  
- **Data Visualization**: Optional charts to explore feature distributions and predicted price trends.  
- **Interactive Interface**: Designed for non-technical users with responsive feedback for invalid or missing inputs.  

---

## 📦 Key Components

| Section              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Configuration        | Sets page title, layout, and basic Streamlit settings                       |
| Input Form           | Collects car features from the user                                         |
| Preprocessing        | Applies encoding, scaling, and transformations used during model training   |
| Model Loading        | Loads trained regression model from `lib/best_regression.pkl`               |
| Prediction Logic     | Generates estimated car price based on user input                            |
| Visualization        | Displays optional charts and data insights                                  |
| Output Display       | Shows predicted price in a readable format                                   |

---

## 🔄 Usage

1. Ensure all dependencies are installed
2. Launch the web application
3. Fill in the car details in the input form
4. Click *Predict* to see estimated price

---

## ⚖️ License

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
