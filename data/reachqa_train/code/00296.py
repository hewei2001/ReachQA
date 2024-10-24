import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2025
years = np.arange(2000, 2026)

# Coffee consumption data for different types (with increased complexity)
espresso_consumption = [15, 18, 20, 23, 27, 30, 28, 29, 32, 35, 37, 39, 42, 45, 48, 50, 52, 55, 58, 60, 62, 65, 67, 70, 72, 75]
cappuccino_consumption = [12, 15, 17, 19, 22, 25, 27, 30, 33, 30, 32, 35, 38, 40, 42, 44, 45, 47, 50, 53, 55, 58, 60, 63, 65, 67]
cold_brew_consumption = [3, 5, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 33, 35, 37, 40, 42, 45, 48, 50, 53, 55, 58, 60, 62, 65]
latte_consumption = [7, 10, 13, 16, 18, 20, 23, 25, 28, 30, 32, 35, 38, 40, 42, 44, 46, 48, 50, 52, 54, 57, 60, 62, 64, 66]

# Standard deviations for error bars (increased complexity)
espresso_std = [1.5, 2, 2, 2.5, 3, 2.5, 2, 3, 2.5, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2.5, 2, 3, 2.5, 2, 1.5, 2, 2.5, 3]
cappuccino_std = [2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2, 1.5]
cold_brew_std = [1, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2.5, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2.5, 2, 3, 2.5, 2, 1.5, 2, 2.5, 3]
latte_std = [1.5, 2, 2.5, 3, 2.5, 2, 3, 2.5, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2, 1.5, 2, 2.5, 3, 2.5, 2, 3, 2, 1.5]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each coffee type with error bars
ax.errorbar(years, espresso_consumption, yerr=espresso_std, label='Espresso',
            fmt='-o', capsize=4, linestyle='--', color='darkorange', alpha=0.7)
ax.errorbar(years, cappuccino_consumption, yerr=cappuccino_std, label='Cappuccino',
            fmt='-^', capsize=4, linestyle='-', color='teal', alpha=0.7)
ax.errorbar(years, cold_brew_consumption, yerr=cold_brew_std, label='Cold Brew',
            fmt='-s', capsize=4, linestyle='-.', color='purple', alpha=0.7)
ax.errorbar(years, latte_consumption, yerr=latte_std, label='Latte',
            fmt='-d', capsize=4, linestyle=':', color='green', alpha=0.7)

# Customize the plot
ax.set_title('Evolving Coffee Consumption Patterns Among Different Types\nAnalyzing Trends Over the Years (2000-2025)', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Monthly Consumption (Cups)', fontsize=12)
ax.set_xticks(years[::2])
ax.set_xlim(2000, 2025)
ax.set_ylim(0, 80)
ax.legend(title="Coffee Type", fontsize=10, loc='upper left')

# Enable grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a trend line for Cappuccino for demonstration
z = np.polyfit(years, cappuccino_consumption, 3)
p = np.poly1d(z)
ax.plot(years, p(years), "b--", alpha=0.5, label='Cappuccino Trend Line')

# Add annotations for significant points
ax.annotate('Cold Brew Popularity Rise', xy=(2015, 20), xytext=(2010, 40),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Adjust layout for neatness
plt.tight_layout()

# Display the plot
plt.show()