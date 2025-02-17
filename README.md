# UV Monitor & Sunscreen Guide
# <h2> Project Overview </h2>
In an age where sun safety is paramount, this project aims to provide individuals with accurate and timely predictions of UV index levels based on their city. Utilizing advanced machine learning algorithms, this project analyzes real-time weather data to forecast UV index levels. Additionally, it offers personalized sunscreen recommendations to ensure optimal skin protection.

By seamlessly integrating data from weather APIs and predictive modeling, UV Predictor & SPF Guide empowers users to make informed decisions about sun exposure and skin care, enhancing public health and awareness.

Please find the link to the App Here: 


# <h2> Problem Statement </h2>
Excessive exposure to ultraviolet (UV) radiation is a significant public health concern, leading to increased risks of skin cancer, sunburns, and other harmful effects on human health. While UV radiation levels fluctuate based on location, time of day, and weather conditions, many individuals lack the awareness and tools to effectively manage their sun exposure. This gap in knowledge and accessibility results in preventable health issues and decreased quality of life.

The project addresses this issue by providing accurate, city-specific UV index predictions and personalized sunscreen recommendations. By leveraging real-time weather data and advanced machine learning algorithms, the project empowers users to make informed decisions about their sun exposure and skin protection, ultimately promoting healthier lifestyles and reducing the risk of UV-related health problems.

# <h2> Data Overview</h2>
The weather data used in this project is from: [https://www.weatherapi.com/](https://www.weatherapi.com/). 
It contains comprehensive real-time weather information, and the target variable is the UV index. 
The data includes the following columns:

1. **City:** The name of the city.
2. **Country:** The name of the country.
3. **Latitude:** The geographic latitude of the city.
4. **Longitude:** The geographic longitude of the city.
5. **Local Time:** The current local time in the city.
6. **Temperature (°C):** The current temperature in degrees Celsius.
7. **Feels Like (°C):** The perceived temperature in degrees Celsius, considering factors like wind and humidity.
8. **Humidity (%):** The percentage of humidity in the air.
9. **Pressure (mb):** The atmospheric pressure in millibars.
10. **Wind Speed (km/h):** The speed of the wind in kilometers per hour.
11. **Wind Direction:** The direction from which the wind is blowing.
12. **UV Index:** The ultraviolet index indicating the strength of UV radiation.
13. **Visibility (km):** The distance one can see clearly, in kilometers.
14. **Weather Condition:** A brief description of the current weather conditions (e.g., clear, cloudy).
15. **Air Quality Index (US):** The air quality index based on US standards.
16. **PM2.5:** The concentration of particulate matter less than 2.5 micrometers.
17. **PM10:** The concentration of particulate matter less than 10 micrometers.
18. **CO (Carbon Monoxide):** The concentration of carbon monoxide in the air.
19. **NO2 (Nitrogen Dioxide):** The concentration of nitrogen dioxide in the air.
20. **SO2 (Sulfur Dioxide):** The concentration of sulfur dioxide in the air.
21. **Tomorrow's Max Temp (°C):** The maximum temperature forecasted for the next day in degrees Celsius.
22. **Tomorrow's Min Temp (°C):** The minimum temperature forecasted for the next day in degrees Celsius.
23. **Tomorrow's Condition:** The forecasted weather conditions for the next day.
24. **Sunrise:** The local time of sunrise.
25. **Sunset:** The local time of sunset.

<h2>Exploratory Data analysis</h2>
1. **Description of summary statistics for our numeric columns**: Provides an overview of the data by highlighting its range, spread, and potential outliers.
<h3> Step 1: Loading of Data and Understanding the Dataset </h3>
The first step is loading the data and understanding the dataset which involves reviewing the dataset's columns, types, and summary statistics to gain insights into the data.

<h3> Step 2: Identify Key Attributes </h3>
These are the most important features or columns that provide valuable information for analysis and model building.

<h3> Step 3: EDA - Exploring the Dataset </h3>
EDA involves visually and statistically exploring a dataset to uncover patterns, trends, and relationships.

<h3> Step 4: Data Preprocessing </h3>
Data preprocessing involves cleaning, transforming, and organizing raw data into a format that can be effectively used for analysis and model building. Some of the steps include checking for missing values, encoding, feature engineering among others.

<h3> Step 6:</h3>

<h3> Step 7:</h3>

<h3>Next Steps - Deploying UV Monitor & Sunscreen Guide</h3>
The next phase of my project involves deploying the UV Predictor & SPF Guide using Streamlit to create an interactive and user-friendly interface. Streamlit will enable users to input their city and receive real-time UV index predictions along with personalized sunscreen recommendations. By leveraging this platform, we aim to enhance accessibility and ensure users can make informed decisions about their sun protection with ease.
