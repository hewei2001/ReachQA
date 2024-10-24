import numpy as np
import matplotlib.pyplot as plt

# Define the years for the chart
years = np.arange(2010, 2021)

# Data representing the percentage contribution of each energy source
solar_power = np.array([1, 2, 3, 5, 7, 10, 12, 14, 18, 22, 25])
wind_power = np.array([3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 22])
hydro_power = np.array([15, 15, 16, 16, 17, 18, 19, 20, 21, 22, 22])

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plotting the stacked area chart
plt.stackplot(years, solar_power, wind_power, hydro_power,
              labels=['Solar Power', 'Wind Power', 'Hydroelectric Power'],
              colors=['#FDB813', '#00A4E4', '#4CAF50'], alpha=0.8)

# Adding title and labels
plt.title('Rising Green: A Decade of Renewable Energy Growth\nin Global Electricity Production (2010-2020)',
          fontsize=16, fontweight='bold', color='darkgreen')
plt.xlabel('Year', fontsize=12, color='navy')
plt.ylabel('Percentage of Total Electricity Production', fontsize=12, color='navy')

# Configure x-ticks for better readability
plt.xticks(years, rotation=45)

# Adding a grid for better readability
plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotations for specific points
plt.annotate('Rise of Solar', xy=(2018, 18), xytext=(2015, 30),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='orange', horizontalalignment='right')

plt.annotate('Wind Power Peaks', xy=(2020, 19), xytext=(2017, 35),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='blue', horizontalalignment='right')

# Add a legend and position it outside the plot to prevent occlusion
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout for better fit and visibility
plt.tight_layout()

# Show the plot
plt.show()