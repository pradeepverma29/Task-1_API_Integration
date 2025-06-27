import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Replace with your own OpenWeatherMap API key
API_KEY = '5f5deb51892d64ae2d81c0f23806a7b0'
CITY = 'Jaipur'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Step 2: Fetch weather forecast data
response = requests.get(URL)
data = response.json()

# Step 3: Extract data into a dataframe
print(data)
forecast_list = data['list']
weather_data = {
    "datetime": [item['dt_txt'] for item in forecast_list],
    "temperature (°C)": [item['main']['temp'] for item in forecast_list],
    "humidity (%)": [item['main']['humidity'] for item in forecast_list],
    "wind speed (m/s)": [item['wind']['speed'] for item in forecast_list],
}
df = pd.DataFrame(weather_data)

# Step 4: Convert datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Step 5: Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='temperature (°C)', data=df, label='Temperature', marker='o')
sns.lineplot(x='datetime', y='humidity (%)', data=df, label='Humidity', marker='s')
plt.title(f'5-Day Weather Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
