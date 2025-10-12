# 📁 `src/` — Core Modules for Used Car Price Prediction  

This folder contains the core components of the **Used Car Price Prediction** project, covering every stage from data collection and preprocessing to model development.  
All modules are designed to work together as a complete machine learning pipeline and integrate seamlessly with the Streamlit web dashboard.  

---

## 📦 Module Structure  

| Folder / File                              | Purpose                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------|
| `notebooks/1. Data_Collection.ipynb`          | Performs web scraping from Carsome Malaysia to collect raw used car listings data |
| `notebooks/2. Features_Engineering.ipynb`     | Cleans and preprocesses the raw dataset (handles missing values, encodes features, etc.) |
| `notebooks/3. Data_Visualization.ipynb`       | Visualizes the dataset **before outlier removal** to understand data distribution |
| `notebooks/4. Features_Engineering.ipynb` | Removes outliers and refines the dataset for improved model accuracy |
| `notebooks/5. Data_Visualization.ipynb` | Visualizes the dataset **after outlier removal** to validate improvements |
| `models/ML_Development.ipynb`              | Develops and evaluates multiple regression models (CatBoost, LightGBM, Random Forest, XGBoost) for price prediction |

---

## 🔄 Execution Flow  

1. **`Data_Collection.ipynb`**  
   - Scrapes car listings from **Carsome Malaysia** and stores them as a structured dataset.  

2. **`Features_Engineering.ipynb`**  
   - Performs initial data cleaning, handles missing values, encodes categorical variables, and prepares the dataset for analysis.  

3. **`Data_Visualization.ipynb`**  
   - Generates visualizations to explore the raw dataset before outlier removal, identifying trends and anomalies.  

4. **`Features_Engineering_Outlier.ipynb`**  
   - Detects and removes data outliers to ensure more robust model performance.  

5. **`Data_Visualization_Cleaned.ipynb`**  
   - Re-visualizes the cleaned dataset after outlier removal to confirm improved data quality.  

6. **`ML_Development.ipynb`**  
   - Trains, compares, and evaluates machine learning models — including **CatBoost**, **LightGBM**, **Random Forest**, and **XGBoost** — for predicting used car prices.  
   - Exports the best-performing model for use in the Streamlit application.  

---

## 🧠 Usage Notes  

- Each notebook is **modular**, allowing for step-by-step execution or individual testing.  
- Recommended pipeline order:  
  `collect → clean → visualize (pre) → remove outliers → visualize (post) → model`  
- The trained model and any preprocessing pipelines are stored in the `lib/` folder for integration with the Streamlit dashboard.  

---

## ⚖️ LICENSE  

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.  

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
