import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="App Rating Predictor", page_icon="📱", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("### Predict how users will rate your Android app 📱")

st.title("Google Play App Rating Predictor")

model = joblib.load("rating_model.pkl")

all_categories = ['ART', 'AUTOMOTIVE', 'BUSINESS', 'COMMUNICATION', 'EDUCATION',
                  'ENTERTAINMENT', 'HEALTH', 'LIFESTYLE', 'SHOPPING',
                  'TRAVEL', 'SYSTEM']

# Input widgets
reviews = st.number_input("Number of Reviews", min_value=0)
price = st.number_input("Price ($)", min_value=0.0)
size = st.number_input("Size (MB)", min_value=0.0)
installs = st.number_input("Number of Installs", min_value=0)

category = st.selectbox("App Category", ['No Category'] + all_categories)
category_encoded = [1 if category == cat else 0 for cat in all_categories]

# Example input array — expand this to match your actual model input
input_data = np.array([[reviews, price, size, installs]+ category_encoded])

if st.button("Predict Rating"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Rating: {prediction[0]:.2f}")