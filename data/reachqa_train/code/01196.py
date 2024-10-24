import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the years from 2000 to 2020
years = np.arange(2000, 2021)

# Expanded data for average monthly consumption in pounds
chocolates = [50, 52, 53, 54, 57, 55, 60, 62, 61, 63, 65, 64, 66, 68, 67, 66, 70, 72, 73, 74, 75]
gummies = [28, 29, 31, 32, 33, 35, 36, 38, 40, 43, 45, 48, 46, 47, 49, 51, 52, 54, 55, 57, 58]
hard_candies = [22, 21, 20, 19, 17, 18, 17, 16, 15, 14, 13, 12, 11, 12, 13, 11, 10, 9, 9, 8, 7]
lollipops = [10, 11, 12, 12, 14, 15, 16, 15, 14, 13, 15, 16, 17, 18, 19, 21, 22, 24, 26, 27, 28]

# Calculate total consumption for line plot
total_consumption = np.array(chocolates) + np.array(gummies) + np.array(hard_candies) + np.array(lollipops)

# Set up the plot
plt.figure(figsize=(14, 9))

# Define bin edges for histogram
bin_edges = np.arange(2000, 2022, 1)

# Plot stacked histogram
plt.hist(
    [years, years, years, years], 
    bins=bin_edges, 
    weights=[chocolates, gummies, hard_candies, lollipops], 
    label=['Chocolates', 'Gummies', 'Hard Candies', 'Lollipops'],
    color=['saddlebrown', 'darkorange', 'royalblue', 'limegreen'], 
    alpha=0.7, 
    edgecolor='black',
    histtype='barstacked'
)

# Add a line plot for total consumption
plt.plot(years, total_consumption, color='black', linestyle='--', marker='o', label='Total Consumption')

# Trendline for total consumption
model = LinearRegression().fit(years.reshape(-1, 1), total_consumption)
trendline = model.predict(years.reshape(-1, 1))
plt.plot(years, trendline, color='purple', linestyle='-', linewidth=2, label='Total Trendline')

# Customize the plot
plt.title(
    "A Sweeter Spectrum: \nThe Evolution of Candy Consumption \nfrom 2000 to 2020 in the United States",
    fontsize=16, 
    fontweight='bold'
)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Avg Monthly Consumption (Pounds)", fontsize=14)
plt.xticks(years, rotation=45, ha='right')
plt.yticks(range(0, 161, 20))
plt.legend(title="Candy Type", fontsize=12)

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()