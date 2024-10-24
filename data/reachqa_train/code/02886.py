import matplotlib.pyplot as plt
import numpy as np

# Data: Percentage of energy derived from renewable sources over time in different regions
years = np.arange(2010, 2021)
solaria = np.array([10, 15, 20, 30, 40, 50, 60, 65, 70, 72, 75])
windmere = np.array([5, 10, 15, 25, 35, 45, 55, 60, 68, 72, 80])
hydrovania = np.array([20, 22, 25, 27, 30, 32, 33, 35, 38, 40, 42])
geotopia = np.array([3, 5, 7, 10, 14, 18, 22, 25, 30, 35, 40])
biomassia = np.array([8, 10, 12, 20, 25, 30, 35, 38, 40, 42, 45])

# Create a figure and axis
plt.figure(figsize=(12, 7))

# Plot the data for each region
plt.plot(years, solaria, label='Solaria', marker='o', linestyle='-', linewidth=2, color='gold')
plt.plot(years, windmere, label='Windmere', marker='s', linestyle='-', linewidth=2, color='skyblue')
plt.plot(years, hydrovania, label='Hydrovania', marker='D', linestyle='-', linewidth=2, color='blue')
plt.plot(years, geotopia, label='Geotopia', marker='^', linestyle='-', linewidth=2, color='darkred')
plt.plot(years, biomassia, label='Biomassia', marker='x', linestyle='-', linewidth=2, color='green')

# Annotate significant points
annotations = {
    (2015, 50): ('Solar Breakthrough', 'gold'),
    (2018, 68): ('Wind Policy Reforms', 'skyblue'),
    (2014, 27): ('Hydro Expansion', 'blue'),
    (2019, 35): ('Geothermal Spike', 'darkred'),
    (2017, 35): ('Biomass Initiatives', 'green')
}
for (x, y), (text, color) in annotations.items():
    plt.annotate(text, xy=(x, y), xytext=(x-1, y+10),
                 arrowprops=dict(facecolor=color, shrink=0.05, edgecolor=color),
                 fontsize=9, color=color, backgroundcolor='white')

# Customize the chart
plt.title('Renewable Energy Adoption in TerraNova Regions\n(2010-2020)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Renewable Energy (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize='12')

# Automatically adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()