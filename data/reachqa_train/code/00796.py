import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Extended years
years = np.arange(2013, 2034)

# Extended popularity data for each color (as percentage values of use in fashion)
red_popularity = np.array([20, 19, 18, 22, 25, 27, 30, 28, 26, 29, 31, 33, 34, 36, 35, 37, 38, 39, 40, 42, 44])
blue_popularity = np.array([25, 23, 22, 24, 27, 28, 30, 32, 35, 36, 37, 39, 41, 42, 43, 45, 46, 47, 48, 49, 50])
green_popularity = np.array([18, 20, 19, 18, 20, 21, 19, 20, 21, 23, 25, 26, 28, 30, 32, 31, 33, 35, 36, 38, 40])
yellow_popularity = np.array([15, 16, 18, 20, 19, 18, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 26, 28, 30, 31, 33])
purple_popularity = np.array([22, 22, 23, 20, 19, 17, 18, 19, 20, 18, 17, 18, 19, 21, 22, 23, 24, 23, 25, 26, 27])
orange_popularity = np.array([10, 12, 13, 14, 15, 16, 18, 19, 18, 17, 19, 20, 22, 24, 23, 25, 26, 28, 29, 31, 32])

# Extended error data
red_error = np.array([2, 1.5, 2.5, 2, 1.8, 2.2, 1.7, 2.3, 2.0, 2.4, 2.1, 2.3, 2.2, 2.5, 2.6, 2.4, 2.7, 2.9, 3.0, 3.1, 3.2])
blue_error = np.array([1.2, 1.0, 1.5, 1.4, 1.6, 1.3, 1.5, 1.7, 1.8, 1.9, 2.0, 2.1, 2.3, 2.5, 2.4, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1])
green_error = np.array([1.5, 1.6, 1.4, 1.3, 1.7, 1.9, 1.8, 1.6, 1.7, 1.5, 1.8, 1.9, 2.0, 2.2, 2.3, 2.1, 2.4, 2.6, 2.7, 2.8, 2.9])
yellow_error = np.array([1.0, 1.2, 1.1, 1.3, 1.5, 1.2, 1.1, 1.4, 1.3, 1.1, 1.5, 1.6, 1.8, 2.0, 2.1, 2.3, 2.2, 2.5, 2.7, 2.6, 2.8])
purple_error = np.array([1.3, 1.2, 1.5, 1.6, 1.4, 1.3, 1.2, 1.5, 1.6, 1.4, 1.3, 1.4, 1.7, 1.8, 1.9, 2.0, 2.1, 2.3, 2.2, 2.5, 2.6])
orange_error = np.array([1.1, 1.3, 1.4, 1.2, 1.5, 1.7, 1.6, 1.8, 1.9, 2.0, 1.9, 2.1, 2.3, 2.4, 2.2, 2.5, 2.7, 2.8, 2.9, 3.0, 3.1])

# Polynomial fitting for trendlines
def poly_trend(x, a, b, c):
    return a*x**2 + b*x + c

year_fit = np.arange(2013, 2034, 0.1)

# Plotting
plt.figure(figsize=(16, 10))

# Plot each line with error bars
plt.errorbar(years, red_popularity, yerr=red_error, label='Red', fmt='-o', color='red', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, blue_popularity, yerr=blue_error, label='Blue', fmt='-o', color='blue', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, green_popularity, yerr=green_error, label='Green', fmt='-o', color='green', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, yellow_popularity, yerr=yellow_error, label='Yellow', fmt='-o', color='gold', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, purple_popularity, yerr=purple_error, label='Purple', fmt='-o', color='purple', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)
plt.errorbar(years, orange_popularity, yerr=orange_error, label='Orange', fmt='-o', color='orange', capsize=5, elinewidth=2, markeredgewidth=2, alpha=0.8)

# Fit and plot trendlines
colors_popularity = [red_popularity, blue_popularity, green_popularity, yellow_popularity, purple_popularity, orange_popularity]
colors_labels = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange']
colors_trendline_colors = ['darkred', 'darkblue', 'darkgreen', 'goldenrod', 'indigo', 'darkorange']

for pop_data, label, trend_color in zip(colors_popularity, colors_labels, colors_trendline_colors):
    popt, _ = curve_fit(poly_trend, years, pop_data)
    plt.plot(year_fit, poly_trend(year_fit, *popt), linestyle='--', linewidth=1.5, color=trend_color, label=f'{label} Trend')

# Customize the plot
plt.title("Fashion Trends Over Time:\nA Two-Decade Analysis of Color Popularity in Fashion", fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Color Popularity (%)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 61, 5))
plt.ylim(10, 60)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Colors", loc='upper left', fontsize=12, bbox_to_anchor=(1, 1), ncol=2)

plt.tight_layout()

plt.show()