# Weather Dataset Analysis using NumPy and Pandas
# Author: Shreyash Shahaji Patil
# Roll No: CM-86 | Division: CM | Batch: CM4
# Activity No: 1

import pandas as pd
import numpy as np

# Assuming the dataset is loaded as 'weather.csv'
df = pd.read_csv('weather.csv', parse_dates=['Date'])

# 1. Find the average temperature for the entire dataset.
avg_temp = df['Temperature'].mean()

# 2. Find the maximum humidity recorded.
max_humidity = df['Humidity'].max()

# 3. Count the number of rainy days.
rainy_days = df[df['Rainfall'] > 0].shape[0]

# 4. Extract all records where wind speed was above 20 km/h.
high_wind = df[df['Wind Speed'] > 20]

# 5. Plot monthly average temperatures.
monthly_avg_temp = df.groupby(df['Date'].dt.month)['Temperature'].mean()

# 6. Find the day with the lowest temperature.
coldest_day = df[df['Temperature'] == df['Temperature'].min()]

# 7. Calculate the standard deviation of temperature.
temp_std = df['Temperature'].std()

# 8. How many days had zero rainfall?
dry_days = df[df['Rainfall'] == 0].shape[0]

# 9. Categorize temperature as Cold (<15), Moderate (15-25), or Hot (>25).
df['Temp_Category'] = np.where(df['Temperature'] < 15, 'Cold', np.where(df['Temperature'] <= 25, 'Moderate', 'Hot'))

# 10. Find the correlation between Temperature and Humidity.
correlation = df[['Temperature', 'Humidity']].corr()

# 11. Replace missing values in Humidity column with the column mean.
df['Humidity'].fillna(df['Humidity'].mean(), inplace=True)

# 12. Check if there is any missing data in the dataset.
missing_data = df.isnull().sum()

# 13. Find average wind speed during rainy days.
avg_wind_rain = df[df['Rainfall'] > 0]['Wind Speed'].mean()

# 14. Create a column that shows temperature in Fahrenheit.
df['Temp_F'] = df['Temperature'] * 9/5 + 32

# 15. Calculate cumulative rainfall over the dataset.
df['Cumulative_Rainfall'] = df['Rainfall'].cumsum()

# 16. Filter all weekends from the dataset.
weekends = df[df['Date'].dt.dayofweek >= 5]

# 17. Count days where Temp > 30, Humidity < 50, Wind Speed > 10.
hot_dry_windy_days = df[(df['Temperature'] > 30) & (df['Humidity'] < 50) & (df['Wind Speed'] > 10)].shape[0]

# 18. Find average monthly humidity.
monthly_avg_humidity = df.groupby(df['Date'].dt.month)['Humidity'].mean()

# 19. Plot a histogram of temperature distribution.
# df['Temperature'].hist()  # Uncomment to plot if using Jupyter or IDE

# 20. Find the longest stretch of consecutive dry days (Rainfall = 0).
df['Dry'] = (df['Rainfall'] == 0).astype(int)
df['Dry_Group'] = df['Dry'].diff().ne(0).cumsum()
longest_dry_streak = df[df['Dry'] == 1].groupby('Dry_Group').size().max()