import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Define the months
months = np.array([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

# Extend AQI data for additional futuristic cities
cities = {
    "EcoVille": np.array([50, 45, 40, 35, 30, 32, 31, 30, 28, 30, 35, 40]),
    "Greenopolis": np.array([60, 55, 50, 45, 40, 42, 38, 35, 37, 40, 45, 50]),
    "SustainCity": np.array([55, 50, 45, 40, 35, 37, 36, 34, 32, 34, 38, 42]),
    "Futuretown": np.array([65, 62, 60, 55, 50, 48, 46, 44, 43, 45, 50, 55])
}

# Add more environmental data (Temperature, Humidity)
temperature_data = {
    "EcoVille": np.array([15, 16, 18, 20, 24, 27, 30, 28, 25, 21, 18, 16]),
    "Greenopolis": np.array([12, 14, 17, 19, 23, 26, 29, 27, 24, 20, 17, 14]),
    "SustainCity": np.array([10, 12, 15, 18, 22, 25, 28, 26, 23, 19, 16, 13]),
    "Futuretown": np.array([8, 10, 13, 17, 21, 24, 27, 25, 22, 18, 15, 11])
}

humidity_data = {
    "EcoVille": np.array([70, 68, 65, 60, 58, 57, 55, 56, 59, 62, 65, 68]),
    "Greenopolis": np.array([72, 70, 67, 64, 61, 59, 58, 59, 62, 65, 68, 70]),
    "SustainCity": np.array([75, 73, 71, 68, 65, 63, 62, 63, 66, 69, 71, 73]),
    "Futuretown": np.array([78, 76, 74, 71, 68, 66, 64, 65, 68, 72, 74, 76])
}

# Create the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Environmental Data Trends for Sustainable Cities in 2123", fontsize=20, fontweight='bold', y=1.02)

# Plot AQI data
for city, aqi in cities.items():
    axs[0, 0].plot(months, aqi, marker='o', linewidth=2, label=city)

axs[0, 0].set_title("Air Quality Index (AQI)", fontsize=14)
axs[0, 0].set_xlabel("Months")
axs[0, 0].set_ylabel("AQI")
axs[0, 0].legend(loc='upper right')
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# Plot Temperature data
for city, temp in temperature_data.items():
    axs[0, 1].plot(months, temp, marker='s', linewidth=2, label=city)

axs[0, 1].set_title("Average Temperature (°C)", fontsize=14)
axs[0, 1].set_xlabel("Months")
axs[0, 1].set_ylabel("Temperature (°C)")
axs[0, 1].legend(loc='upper left')
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# Plot Humidity data
for city, hum in humidity_data.items():
    axs[1, 0].plot(months, hum, marker='^', linewidth=2, label=city)

axs[1, 0].set_title("Average Humidity (%)", fontsize=14)
axs[1, 0].set_xlabel("Months")
axs[1, 0].set_ylabel("Humidity (%)")
axs[1, 0].legend(loc='upper left')
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# Add trend lines for AQI
axs[1, 1].set_title("AQI Trend Lines", fontsize=14)
axs[1, 1].set_xlabel("Months")
axs[1, 1].set_ylabel("AQI Trend")

for city, aqi in cities.items():
    # Numerical representation for linear regression
    X = np.arange(len(months)).reshape(-1, 1)
    model = LinearRegression().fit(X, aqi)
    trend = model.predict(X)
    axs[1, 1].plot(months, trend, linestyle='--', linewidth=2, label=f'{city} Trend')

axs[1, 1].legend(loc='upper right')
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()