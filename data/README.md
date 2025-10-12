# 📁 `data/` — Datasets for Used Car Price Prediction

This folder contains both **raw and processed datasets** used throughout the car price prediction pipeline.  
The data is sourced from **Carsome Malaysia** through web scraping and is cleaned, feature-engineered, and optionally outlier-processed before being fed into the machine learning models.

---

## 📦 Folder Structure

| Folder / File                         | Description                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| `raw/carsome_data_raw.csv`             | Raw dataset collected directly from Carsome Malaysia listings               |
| `processed/carsome_data_clean.csv`     | Cleaned dataset with missing values handled, categorical features encoded, and numeric features scaled |
| `processed/carsome_data_super_clean.csv` | Further cleaned dataset with outliers removed for improved model performance |

---

## 🔄 Data Flow

1. **`carsome_data_raw.csv`**  
   - Contains all raw car listing information scraped from Carsome Malaysia.  
   - Includes features such as brand, model, year, mileage, transmission, fuel type, and price.  

2. **`carsome_data_clean.csv`**  
   - Cleaned version of the raw dataset.  
   - Missing values handled, categorical variables encoded, numeric features normalized.  
   - Ready for initial model training and data visualization.  

3. **`carsome_data_super_clean.csv`**  
   - Further processed dataset with outliers removed.  
   - Provides a more robust input for model training and helps improve prediction accuracy.  

---

## 🧠 Usage Notes

- **Raw dataset** is retained for reproducibility and audit purposes.  
- **Cleaned datasets** are used for feature engineering, model training, and evaluation.  
- **Super-clean dataset** (without outliers) is recommended for models sensitive to extreme values.  

---

## ⚖️ License

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
