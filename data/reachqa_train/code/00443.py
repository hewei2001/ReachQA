import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(1980, 2021)

# Average surface temperature data (in °C)
atlantic_temps = np.array([
    15.8, 15.9, 15.9, 16.0, 16.1, 16.2, 16.2, 16.3, 16.3, 16.4, 
    16.5, 16.6, 16.6, 16.7, 16.7, 16.8, 16.9, 17.0, 17.0, 17.1, 
    17.2, 17.2, 17.3, 17.4, 17.5, 17.5, 17.6, 17.7, 17.8, 17.8, 
    17.9, 18.0, 18.1, 18.2, 18.2, 18.3, 18.4, 18.5, 18.5, 18.6, 
    18.7
])

pacific_temps = np.array([
    20.1, 20.1, 20.2, 20.3, 20.4, 20.4, 20.5, 20.6, 20.7, 20.7, 
    20.8, 20.9, 21.0, 21.1, 21.1, 21.2, 21.3, 21.4, 21.4, 21.5, 
    21.6, 21.7, 21.7, 21.8, 21.9, 22.0, 22.0, 22.1, 22.2, 22.3, 
    22.3, 22.4, 22.5, 22.6, 22.6, 22.7, 22.8, 22.9, 23.0, 23.0, 
    23.1
])

indian_temps = np.array([
    24.5, 24.5, 24.6, 24.7, 24.7, 24.8, 24.9, 25.0, 25.0, 25.1, 
    25.2, 25.3, 25.3, 25.4, 25.5, 25.6, 25.6, 25.7, 25.8, 25.9, 
    25.9, 26.0, 26.1, 26.2, 26.3, 26.3, 26.4, 26.5, 26.6, 26.6, 
    26.7, 26.8, 26.9, 27.0, 27.0, 27.1, 27.2, 27.3, 27.4, 27.4, 
    27.5
])

# Create the plot
plt.figure(figsize=(12, 6))

# Plot lines for each ocean
plt.plot(years, atlantic_temps, label="Atlantic Ocean", color='blue', linestyle='-', marker='o', linewidth=2)
plt.plot(years, pacific_temps, label="Pacific Ocean", color='green', linestyle='-', marker='s', linewidth=2)
plt.plot(years, indian_temps, label="Indian Ocean", color='red', linestyle='-', marker='^', linewidth=2)

# Set chart title and labels
plt.title("Ocean Temperature Trends:\nAverage Annual Surface Temperature (1980-2020)", fontsize=16, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Temperature (°C)", fontsize=12)

# Add legend and grid
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)

# Configure x-axis tick marks
plt.xticks(np.arange(1980, 2021, 5))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()