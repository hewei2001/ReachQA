import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
cities = ["Greensville", "Metropolita", "Ecopolis", "Floraltown", "Verdancia"]
park_acres = np.array([450, 620, 380, 470, 520])
community_garden_acres = np.array([50, 80, 45, 70, 60])
urban_forest_acres = np.array([300, 500, 250, 400, 350])
rooftop_garden_acres = np.array([30, 55, 25, 60, 50])
wetland_acres = np.array([120, 200, 150, 170, 180])

# Data for the line chart (percentage increase over a decade)
percentage_increase = np.array([15, 25, 10, 20, 18])

# Set positions for the groups of bars on the x-axis
x = np.arange(len(cities))
bar_width = 0.15

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Bar chart in the first subplot
ax1.bar(x - 2*bar_width, park_acres, bar_width, label='Parks', color='#8dd3c7')
ax1.bar(x - bar_width, community_garden_acres, bar_width, label='Community Gardens', color='#ffffb3')
ax1.bar(x, urban_forest_acres, bar_width, label='Urban Forests', color='#bebada')
ax1.bar(x + bar_width, rooftop_garden_acres, bar_width, label='Rooftop Gardens', color='#fb8072')
ax1.bar(x + 2*bar_width, wetland_acres, bar_width, label='Wetlands', color='#80b1d3')

# Annotate the bars with values
for idx, city in enumerate(x):
    ax1.text(city - 2*bar_width, park_acres[idx] + 10, park_acres[idx], ha='center', va='bottom', fontsize=9)
    ax1.text(city - bar_width, community_garden_acres[idx] + 10, community_garden_acres[idx], ha='center', va='bottom', fontsize=9)
    ax1.text(city, urban_forest_acres[idx] + 10, urban_forest_acres[idx], ha='center', va='bottom', fontsize=9)
    ax1.text(city + bar_width, rooftop_garden_acres[idx] + 10, rooftop_garden_acres[idx], ha='center', va='bottom', fontsize=9)
    ax1.text(city + 2*bar_width, wetland_acres[idx] + 10, wetland_acres[idx], ha='center', va='bottom', fontsize=9)

# Bar chart customization
ax1.set_title("Distribution of Green Space Types\nin Major Metropolitan Cities - 2023", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Cities", fontsize=12)
ax1.set_ylabel("Green Space Area (Acres)", fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontsize=11)
ax1.legend(title="Green Space Types", fontsize=10, title_fontsize='13')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('#f7f7f7')

# Line chart in the second subplot
ax2.plot(cities, percentage_increase, marker='o', color='#ff7f00', linewidth=2, markersize=8)
ax2.set_title("Percentage Increase of Green Space\nAcreage Over the Past Decade", fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel("Cities", fontsize=12)
ax2.set_ylabel("Increase (%)", fontsize=12)
ax2.set_ylim(0, 30)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_facecolor('#f7f7f7')

# Annotate the line chart with values
for i, value in enumerate(percentage_increase):
    ax2.text(cities[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()