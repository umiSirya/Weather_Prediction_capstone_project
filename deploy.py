import streamlit as st
import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Your API key
api_key = "4091f433030f47658ea85020253001"

# List of columns to drop (including "Weather Condition")
columns_to_drop = [
    "Country", "Local Time", "Visibility (km)", "Weather Condition", "Tomorrow's Condition", "Wind Direction", "Longitude", "Latitude"
]

# List of city names
city_names = [
    'Bomet', 'Bungoma', 'Chuka', 'Eldoret', 'Embu', 'Garissa', 'Homa Bay', 'Isiolo', 'Kajiado', 'Kakamega', 'Kendu Bay', 
    'Kericho', 'Kiambu', 'Kisii', 'Kisumu', 'Kitale', 'Kitui', 'Lamu', 'Lodwar', 'Machakos', 'Malindi', 'Mandera', 
    'Marsabit', 'Meru', 'Mombasa', "Murang'a", 'Mwingi', 'Nairobi', 'Nakuru', 'Nandi Hills', 'Nyeri', 'Ruiru', 
    'Samburu', 'Siaya', 'Taita', 'Taveta', 'Thika', 'Trans', 'Voinjama Airport', 'Wajir'
]

# Load the trained UV index prediction model
model_path = "C:\\Users\\sirya\\Downloads\\capstone\\model_LSTM.keras"
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Read the sunscreen data from CSV file with a different encoding
try:
    sunscreens_df = pd.read_csv("C:\\Users\\sirya\\Downloads\\capstone\\sunscreens.csv", encoding='ISO-8859-1')
    sunscreens = sunscreens_df.to_dict('records')
except Exception as e:
    st.error(f"Error loading sunscreen data: {e}")

# Function to fetch and prepare weather data for the given city
def fetch_weather_data(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    weather_data = response.json()
    df = pd.json_normalize(weather_data)
    
    # Drop unnecessary columns
    df.drop(columns=columns_to_drop, inplace=True)

    # Convert 'Sunrise' and 'Sunset' to numerical features (minutes since midnight)
    df['Sunrise'] = pd.to_datetime(df['Sunrise'], format='%I:%M %p').dt.hour * 60 + pd.to_datetime(df['Sunrise'], format='%I:%M %p').dt.minute
    df['Sunset'] = pd.to_datetime(df['Sunset'], format='%I:%M %p').dt.hour * 60 + pd.to_datetime(df['Sunset'], format='%I:%M %p').dt.minute

    # One-hot encode the 'City' column and drop the first column to avoid multicollinearity
    df = pd.get_dummies(df, columns=['City'], drop_first=True)

    # Rename encoded column names to contain only the city name and convert their dtype to float64
    encoded_columns = [col for col in df.columns if col.startswith('City_')]
    new_column_names = {col: col.split('_')[1] for col in encoded_columns}
    df.rename(columns=new_column_names, inplace=True)

    # Convert the dtype of city columns to float64
    city_columns = list(new_column_names.values())
    df[city_columns] = df[city_columns].astype('int64')

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Separate target variable
    uv_index = df[['UV Index']]

    # Standardize the features (excluding 'UV Index')
    feature_scaler = StandardScaler()
    scaled_features = feature_scaler.fit_transform(df.drop(columns=['UV Index']))

    # Standardize the target variable
    target_scaler = StandardScaler()
    scaled_target = target_scaler.fit_transform(uv_index)

    # Convert scaled features back to a DataFrame
    scaled_df = pd.DataFrame(scaled_features, columns=df.columns[df.columns != 'UV Index'])

    # Add scaled 'UV Index' back
    scaled_df['UV Index'] = scaled_target

    return scaled_df

# Updated Streamlit UI to use the new fetch_weather_data function
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
        if features is not None:
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
