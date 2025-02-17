import streamlit as st
import random
import numpy as np
import tensorflow as tf
import pandas as pd

# Load the trained UV index prediction model
model_path = "C:\\Users\\sirya\\Downloads\\capstone\\LSTM_model.keras"
model = tf.keras.models.load_model(model_path)

# Read the sunscreen data from CSV file
sunscreens_df = pd.read_csv("C:\\Users\\sirya\\Downloads\\capstone\\sunscreens.csv")
sunscreens = sunscreens_df.to_dict('records')

# Placeholder function to fetch and prepare weather data for the given city
def fetch_weather_data(city):
    # This function should return a NumPy array of shape (1, 30, 15)
    # Replace this with actual data fetching and preparation logic
    features = np.random.random((1, 30, 15))
    return features

# Function to recommend sunscreen based on predicted UV index
def recommend_sunscreen(uv_index):
    if uv_index <= 2:
        spf_range = (15, 30)
    elif uv_index <= 5:
        spf_range = (30, 50)
    elif uv_index <= 7:
        spf_range = (50, 100)
    else:
        spf_range = (50, 100)

    filtered_sunscreens = [s for s in sunscreens if spf_range[0] <= s["SPF"] <= spf_range[1]]
    return random.choice(filtered_sunscreens) if filtered_sunscreens else None

# Streamlit UI
st.set_page_config(
    page_title="UV Index Predictor & Sunscreen Recommender",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    body {
        background-color: #000000; /* Black background */
        color: #FFFFFF; /* White text */
    }
    .main {
        background-color: #000000;
        padding: 1rem;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown li {
        color: #FFFFFF; /* White text for all headings and paragraphs */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌞 UV Index Predictor & Sunscreen Recommender")
st.markdown("""
Welcome to the **UV Index Predictor & Sunscreen Recommender**! 🌞

Simply enter your city to predict the UV index and get a sunscreen recommendation tailored to your needs.

**Steps:**
1. Enter your city in the input box below.
2. Click the 'Predict UV Index' button.
3. Get your predicted UV index and recommended sunscreen.

Stay safe and protect your skin! 😊
""")

# User input for city
city = st.text_input("Enter your city:")

# Button to predict UV index
if st.button("Predict UV Index"):
    if city:
        # Fetch weather data for the city
        features = fetch_weather_data(city)
        uv_pred = model.predict(features)[0][0]  # Predict UV index

        # Get sunscreen recommendation
        sunscreen = recommend_sunscreen(uv_pred)

        # Display results
        st.subheader(f"Predicted UV Index for {city}: {uv_pred:.2f}")
        if sunscreen:
            st.success(f"Recommended Sunscreen: {sunscreen['Sunscreen Name']} (SPF {sunscreen['SPF']})")
        else:
            st.error("No suitable sunscreen found.")
    else:
        st.warning("Please enter a city.")
