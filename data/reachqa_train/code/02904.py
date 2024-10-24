import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2020)

# Average yearly AQI data for each city
aqi_data = {
    'New York': np.array([50, 52, 48, 49, 51, 50, 47, 48, 46, 45]),
    'Beijing': np.array([110, 108, 115, 120, 118, 125, 130, 135, 129, 126]),
    'Paris': np.array([45, 44, 43, 42, 41, 40, 39, 38, 37, 36]),
    'New Delhi': np.array([140, 142, 145, 148, 152, 150, 155, 158, 160, 165])
}

# Standard deviation of AQI data for each city
aqi_variability = {
    'New York': np.array([5, 4, 5, 6, 5, 4, 3, 4, 3, 3]),
    'Beijing': np.array([10, 12, 15, 13, 14, 15, 16, 17, 16, 14]),
    'Paris': np.array([3, 3, 4, 3, 2, 3, 2, 2, 2, 1]),
    'New Delhi': np.array([15, 14, 13, 12, 11, 10, 11, 12, 14, 16])
}

# Create a plot
plt.figure(figsize=(12, 8))

# Iterate over each city and plot the data
for city, aqi in aqi_data.items():
    plt.errorbar(years, aqi, yerr=aqi_variability[city], label=city, fmt='-o', capsize=5, alpha=0.8)

# Set titles and labels
plt.title("Decade of Air Quality Trends in Global Cities\nConsistency and Variability", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Yearly AQI', fontsize=12)
plt.xticks(years)

# Add a legend
plt.legend(title='Cities', fontsize=10, loc='upper right')

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()