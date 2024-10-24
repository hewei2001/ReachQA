import numpy as np
import matplotlib.pyplot as plt

# Define the years for the analysis
years = np.arange(2010, 2021)

# Hypothetical average sea surface temperature data (in degrees Celsius)
pacific_sst = np.array([24.8, 24.9, 25.1, 25.3, 25.4, 25.6, 25.7, 25.8, 26.0, 26.1, 26.3])
atlantic_sst = np.array([22.2, 22.3, 22.4, 22.6, 22.8, 23.0, 23.2, 23.3, 23.5, 23.7, 23.8])
indian_sst = np.array([26.5, 26.6, 26.8, 26.9, 27.1, 27.3, 27.4, 27.5, 27.7, 27.8, 28.0])

# Uncertainty/error in temperature measurements (standard deviation)
pacific_error = np.array([0.3, 0.25, 0.28, 0.26, 0.24, 0.23, 0.25, 0.28, 0.27, 0.29, 0.3])
atlantic_error = np.array([0.4, 0.35, 0.34, 0.33, 0.31, 0.29, 0.32, 0.35, 0.36, 0.37, 0.39])
indian_error = np.array([0.5, 0.45, 0.43, 0.42, 0.41, 0.4, 0.39, 0.38, 0.36, 0.34, 0.33])

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plotting the line chart with error bars
plt.errorbar(years, pacific_sst, yerr=pacific_error, fmt='-o', label='Pacific Ocean', color='royalblue', capsize=5, alpha=0.8)
plt.errorbar(years, atlantic_sst, yerr=atlantic_error, fmt='-s', label='Atlantic Ocean', color='darkorange', capsize=5, alpha=0.8)
plt.errorbar(years, indian_sst, yerr=indian_error, fmt='-^', label='Indian Ocean', color='forestgreen', capsize=5, alpha=0.8)

# Adding title and labels
plt.title('Waves of Change: \nTracking Oceanic Temperature Variability (2010-2020)', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Sea Surface Temperature (°C)', fontsize=12, color='black')

# Configure x-ticks for better readability
plt.xticks(years, rotation=45)

# Adding a grid for better readability
plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend and position it outside the plot to prevent occlusion
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust the layout for better fit and visibility
plt.tight_layout()

# Show the plot
plt.show()