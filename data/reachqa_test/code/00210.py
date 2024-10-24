import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data: Number of bird sightings in a city park (January to December)
months = np.arange(1, 13)
bird_sightings = np.array([20, 28, 35, 50, 70, 85, 95, 88, 65, 45, 30, 22])

# Additional data: Average temperature (in Celsius) for each month in the same park
average_temp = np.array([-1, 0, 5, 10, 15, 20, 22, 21, 17, 10, 5, 0])

# Define a quadratic function for fitting
def seasonal_trend(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the data to the quadratic trend
params, _ = curve_fit(seasonal_trend, months, bird_sightings)

# Generate a smooth line for the fitted curve
x_smooth = np.linspace(1, 12, 100)
y_smooth = seasonal_trend(x_smooth, *params)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("Urban Bird Sightings and Seasonal Influences", fontsize=18, fontweight='bold')

# First subplot: Bird sightings with a fitted curve
axs[0].scatter(months, bird_sightings, color='sienna', edgecolor='black', s=100, alpha=0.8, label='Bird Sightings')
axs[0].plot(x_smooth, y_smooth, color='darkorange', linestyle='-', linewidth=2, label='Migration Trend')
axs[0].set_title("Monthly Bird Sightings and Migration Trend", fontsize=14)
axs[0].set_xlabel("Month", fontsize=12)
axs[0].set_ylabel("Number of Sightings", fontsize=12)
axs[0].set_xticks(months)
axs[0].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
axs[0].set_xlim(1, 12)
axs[0].set_ylim(0, 100)
axs[0].legend(loc='upper left', fontsize=10)
axs[0].grid(alpha=0.3)

# Annotate the peak migration month
peak_month = months[np.argmax(bird_sightings)]
peak_sightings = np.max(bird_sightings)
axs[0].annotate('Peak Migration', xy=(peak_month, peak_sightings), xytext=(peak_month-1.5, peak_sightings+10),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
                fontsize=11, color='black')

# Second subplot: Bar chart of average temperatures
axs[1].bar(months, average_temp, color='skyblue', alpha=0.7, edgecolor='black')
axs[1].set_title("Average Monthly Temperature", fontsize=14)
axs[1].set_xlabel("Month", fontsize=12)
axs[1].set_ylabel("Temperature (°C)", fontsize=12)
axs[1].set_xticks(months)
axs[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
axs[1].set_xlim(0.5, 12.5)
axs[1].axhline(0, color='gray', linewidth=0.8)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()