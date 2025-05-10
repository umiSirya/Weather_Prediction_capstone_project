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

![Image](https://github.com/user-attachments/assets/358d4ff2-f1b1-4093-9cba-f089ce677fb0)

I chose to work with data from 2000 to 2004 because, as shown in the chart, this period has a consistent and complete UV Index Daily Max trend without the gaps and irregularities seen in the later years.
<br>
![Image](https://github.com/user-attachments/assets/264d2d93-f429-4ab5-91e4-3ff6b9717607)

<br>
<strong>Seasonal Pattern</strong> – The UV index follows a cyclical pattern, with peaks occurring approximately once per year. This suggests that UV radiation levels are higher during specific seasons, likely summer.

<strong>Yearly Trends</strong> – Each year exhibits similar trends: the UV index increases during warmer months and decreases in colder months.

<strong>Fluctuations</strong> – There are noticeable spikes and variations in the UV index, indicating short-term changes, possibly due to weather conditions, atmospheric changes, or measurement anomalies.

<strong>General Stability</strong> – Despite fluctuations, the overall pattern remains consistent, implying that UV index levels generally follow predictable seasonal cycles.


# <h2>Data Pre-Processing</h2>
### Steps Performed:
1. **Datetime Conversion**: Ensured the `instance_date` column was in datetime format and set as the index.
2. **Stationarity Check**: Applied the ADF test and differencing if necessary.
3. **Train-Test Split**: Divided the data into training and testing sets, with the last 2 months reserved for testing.
4. **ACF and PACF Plots**: Used to determine the optimal ARIMA and SARIMA parameters.
   
# <h2>Model Development</h2>
My approach involves testing and comparing several types of models to determine the best fit for cryptocurrency price prediction:

<ul>
<li>Time Series Models:</li> ARIMA, SARIMA & Prophet
                       Model trends, seasonality, and cyclical patterns in the data.
<li>Deep Learning Models:</li> Long Short Term Memory (LSTM)
                         Leverage recurrent neural networks to capture long-term dependencies in sequential data.
</ul>
<h2>Time series Model</h2>
ARIMA (AutoRegressive Integrated Moving Average) and SARIMA (Seasonal ARIMA) are time series forecasting models.

ARIMA:

AR (AutoRegressive): Uses the relationship between an observation and a number of lagged observations (previous time points).

I (Integrated): Makes the series stationary by differencing (subtracting previous values).

MA (Moving Average): Models the error term as a combination of past forecast errors.

SARIMA:

Extends ARIMA by adding seasonal components to account for periodic patterns (seasonality) in data.

It includes seasonal auto-regression (SAR), seasonal differencing (SD), and seasonal moving average (SMA).
### ARIMA Model

#### Training
- The ARIMA model was trained using the order `(1, 1, 1)`:
  - `p=1`: Number of autoregressive terms.
  - `d=1`: Degree of differencing.
  - `q=1`: Number of moving average terms.

#### Forecasting
- Predictions were made on the test set and compared with actual values.

#### Visualization
- The results were plotted to compare training data, actual test data, and ARIMA predictions.
 <div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/ea524cfc-7940-44a9-8571-c02ccae10d9c" width="45%" />
  <img src="https://github.com/user-attachments/assets/2bdd241c-d659-4609-a721-b3710a6f1eb9" width="45%" />
</div>


#### Evaluation
- Metrics such as **MAE**, **MSE**, and **RMSE** were calculated to evaluate model performance.
<img width="208" alt="Image" src="https://github.com/user-attachments/assets/5a714b21-605c-48ac-b6f9-d74cb2b46e0c" />

### SARIMA Model

#### Training
- The SARIMA model extended ARIMA by adding seasonal components:
  - `order=(1, 0, 1)`: Non-seasonal ARIMA parameters.
  - `seasonal_order=(1, 0, 1, 12)`: Seasonal ARIMA parameters with a period of 12 months.

#### Forecasting
- Predictions were made on the test set and visualized alongside actual values.
  <div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/4966f1cd-7836-41e6-804b-b9901b5328da" width="45%">
  <img src="https://github.com/user-attachments/assets/c777581e-4f46-4b97-b0bc-7460d80d1fdc" width="45%">
</div>


#### Evaluation
- Similar metrics (**MAE**, **MSE**, **RMSE**) were computed to assess performance.

<img width="238" alt="Image" src="https://github.com/user-attachments/assets/a94199c8-7d93-4d71-bd32-676f134103bc" />

## Prophet Model
The <strong>Prophet model</strong> is a time series forecasting tool designed to handle data with strong <strong>seasonal effects</strong> and <strong>missing values</strong>. It works by decomposing the time series into three main components:

1. <strong>Trend</strong>: Captures long-term changes in the data over time (e.g., growth or decline).
2. <strong>Seasonality</strong>: Models periodic patterns that repeat at regular intervals (e.g., weekly or yearly cycles).
3. <strong>Holidays</strong>: Incorporates the effects of holidays or special events that can impact the data.

Prophet uses an <strong>additive</strong> or <strong>multiplicative</strong> model to combine these components and make forecasts. It automatically handles <strong>seasonality</strong>, <strong>outliers</strong>, and <strong>missing data</strong>, and it also allows users to include custom <strong>holidays</strong> and special events for more accurate predictions.

Prophet is easy to use for time series forecasting when there are clear <strong>seasonal trends</strong> and irregularities in the data.

### Prophet Configuration
- **Yearly Seasonality**: Enabled to capture annual trends.
- **Weekly/Daily Seasonality**: Disabled as they are not relevant for this dataset.
- **Seasonality Mode**: Set to `'multiplicative'` to handle varying seasonal effects.

### Training Process
1. The model was trained on the training data (`train_data`).
2. Future predictions were generated for the test period using `make_future_dataframe`.

### Visualization
- Actual UV index values were plotted alongside Prophet's predictions.
- Confidence intervals (shaded area) were added to indicate prediction uncertainty.
- 
![Image](https://github.com/user-attachments/assets/e38c4ec8-9c6d-4215-9b79-f410996487da)

## Model Evaluation

The model's performance was evaluated using the following metrics:

<img width="209" alt="Image" src="https://github.com/user-attachments/assets/ac84f34f-17c4-4008-8ffa-fbb820df8b91" />

## LSTM Model
The <strong>LSTM</strong> (Long Short-Term Memory) model is a type of <strong>Recurrent Neural Network (RNN)</strong> designed to handle <strong>sequential data</strong> and capture long-term dependencies. It is particularly effective for tasks like <strong>time series forecasting</strong>, <strong>speech recognition</strong>, and <strong>natural language processing</strong>.

LSTM overcomes the vanishing gradient problem found in traditional RNNs by using <strong>memory cells</strong> to store and retrieve information over long periods. It consists of three main gates:

1. <strong>Forget Gate</strong>: Decides what information to discard from the memory.
2. <strong>Input Gate</strong>: Controls what new information is added to the memory.
3. <strong>Output Gate</strong>: Determines what part of the memory to output.

This architecture allows LSTM to remember important information for longer durations, making it suitable for tasks involving long-range dependencies.

LSTM is a powerful model for learning patterns in sequential data, as it can effectively capture both short-term and long-term dependencies.


### LSTM Architecture
The LSTM model consists of the following layers:
1. **LSTM Layer 1**: 100 units with `return_sequences=True`.
2. **Dropout Layer**: 20% dropout to prevent overfitting.
3. **LSTM Layer 2**: 100 units with `return_sequences=False`.
4. **Dropout Layer**: 20% dropout.
5. **Dense Layer**: 50 units for feature extraction.
6. **Output Layer**: Single unit to predict the next day's UV index.

### Training Process
- **Optimizer**: Adam.
- **Loss Function**: Mean Squared Error (MSE).
- **Epochs**: 50.
- **Batch Size**: 32.

### Visualization
- Actual vs. predicted UV index values were plotted for both training and testing data.
- Confidence intervals were omitted as LSTM directly predicts values without uncertainty bounds.
- 
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/7afde328-49ac-4a21-9ff9-9d5095141adb" width="45%">
  <img src="https://github.com/user-attachments/assets/df424815-44e5-45cc-a3ce-5dcaef9ee654" width="45%">
</div>


## Model Evaluation

The model's performance was evaluated using the following metrics:
<img width="209" alt="Image" src="https://github.com/user-attachments/assets/7e4e8eb0-bdb8-48a5-8de7-3c3ef8f9f7e1" />

## Sunscreen Recommendation System
# Sunscreen Recommendation System

The sunscreen recommendation system provides personalized sunscreen suggestions based on the predicted UV index. It ensures users are adequately protected by recommending products with appropriate SPF ratings.

---

## How It Works

### 1. UV Index Categories
The system uses the following UV index categories to determine sunscreen recommendations:

| **UV Index Range** | **Category**       | **Recommended SPF** |
|--------------------|--------------------|---------------------|
| 0–2               | Low               | SPF ≤ 15           |
| 3–5               | Moderate          | 15 < SPF ≤ 30      |
| 6–7               | High              | 30 < SPF ≤ 50      |
| 8+                | Very High/Extreme | SPF > 50           |

### 2. Filtering Sunscreens
The system filters the `sunscreens.csv` dataset to find products matching the recommended SPF range for the predicted UV index.

### 3. Selecting a Recommendation
If multiple sunscreens match the criteria, the system selects the first product from the filtered list. If no match is found, it notifies the user.

---

## Example

### Input
- Predicted UV Index: `0.19`

### Process
- Category: **High UV Index (30 < SPF ≤ 50)**
- Filtered Products: Sunscreens with SPF between 30 and 50.
- Selected Product: First matching sunscreen.

### Output
<img width="298" alt="Image" src="https://github.com/user-attachments/assets/860cf596-f569-42e5-aa98-dc5217e9697b" />

# <h2>Stakeholders</h2>
The stakeholders for such a real world project would be:-
<br>
1. <strong>Healthcare Providers:</strong> Dermatologists and general practitioners who could use the information to advise their patients on sun safety.
2. <strong>Consumers:</strong> Individuals who want to protect their skin from UV damage and are looking for personalized sunscreen recommendations.
3. <strong>Sunscreen Manufacturers:</strong> Companies that produce sunscreen products and could use the data to market their products more effectively.
