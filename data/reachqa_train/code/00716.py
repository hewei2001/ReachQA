import matplotlib.pyplot as plt
import numpy as np

# Years from 2012 to 2022
years = np.arange(2012, 2023)

# Sales data (in thousands) for different regions
north_america = np.array([5, 8, 12, 18, 27, 39, 55, 68, 80, 93, 110])
europe = np.array([7, 11, 18, 25, 33, 50, 65, 80, 95, 115, 130])
asia_pacific = np.array([10, 15, 25, 35, 50, 75, 100, 130, 170, 210, 250])
rest_of_world = np.array([3, 5, 7, 10, 15, 20, 28, 40, 52, 65, 80])

# Stack the data for the area chart
sales_data = np.vstack([north_america, europe, asia_pacific, rest_of_world])

# Set up the plot
plt.figure(figsize=(14, 8))

# Plotting the area chart (stacked)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
plt.stackplot(years, sales_data, labels=['North America', 'Europe', 'Asia-Pacific', 'Rest of the World'], 
              colors=colors, alpha=0.8)

# Overlay trend lines
for region, color in zip(sales_data, colors):
    plt.plot(years, region, color=color, linewidth=1.5, linestyle='--')

# Customize the plot
plt.title("Decade of Electric Vehicle Growth (2012-2022)\nEV Sales Across Major Regions", fontsize=18, fontweight='bold', pad=30)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of EVs Sold (Thousands)", fontsize=14)

# Add grid lines
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 601, 100))

# Highlight the peak for each region
peak_years = [2012 + np.argmax(region) for region in sales_data]
peak_values = [max(region) for region in sales_data]

for year, value, label, color in zip(peak_years, peak_values, ['North America', 'Europe', 'Asia-Pacific', 'Rest of the World'], colors):
    plt.annotate(f'{value}k', xy=(year, value), xytext=(3, 10),
                 textcoords='offset points', fontsize=10,
                 arrowprops=dict(facecolor=color, shrink=0.05),
                 bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

# Custom legend with region names and colors
custom_legend = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(custom_legend, ['North America', 'Europe', 'Asia-Pacific', 'Rest of the World'], loc='upper left', fontsize=10, title="Regions")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()