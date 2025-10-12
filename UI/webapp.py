import streamlit as st
import pickle
import time
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, StackingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import cross_val_score, KFold
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PowerTransformer, RobustScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import optuna
from optuna.samplers import TPESampler
from optuna.pruners import MedianPruner
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))

st.set_page_config(page_title='Car Price Prediction', page_icon='📊', layout='wide')

# App Title
st.set_page_config(page_title="Predictions of Used Car Prices", layout="centered")
st.title("🚗 Predictions of Used Car Prices")
st.write('Welcome to the Car Price Prediction App!')
st.write('This app will assist you for predicting your car value in CarSome!')
st.write('This AI uses data directly from [CarSome advertisements](https://www.carsome.my/buy-car).')
st.warning("""
⚠️ **Disclaimer**  
1. The predicted price is an **estimated CarSome selling price** based on historical data and machine learning algorithms.  
2. Please note that the prediction is **not 100% accurate**, and actual prices may vary depending on vehicle condition, market demand, and other factors.  
3. If you are planning to **sell your car to CarSome**, the final offer might be **slightly lower** than the predicted selling price.
""")

st.markdown("Enter the car details and get an estimated price!")
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'best_regression.pkl'))
with open(model_path, 'rb') as file:  
    predict = pickle.load(file) # load previous trained model
brand = ['Honda', 'Mazda', 'Perodua', 'Mercedes-Benz', 'Toyota', 'Subaru',
       'Proton', 'Nissan', 'BMW', 'Mitsubishi', 'Lexus', 'Volkswagen',
       'Kia', 'Hyundai', 'Daihatsu', 'Peugeot', 'Suzuki', 'Renault',
       'MINI', 'Naza', 'Isuzu']
model = ['city e i-vtec 1.5', '3 skyactiv-g 1.5', 'cr-v tc-p vtec 1.5',
       'jazz v i-vtec 1.5', 'myvi av 1.5', 'civic tc vtec premium 1.5',
       'a250 amg line 2.0', 'sienta v 1.5', 'vios j 1.5',
       'axia gxtra 1.0', 'alza advance 1.5', 'alza se 1.5',
       'bezza advance premium 1.3', 'myvi h 1.5', 'xv p 2.0',
       'suprima s turbo premium 1.6', 'city v sensing 1.5',
       'axia style 1.0', 'almera e 1.5', 'saga premium 1.3',
       'grand livina comfort 1.6', '320i m sport 2.0',
       'city v i-vtec 1.5', 'cr-v tc vtec 1.5', 'aruz av 1.5',
       'myvi se 1.5', 'xpander 1.5', 'axia se 1.0', 'city s i-vtec 1.5',
       'myvi g 1.3', 'hr-v v 1.5', 'x70 tgdi premium 1.8',
       'jazz e i-vtec 1.5', 'bezza x premium 1.3',
       'x50 tgdi flagship 1.5', 'ativa h 1.0', 'jazz s i-vtec 1.5',
       'cx-5 skyactiv-g high 2.0', 'vellfire z g edition 2.5',
       'hr-v i-vtec rs 1.8', 'hr-v i-vtec v 1.8', 'ativa av 1.0',
       'almera vlp 1.0', 'xv gt edition eyesight 2.0', 'axia g 1.0',
       'saga standard 1.3', 'myvi x 1.3', 'voxy zs kirameki edition 2.0',
       'cr-v i-vtec 2.0', 'accord i-vtec vti-l 2.0', 'civic rs vtec 1.5',
       'vios e 1.5', 'cx-8 skyactiv-g high 2.5', 'br-v v i-vtec 1.5',
       'bezza x 1.3', 'hilux rogue dual cab 2.8', 'ct200h 1.8',
       'glc250 4matic amg line 2.0', 'hiace panel 2.5',
       'cx-8 skyactiv-g mid 2.5', 'civic tc vtec 1.5', 'iriz premium 1.6',
       'cx-3 skyactiv 2.0', 'persona elegance high line 1.6',
       'tiguan 280 tsi highline 1.4', 'alphard g s c package 2.5',
       'hr-v e 1.5', 'hilux gr sport dual cab 2.8', 'x50 standard 1.5',
       'cx-5 2.5g 4wd high t/c 2.5', 'cx-5 skyactiv-g gls 2.0',
       'passat tsi 1.8', 'vellfire z 2.4', 'axia advance 1.0',
       'hilux l-edition dual cab 2.8', 'civic s i-vtec 1.8',
       'carnival yp 2.2', 'persona standard 1.6', 'x-trail 2.0',
       'innova g 2.0', 'serena s-hybrid high-way star 2.0',
       'serena s-hybrid high-way star premium 2.0',
       'bezza g standard 1.0', 'grand starex executive 2.5',
       'inspira premium 2.0', '2 skyactiv-g 1.5', 'bezza advance 1.3',
       'iriz standard 1.3', 'cr-v i-vtec 2.4', 'accord tc vtec 1.5',
       'vios g 1.5', 'saga executive 1.3', 'navara pro-4x dual cab 2.5',
       'x50 premium 1.5', 'vios gx 1.5', '3 skyactiv-g high 2.0',
       'exora turbo premium 1.6', 'yaris g 1.5', 'myvi advance 1.5',
       '320i sport 2.0', 'outlander 2.4', 'gran max panel 1.5',
       '320i sport line 2.0', 'estima aeras 2.4', 'polo 1.6',
       'e250 avantgarde 2.0', 'alza ez 1.5', 'hr-v i-vtec e 1.8',
       'viva ez 1.0', 'hilux l-edition dual cab 2.4',
       'cx-3 skyactiv gvc 2.0', 'alza ezi 1.5',
       'grand livina cvtc comfort 1.8', '208 puretech 1.2',
       'navara se dual cab 2.5', 'rx350 f sport 3.5', 'aruz x 1.5',
       'triton quest dual cab 2.5', 'yaris e 1.5', '3 skyactiv-g gl 2.0',
       'asx 2.0', 'saga blm b-line 1.3', 'persona premium 1.6',
       'swift premier 1.5', 'triton vgt adventure x dual cab 2.4',
       'saga flx se 1.6', 'x70 tgdi executive 1.8',
       'x70 tgdi premium 1.5', 'hilux black edition dual cab 2.8',
       'almera vl 1.5', 'persona medium line 1.6', 'myvi ez 1.3',
       'n-box custom g l 0.7', 'myvi ezi 1.3', 'outlander 2.0',
       'hr-v i-vtec s 1.8', 'wr-v rs 1.5', 'c300 amg line 2.0',
       'attrage gs 1.2', 'avanza s 1.5', 'hilux g dual cab 2.8',
       'innova e 2.0', 'cx-5 skyactiv-g gl 2.0',
       'triton vgt dual cab 2.4', 'vios trd sportivo 1.5',
       'iriz executive 1.6', 'forester l eyesight 2.0',
       'grand livina comfort 1.8', 'optima - 2.0', 'b180 1.7',
       'cx-30 skyactiv-g high 2.0', 'cx-5 skyactiv-g high spec 2.0',
       'alza x 1.5', 'arteon r-line 4motion fastback 2.0',
       'passat 380 tsi highline 2.0', 'c-hr 1.8', 'hr-v e:hev rs 1.5',
       'cx-30 skyactiv-g high+ premium 2.0', 'viva ezi 1.0',
       'x50 executive 1.5', 'city s+ i-vtec 1.5',
       'vento tsi highline 1.2', 'cc sport 1.8',
       'serena s-hybrid high-way star two-tone color 2.0',
       'hiace window 2.7', 'vios sports edition 1.5',
       'saga premium s 1.3', 'city rs i-vtec 1.5', 'captur tce 120 1.2',
       'almera vlt 1.0', 'cx-5 skyactiv-g gls 2.5',
       'cx-30 skyactiv-g high+ 2.0', 'x70 tgdi standard 1.8',
       'hilux e dual cab 2.4', '3 door cooper s 2.0',
       'persona executive 1.6', 'rx300 f sport 2.0',
       'x3 xdrive30i m sport 2.0', 'x70 tgdi executive 1.5',
       'civic v vtec 1.5', 'city rs e-hev 1.5', 'sportage ql 2.0',
       'alza av 1.5', 'viva ez elite 1.0', 'ativa x 1.0', 'bezza g 1.0',
       'x-trail 4wd 2.5', 'exora turbo executive 1.6',
       'br-v e i-vtec 1.5', 'hilux v dual cab 2.4', 'livina x-gear 1.6',
       'civic navi i-vtec 2.0', 'glc200 exclusive 2.0',
       'fortuner srz 2.7', 'sylphy vl 1.8', 'a200 progressive line 1.3',
       'preve cfe executive 1.6', '86 2.0', 'countryman cooper s 2.0',
       'civic e vtec 1.5', 'triton vgt athlete dual cab 2.4',
       'preve executive 1.6', 'forte sx 1.6', 'b200 sport tourer 1.6',
       'captur 1.2', 'almera v 1.5', 'rush s 1.5', 'e200 avantgarde 2.0',
       'persona sv 1.6', 'polo comfortline 1.6',
       'tiguan allspace elegance 1.4', 'swift glx-s 1.4',
       'corolla altis v 2.0', 'corolla cross hybrid 1.8',
       'exora bold cfe premium 1.6', 'swift glx 1.4',
       'civic s-l i-vtec 1.8', 'c200 avantgarde 1.5',
       '3 skyactiv-g high plus 2.0', '3 skyactiv-g 2.0',
       'x1 sdrive20i m sport 2.0', 'c200 amg line 2.0', 'stream rsz 1.8',
       'jazz i-vtec 1.5', 'camry e 2.0', 'optima k5 2.0',
       'triton vgt 2.4', 'camry v 2.5', 'd-max z-prestige dual cab 2.5',
       'jimny jlx 1.3', 'grand starex royale 2.5', 'harrier luxury 2.0',
       'carnival 2.2', 'accord i-vtec vti 2.0', 'axia x 1.0',
       's70 flagship x 1.5', 'rio ex 1.4', 'city v(sensing) sensing 1.5',
       'accord tc premium 1.5', 'saga flx plus 1.3',
       'd-max premium dual cab 1.9', 'myvi x 1.5',
       'ertiga vvt plus executive 1.4', 'c300 avantgarde amg line 2.0',
       'iriz executive 1.3', 'wr-v v 1.5', 'forester s 2.0',
       's70 executive 1.5', 'forester p 2.0', '2 skyactiv-g gvc plus 1.5',
       'nv200 semi panel 1.6', 'ertiga vvt executive 1.4', 'cerato 1.6',
       'iriz active 1.6', 'veloz 1.5', 'grand starex executive plus 2.5',
       'cerato yd 1.6', 'corolla altis g 1.8', 'x-trail mid 2.0',
       'hilux single cab 2.4', 'attrage se 1.2', 'alza h 1.5',
       'wr-v s 1.5', '318i luxury 1.5', 'harrier premium advanced 2.0',
       'picanto ex 1.2', 'camry g 2.0', 'picanto 1.2',
       'stream i-vtec rsz 1.8', 'rio sx 1.4', 'lancer gte 2.0']
highlight = ['daily drive', 'upgrade daily drive', 'compact suv',
       'national daily drive', 'luxury', 'family drive', 'executive',
       'adventure', 'commercial']
location = ['carsome chan sow lin, kuala lumpur',
       'carsome kepong, kuala lumpur', 'carsome kuantan, pahang',
       'carsome taman sutera (skudai), johor',
       'carsome johor jaya, johor', 'carsome juru, pulau pinang',
       'carsome cheras, selangor', 'carsome pj automall, selangor',
       'carsome melaka, melaka', 'carsome kota kinabalu, sabah',
       'carsome alor setar, kedah',
       'carsome kuala terengganu, terengganu', 'carsome temerloh, pahang',
       'carsome setiawangsa, kuala lumpur', 'carsome sitiawan, perak',
       'carsome ipoh, perak', 'carsome seremban, negeri sembilan',
       'carsome setia spice, pulau pinang',
       'carsome kota bharu, kelantan', 'carsome kuching, sarawak']
        
# Input Form
with st.form("form_mobil"):
    col1, col2 = st.columns(2)
        
    with col1:
            Year = st.slider("Production Year", 2008, 2025, 2018)
            Brand = st.selectbox("Car Brand", brand)
            Model = st.selectbox("Car Model", model)
            Transmission = st.selectbox("Transmission", ['A', 'M'])

    with col2:
            Mileage = st.number_input("Mileage (km)", 109, 250364, 50000, step=1)
            Highlight = st.selectbox("Highligth", highlight)
            Location = st.selectbox("Location", location)
        
    submitted = st.form_submit_button("Price Predict")

# Inference
if submitted:
    # Contoh dummy preprocessing
    X_input = pd.DataFrame([{
    'Year': Year,
    'Brand': Brand,
    'Model': Model,
    'Mileage(km)': Mileage,
    'Transmission': Transmission,
    'Highlight': Highlight,
    'Location': Location
    }])

    y_pred = predict.predict(X_input) 

    price_pred = np.expm1(y_pred[0])

    st.success(f"💰 Estimated Price of Used Cars: **RM {price_pred:,.2f}**")

    st.info("Price estimation based on historical data of similar cars.")
