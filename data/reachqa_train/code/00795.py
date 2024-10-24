import numpy as np
import matplotlib.pyplot as plt

# Define the years
years = np.arange(2013, 2024)

# Popularity data for each color (as percentage values of use in fashion)
red_popularity = np.array([20, 19, 18, 22, 25, 27, 30, 28, 26, 29, 31])
blue_popularity = np.array([25, 23, 22, 24, 27, 28, 30, 32, 35, 36, 37])
green_popularity = np.array([18, 20, 19, 18, 20, 21, 19, 20, 21, 23, 25])
yellow_popularity = np.array([15, 16, 18, 20, 19, 18, 16, 17, 18, 19, 20])
purple_popularity = np.array([22, 22, 23, 20, 19, 17, 18, 19, 20, 18, 17])

# Error data (representing the uncertainty or variability in popularity prediction)
red_error = np.array([2, 1.5, 2.5, 2, 1.8, 2.2, 1.7, 2.3, 2.0, 2.4, 2.1])
blue_error = np.array([1.2, 1.0, 1.5, 1.4, 1.6, 1.3, 1.5, 1.7, 1.8, 1.9, 2.0])
green_error = np.array([1.5, 1.6, 1.4, 1.3, 1.7, 1.9, 1.8, 1.6, 1.7, 1.5, 1.8])
yellow_error = np.array([1.0, 1.2, 1.1, 1.3, 1.5, 1.2, 1.1, 1.4, 1.3, 1.1, 1.5])
purple_error = np.array([1.3, 1.2, 1.5, 1.6, 1.4, 1.3, 1.2, 1.5, 1.6, 1.4, 1.3])

# Plotting
plt.figure(figsize=(14, 8))

# Plot each line with error bars
plt.errorbar(years, red_popularity, yerr=red_error, label='Red', fmt='-o', color='red', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, blue_popularity, yerr=blue_error, label='Blue', fmt='-o', color='blue', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, green_popularity, yerr=green_error, label='Green', fmt='-o', color='green', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, yellow_popularity, yerr=yellow_error, label='Yellow', fmt='-o', color='gold', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, purple_popularity, yerr=purple_error, label='Purple', fmt='-o', color='purple', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)

# Customize the plot
plt.title("Fashion Trends Over Time:\nA Decade of Color Popularity", fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Color Popularity (%)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 41, 5))
plt.ylim(10, 40)  # Ensure all data points and errors are visible
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Colors", loc='upper left', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()