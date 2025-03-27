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



# <h2>Data Pre-Processing</h2>

# <h2>Training the Model</h2>
I went with <strong>The LSTM (Long Short-Term Memory) model</strong> to predict the UV index is an excellent choice due to its ability to handle sequential and time-series data effectively. 
Here's why:

**Ability to Capture Temporal Patterns:** UV index data is inherently time-dependent, and LSTM models excel at capturing temporal patterns and dependencies in sequential data.

**Handling Long-Term Dependencies:** LSTMs are designed to remember long-term dependencies, which is crucial for accurate UV index predictions, as past UV patterns can significantly influence future values.

**Robustness to Noise and Variability:** The UV index can exhibit high variability due to factors like weather conditions and geographical changes. LSTMs are robust to such noise and can learn the underlying trends effectively.

**Better Performance:** LSTMs often outperform traditional models in time-series forecasting tasks, leading to more accurate and reliable UV index predictions.

<h3> Evaluation Metrics</h3>
To evaluate the performance of my model, I use the Mean Squared Error (MSE) metric. MSE measures the average squared difference between the actual and predicted values, providing a clear indication of the model's accuracy. By minimizing the MSE, I aim to enhance the model's predictive capabilities and ensure robust performance.
<br>
<img width="220" alt="Image" src="https://github.com/user-attachments/assets/36b91218-c768-4e0f-b474-ce561cec8f7d" />
<br>

# <h2>Final Stage - Deploying UV Monitor & Sunscreen Guide</h3>
The last phase of my project involves deploying the UV Predictor & SPF Guide using Streamlit to create an interactive and user-friendly interface. Streamlit will enable users to input their city(City in Kenya) and receive real-time UV index predictions along with personalized sunscreen recommendations. By leveraging this platform, I aim to enhance accessibility and ensure users can make informed decisions about their sun protection with ease.

# <h2>Stakeholders</h2>
The stakeholders for such a real world project would be:-
<br>
1. <strong>Healthcare Providers:</strong> Dermatologists and general practitioners who could use the information to advise their patients on sun safety.
2. <strong>Consumers:</strong> Individuals who want to protect their skin from UV damage and are looking for personalized sunscreen recommendations.
3. <strong>Sunscreen Manufacturers:</strong> Companies that produce sunscreen products and could use the data to market their products more effectively.
