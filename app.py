import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="App Rating Predictor", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1 {
            color: #333333;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 24px;
        }
        .css-1aumxhk {
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📱 Google Play App Rating Predictor")
st.markdown("Use this tool to estimate the expected rating of your Android app based on key information.")
st.markdown("---")

model = joblib.load("rating_model.pkl")

all_categories = ['ART', 'AUTOMOTIVE', 'BUSINESS', 'COMMUNICATION', 'EDUCATION',
                  'ENTERTAINMENT', 'HEALTH', 'LIFESTYLE', 'SHOPPING',
                  'TRAVEL', 'SYSTEM']

st.subheader("🔧 App Details")

col1, col2 = st.columns(2)
with col1:
    reviews = st.number_input("Number of Reviews", min_value=0)
    price = st.number_input("Price (USD)", min_value=0.0)
with col2:
    size = st.number_input("App Size (MB)", min_value=0.0)
    installs = st.number_input("Number of Installs", min_value=0)

category = st.selectbox("App Category", all_categories)
category_encoded = [1 if category == cat else 0 for cat in all_categories]

input_data = np.array([[reviews, price, size, installs] + category_encoded])

st.markdown("---")
if st.button("Predict Rating"):
    prediction = model.predict(input_data)
    st.success(f"⭐ Predicted Rating: **{prediction[0]:.2f} / 5.0**")

st.markdown("---")

