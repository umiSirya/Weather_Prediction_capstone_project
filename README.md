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
1. <strong>Description of summary statistics for our numeric columns:</strong>  Provides an overview of the data by highlighting its range, spread, and potential outliers<br>
<img width="838" alt="Image" src="https://github.com/user-attachments/assets/b3330b6a-eb06-4c44-a21a-44d05d1af415" />
<br>
<br>
2.<strong>Distribution plots for the numeric columns:</strong> Visualize how values are distributed across numeric columns revealing skewness and the presence of outliers.<br> 

![Image](https://github.com/user-attachments/assets/d927b373-05bd-486e-91ac-a9417cb7e973)

3. <strong>Correlation Matrix:</strong> Explores relationships that may exist between the numeric columns and the target variable UV Index.<br>
![Image](https://github.com/user-attachments/assets/c0d66fa7-f02f-42e4-b013-3e9b622a59ea)"



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

The key insights are:
**Low UV Index:** Most cities have UV Index values ranging from 0.0 to 0.3, indicating very low UV radiation exposure in the evening.<br>
**Exception - Embu:** Embu has the highest UV Index value of 14.3, which is unusual .<br>
**Sparse Data:** Many cities do not have recorded UV Index values for the given time.<br>
This heatmap provides a clear visual representation of UV exposure levels across various locations at 7 PM, emphasizing generally low UV radiation during this time.
<br>

![Image](https://github.com/user-attachments/assets/7ae24fae-5f33-46d9-bb2d-59bf34132cea)


<br>
<h3>Weather Conditions (Distribution/ Over Time)
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
