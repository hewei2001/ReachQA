import matplotlib.pyplot as plt
import numpy as np

# Data: Average home prices in thousands of dollars for various cities and property types
cities = ['New York City', 'San Francisco', 'Chicago', 'Miami', 'Seattle', 'Los Angeles', 'Austin', 'Boston', 'Washington D.C.']

# Home prices (in thousands) for different types of homes
home_prices = {
    'New York City': [700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800],
    'San Francisco': [900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],
    'Chicago': [200, 220, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],
    'Miami': [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300],
    'Seattle': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400],
    'Los Angeles': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550],
    'Austin': [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
    'Boston': [600, 650, 700, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400],
    'Washington D.C.': [750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300]
}

# Prepare data for the boxplot
data_to_plot = [home_prices[city] for city in cities]

# Create a horizontal box plot
plt.figure(figsize=(14, 8))
box = plt.boxplot(data_to_plot, vert=False, patch_artist=True, notch=True, whis=1.5)

# Set title and labels
plt.title('Housing Affordability: Average Home Prices in Major Cities\n(in thousands of dollars)', fontsize=16, fontweight='bold')
plt.xlabel('Home Prices ($1000s)', fontsize=12)
plt.yticks(ticks=np.arange(1, len(cities) + 1), labels=cities, fontsize=10)

# Customize box colors
colors = ['#FF9999', '#FFCC99', '#99FF99', '#CCFFFF', '#9999FF', '#FFD700', '#FF69B4', '#87CEFA', '#FFB6C1']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize median lines and whiskers
for median in box['medians']:
    median.set(color='black', linewidth=2)
for whisker in box['whiskers']:
    whisker.set(color='darkgray', linewidth=1.5)

# Adding grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Add annotations for significant data points (outliers, etc.)
for i, city in enumerate(cities):
    for j in range(len(data_to_plot[i])):
        if data_to_plot[i][j] > np.percentile(data_to_plot[i], 75) + 1.5 * (np.percentile(data_to_plot[i], 75) - np.percentile(data_to_plot[i], 25)):
            plt.annotate('Outlier', xy=(data_to_plot[i][j], i + 1), xytext=(data_to_plot[i][j] + 10, i + 0.2),
                         arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show plot
plt.show()