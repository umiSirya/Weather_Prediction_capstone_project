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
1. <strong>Description of summary statistics for our numeric columns:</strong>  Provides an overview of the data by highlighting its range, spread, and potential outliers<br>
<img width="838" alt="Image" src="https://github.com/user-attachments/assets/b3330b6a-eb06-4c44-a21a-44d05d1af415" />
<br>
<br>
2.<strong>Distribution plots for the numeric columns:</strong> Visualize how values are distributed across numeric columns revealing skewness and the presence of outliers.<br> 

![Image](https://github.com/user-attachments/assets/d927b373-05bd-486e-91ac-a9417cb7e973)

3. <strong>Correlation Matrix:</strong> Explores relationships that may exist between the numeric columns and the target variable UV Index.<br>
![Image](https://github.com/user-attachments/assets/c0d66fa7-f02f-42e4-b013-3e9b622a59ea)



# <h2>Visualisations</h2>
<br>
<h3> Distribution of Tomorrow's weather Condition</h3>
<br>
<strong>Sunny:</strong>This weather condition has the highest frequency, with approximately 35 occurrences. It indicates that sunny weather is the most likely condition for tomorrow.<br>
<strong>Patchy Rain Nearby:</strong>This weather condition has a moderate frequency, with around 10 occurrences. It suggests that there will be some areas experiencing patchy rain.<br>
<strong>Partly Cloudy:</strong> This weather condition has the lowest frequency, with approximately 5 occurrences. It indicates that partly cloudy conditions are less common compared to sunny and patchy rain nearby.
<br>
<br>

![Image](https://github.com/user-attachments/assets/8a92c8e8-d0ae-463f-92fa-30adffd4927c)
<br>
<h3>Temperatures across cities in Kenya</h3>

**Lodwar** has the highest average temperature, above 35°C.<br>
**Garissa** and **Wajir** follow with temperatures above 35°C.<br>
**Taita** has the lowest average temperature, below 15°C.<br>

![Image](https://github.com/user-attachments/assets/0cbb0acf-d3b7-48c6-8659-d91df4085abd)

<br>
<h3>Propotions of Different Pollutants</h3>

Carbon Monoxide (CO) dominates, making up 89.7% of the total pollutants. PM10 and PM2.5 contribute 5.4% and 4.3%, respectively. Both Sulfur Dioxide (SO2) and Nitrogen Dioxide (NO2) are minimal, each accounting for 0.3%. This indicates that CO is the major pollutant in the given data set.

<br>

![Image](https://github.com/user-attachments/assets/93c62a16-3fda-484e-99bd-fbc5f54b9073)
<br>
The high concentration of Carbon Monoxide (CO) in Kenya's air pollution can be attributed to several factors:

1. **Motor Vehicles:** A significant source of CO in Kenya is motor vehicle emissions, especially in urban areas where traffic congestion is common.
2. **Indoor Cooking:** The use of traditional fuels and kerosene for cooking and heating in many households contributes to indoor air pollution, releasing CO.
3. **Burning of Solid Waste:** The indiscriminate burning of solid waste, including plastics and other materials, releases CO and other pollutants into the air.
4. **Industrial Activities:** Industries in urban areas also contribute to CO emissions due to the burning of fossil fuels.

These factors combined result in CO being the major pollutant in Kenya's air pollution profile. Efforts to reduce CO levels would need to address these sources, such as improving vehicle emission standards, promoting cleaner cooking technologies, and better waste management practices.


<br>
<h3>UV Index Across Various Cities</h3>

The heatmap titled "UV Index Across Various Cities" shows UV Index values for different cities at 7 PM. 

The key insights are:<br>
**Low UV Index:** Most cities have UV Index values ranging from 0.0 to 0.3, indicating very low UV radiation exposure in the evening.<br>
**Exception - Embu:** Embu has the highest UV Index value of 14.3, which is unusual .<br>
**Sparse Data:** Many cities do not have recorded UV Index values for the given time.<br>
This heatmap provides a clear visual representation of UV exposure levels across various locations at 7 PM, emphasizing generally low UV radiation during this time.
<br>

![Image](https://github.com/user-attachments/assets/7ae24fae-5f33-46d9-bb2d-59bf34132cea)


<br>
The heatmap titled "UV Index Across Various Cities" shows UV Index values for different cities at 3:30PM. 

1. **Highest UV Index:** Homa Bay, Kisumu, and Nakuru have consistently high UV Index values between 9.0 to 9.4.
2. **Lowest UV Index:** The lowest UV Index recorded is 0.0 at Thika.
3. **Moderate UV Index:** Embu has a UV Index of 5.3, which is moderate.
4. **Very High UV Exposure:** Several cities have UV Index values above 8.0, indicating very high UV exposure.

I've noticed an intriguing pattern in Embu's UV Index readings. During the day, the UV Index tends to be relatively low, which is unexpected considering daytime UV levels are usually higher. Surprisingly, at night, the UV Index spikes to a remarkably high value of 14.3. This anomaly suggests that atmospheric conditions in Embu might be affecting UV radiation levels in unusual ways, and it's worth investigating further to understand the underlying causes. Whether it's cloud cover, air quality, or other environmental factors, something unique is at play here.

<br>

![Image](https://github.com/user-attachments/assets/c84ec5b3-2e15-4d4d-9e56-3effa35c7f29)

<br>

<h3>Weather Conditions (Distribution/ Over Time)</h3>
<strong>Weather Conditions Distribution:</strong> The majority of weather conditions are partly cloudy (59.5%), followed by sunny (31.0%). Patchy rain nearby and moderate rain at times are both less frequent at 2.4%.

**Weather Conditions Over Time:** Sunny weather is consistently recorded, with partly cloudy conditions appearing frequently. Patchy rain and moderate rain appear less frequently, typically around specific time intervals.

These charts highlight the dominance of partly cloudy and sunny conditions, with occasional rain events during specific times.

![Image](https://github.com/user-attachments/assets/7c69a5cb-ac79-4949-832d-40c93cbd2dae)
<br>


# <h2>Data PreProcessing</h2>
1. **Dropped Columns:** We dropped several columns that were deemed unnecessary for our analysis. These columns included 'Country', 'Local Time', 'Visibility (km)', 'Weather Condition', 'Tomorrow's Condition', 'Wind Direction', 'Longitude', and 'Latitude'. This was done to reduce the complexity of the dataset and focus on the most relevant features.

2. **Sunrise and Sunset Conversion:** The 'Sunrise' and 'Sunset' columns, initially represented in time format, were converted to numerical features. Specifically, we calculated the minutes since midnight for both 'Sunrise' and 'Sunset' times. This transformation allows for easier integration into machine learning models.

3. **Encoding:** Label encoding was used for the 'City' column, which contains categorical data representing different cities.

4. **Feature Scaling:** Standard Scaling was applied to all features except the 'UV Index' to normalize the data. The 'UV Index' was also standardized to ensure consistency in the data scaling process.

5. <strong>Data Splitting:</strong>I divided the dataset into three parts to ensure robust model performance: 70% for training, 15% for validation, and 15% for testing. This approach helps in training the model effectively, fine-tuning it, and evaluating its performance on unseen data.

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
