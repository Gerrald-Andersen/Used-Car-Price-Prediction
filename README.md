# 🚗 Used Car Price Prediction WebApp  
[Streamlit WebApp](https://used-car-price-prediction-gerrald-andersen.streamlit.app/)  

## 🧭 Purpose  

This web application was developed to assist car owners and buyers in **estimating the fair market value of used cars in Malaysia**, particularly from listings on Carsome Malaysia.  
By providing data-driven price predictions, it helps users **avoid being misled or underpaid** when selling or purchasing second-hand vehicles.  
While not a replacement for professional valuation, it serves as a reliable tool to support better decision-making in the used car market.  

---

## ⚙️ What I Did  

The development process involved several key stages:  

1. **Task Plan**  
   - Created a clear project plan outlining each development step to maintain focus and ensure efficient progress toward the final goal — a predictive web dashboard that simplifies car price estimation.  

2. **Data Collection**  
   - Conducted **web scraping** on [Carsome Malaysia](https://www.carsome.my/) to gather real-world car listing data, including details such as brand, model, year, mileage, transmission, and selling price.  

3. **Data Cleaning & Feature Engineering**  
   - Cleaned raw scraped data by handling missing values, encoding categorical variables, and normalizing numeric columns.  
   - Engineered new features to improve prediction performance and meet model training requirements.  

4. **Data Visualization**  
   - Created **interactive visualizations** to analyze data distribution, identify outliers, and better understand relationships between features (e.g., year vs. price, mileage vs. price).  

5. **Model Development**  
   - Trained and compared several regression models to predict used car prices:  
     - **CatBoost Regressor**  
     - **LightGBM Regressor**  
     - **Random Forest Regressor (RFR)**  
     - **XGBoost Regressor (XGB)**  
   - Evaluated each model’s performance and selected the best one for integration into the web application.  

6. **Web Application Deployment**  
   - Built an intuitive **Streamlit dashboard** to allow users to input car details and instantly get predicted prices.  
   - Designed a simple and clean interface to make it accessible even for non-technical users.  

---

## 📊 Results  

Although the prediction results are **not perfectly accurate**, they provide a **reasonable estimation close to the real market price**.  
This project successfully demonstrates the integration of **machine learning with real-world automotive data**, offering a practical tool for consumers in Malaysia’s used car market.  

Key learnings include:  
- Real-world web scraping and data preparation  
- Applied regression modeling and model comparison  
- Web-based ML deployment using Streamlit  

---

## 🚀 Future Improvements  

Planned future developments include:  

- **Model Tuning**  
  - Apply advanced hyperparameter optimization to further improve prediction accuracy.  

- **Expanded Dataset**  
  - Integrate data from multiple platforms and extend coverage **beyond Malaysia** to include international used car markets.  

- **Feature Enhancement**  
  - Include additional attributes such as condition score, service records, and accident history.  

- **Cloud Deployment**  
  - Host the app on a scalable cloud environment for faster response and global availability.  

---

## 🛠️ Technical Skills  

### 💻 Programming Languages  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  

### 📚 Frameworks / Libraries  
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![CatBoost](https://img.shields.io/badge/CatBoost-FFDE00?style=for-the-badge&logoColor=black) ![LightGBM](https://img.shields.io/badge/LightGBM-00C853?style=for-the-badge&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-AA0000?style=for-the-badge&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-2E4053?style=for-the-badge) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  

### 🧰 Developer Tools  
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=black) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)  

### 🤖 Machine Learning  
![Regression Modeling](https://img.shields.io/badge/Regression%20Modeling-8E44AD?style=for-the-badge) ![Feature Engineering](https://img.shields.io/badge/Feature%20Engineering-1ABC9C?style=for-the-badge)  

### 🔌 APIs and Integrations  
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-3498DB?style=for-the-badge)  

### 🖥️ Operating Systems  
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)  

---

## ⚖️ LICENSE  

This project is proprietary. All rights reserved © 2025 Gerrald Andersen.  
No part of this repository may be copied, modified, reused, or redistributed without explicit written permission.  

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red.svg)
