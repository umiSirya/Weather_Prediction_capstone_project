# UV Monitor & Sunscreen Guide
# <h2> Project Overview </h2>
In an age where sun safety is paramount, this project aims to provide individuals with accurate and timely predictions of UV index levels based on their country. Utilizing advanced machine learning algorithms, this project analyzes real-time weather data to forecast UV index levels. Additionally, it offers personalized sunscreen recommendations to ensure optimal skin protection.

By seamlessly integrating data from weather APIs and predictive modeling, UV Predictor & SPF Guide empowers users to make informed decisions about sun exposure and skin care, enhancing public health and awareness.


# <h2> Problem Statement </h2>
Excessive exposure to ultraviolet (UV) radiation is a significant public health concern, leading to increased risks of skin cancer, sunburns, and other harmful effects on human health. While UV radiation levels fluctuate based on location, time of day, and weather conditions, many individuals lack the awareness and tools to effectively manage their sun exposure. This gap in knowledge and accessibility results in preventable health issues and decreased quality of life.

The project addresses this issue by providing accurate, UV index predictions and personalized sunscreen recommendations. By leveraging historical weather data and advanced machine learning algorithms, the project empowers users to make informed decisions about their sun exposure and skin protection, ultimately promoting healthier lifestyles and reducing the risk of UV-related health problems.

# <h2> Data Overview</h2>
The weather data used in this project is from: https://woudc.org/data/explore.php?lang=en. 
It contains comprehensive real-time weather information, and the target variable is the UV index. 
The data includes the following columns:

1. Y: Latitude (in decimal degrees).
2. X: Longitude (in decimal degrees).
3. uv_index_hourly_average: The hourly average UV index measurement.
4. url: A link providing more details about the observation.
5. dataset: Identifier for the dataset source.
6. instance_datetime: Timestamp when the measurement was taken.
7. platform_id: Unique ID for the measuring station.
8. platform_name: Name of the station or platform.
9. country: Country where the measurement was recorded.
10. gaw_id: Global Atmosphere Watch identifier for the station.
11. instrument_name: Name of the instrument used to measure UV.
12. instrument_model: Model designation of the instrument.
13. instrument_number: Numeric identifier for the instrument.
14. uv_index_qa: Quality assurance flag for the UV index measurement.
15. instance_hour: The hour (0–23) when the observation was made.
16. platform_type: Type of station (e.g., fixed, mobile).
17. data_payload_id: Unique identifier for the data submission batch.
18. latest_observation: Flag indicating if it’s the most recent observation.
19. uv_index_daily_max: The maximum UV index recorded during the day.
20. agency: Organization responsible for collecting or verifying the data.

<h2>Exploratory Data analysis</h2>
<strong>Note</strong><br>
I dropped all the other columns in the dataset and decided to work with only the <strong>uv_index_daily_max and the date</strong> because it represents the highest UV exposure level for the day, making it the most relevant feature for my analysis. Since my goal is to predict the UV index and recommend appropriate sunscreen based on the peak exposure, keeping additional variables that do not directly contribute to this prediction would add unnecessary complexity. By focusing solely on <strong>uv_index_daily_max</strong>, I can streamline the modeling process, reduce noise in the data, and improve the efficiency and interpretability of my machine-learning model.<br>
<strong>UV Index Statistics</strong><br>
<img width="140" alt="Image" src="https://github.com/user-attachments/assets/0338001d-6843-4a03-874c-94656012d1c6" /><br>
<br>
This summary suggests that most UV index values are relatively low, with a maximum of 3.44, which is moderate to low UV exposure.

<br>
<strong>Distribution plot for uv_index_daily_max:</strong> Visualize how values are distributed across numeric columns revealing skewness and the presence of outliers.<br> 

![Image](https://github.com/user-attachments/assets/65669800-ca5b-4048-977f-f9eaf8cd8a0e)

# <h2>Data Analysis</h2>
![Image](https://github.com/user-attachments/assets/264d2d93-f429-4ab5-91e4-3ff6b9717607)
<br>
<strong>Seasonal Pattern</strong> – The UV index follows a cyclical pattern, with peaks occurring approximately once per year. This suggests that UV radiation levels are higher during specific seasons, likely summer.

<strong>Yearly Trends</strong> – Each year exhibits similar trends: the UV index increases during warmer months and decreases in colder months.

<strong>Fluctuations</strong> – There are noticeable spikes and variations in the UV index, indicating short-term changes, possibly due to weather conditions, atmospheric changes, or measurement anomalies.

<strong>General Stability</strong> – Despite fluctuations, the overall pattern remains consistent, implying that UV index levels generally follow predictable seasonal cycles.


# <h2>Data Pre-Processing</h2>
To prepare the dataset for analysis and model training, the following preprocessing steps were performed:

<strong>Feature Scalling:</strong> Since the UV Index was not normally distributed, I applied the Min-Max Scaler to normalize the data. This transformed the 
          values into a range between 0 and 1, ensuring the model could better learn from the data.
<strong>Data Splitting</strong>
Chronological Order:
Data is sorted by date to preserve temporal relationships.

80/20 Split:

  Training Set (80%): Earliest data for model learning.

  Test Set (20%): Most recent data for evaluation.
# <h2>Model Development</h2>
My approach involves testing and comparing several types of models to determine the best fit for cryptocurrency price prediction:

<ul>
<li>Time Series Models:</li> ARIMA, SARIMA & Prophet
                       Model trends, seasonality, and cyclical patterns in the data.
<li>Deep Learning Models:</li> Long Short Term Memory (LSTM)
                         Leverage recurrent neural networks to capture long-term dependencies in sequential data.
</ul>
# <h2>Final Stage - Deploying UV Monitor & Sunscreen Guide</h3>
The last phase of my project involves deploying the UV Predictor & SPF Guide using Streamlit to create an interactive and user-friendly interface. Streamlit will enable users to input their city(City in Kenya) and receive real-time UV index predictions along with personalized sunscreen recommendations. By leveraging this platform, I aim to enhance accessibility and ensure users can make informed decisions about their sun protection with ease.

# <h2>Stakeholders</h2>
The stakeholders for such a real world project would be:-
<br>
1. <strong>Healthcare Providers:</strong> Dermatologists and general practitioners who could use the information to advise their patients on sun safety.
2. <strong>Consumers:</strong> Individuals who want to protect their skin from UV damage and are looking for personalized sunscreen recommendations.
3. <strong>Sunscreen Manufacturers:</strong> Companies that produce sunscreen products and could use the data to market their products more effectively.
