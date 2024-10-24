import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Define the years and waste types
years = ['2010', '2012', '2014', '2016', '2018', '2020']
waste_types = ['Organic', 'Recyclable', 'Electronic', 'Hazardous']

# Data for tons of each type of waste managed over the years
waste_data = np.array([
    [320, 150, 70, 50],  # 2010
    [310, 180, 90, 60],  # 2012
    [300, 200, 110, 65], # 2014
    [290, 230, 130, 70], # 2016
    [280, 260, 160, 75], # 2018
    [270, 290, 190, 80]  # 2020
])

# Calculate percentage share for each waste type over the years
total_waste = waste_data.sum(axis=1, keepdims=True)
percentage_data = (waste_data / total_waste) * 100

# Define colors for each waste type
colors = ['#4CAF50', '#FFEB3B', '#2196F3', '#FF5722']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Stacked Bar Chart
bottom = np.zeros(len(years))
for i, (waste_type, color) in enumerate(zip(waste_types, colors)):
    ax1.bar(years, waste_data[:, i], bottom=bottom, label=waste_type, color=color, edgecolor='black', alpha=0.7)
    bottom += waste_data[:, i]

ax1.set_title('Waste Composition Trends in\nMetropolia City Council (2010-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Tons of Waste', fontsize=14)
ax1.legend(title='Waste Type', fontsize=12, title_fontsize='13')
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(range(len(years)))
ax1.set_xticklabels(years, rotation=45, ha='right', fontsize=12)

# Subplot 2: Line Chart for Percentage Share
for i, (waste_type, color) in enumerate(zip(waste_types, colors)):
    ax2.plot(years, percentage_data[:, i], marker='o', label=waste_type, color=color, linewidth=2)
    for j, value in enumerate(percentage_data[:, i]):
        ax2.text(j, value + 1, f"{value:.1f}%", ha='center', fontsize=10, color=color)

ax2.set_title('Percentage Share of Waste Types (2010-2020)', fontsize=16, weight='bold')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Percentage (%)', fontsize=14)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter())
ax2.legend(title='Waste Type', fontsize=12, title_fontsize='13')
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(range(len(years)))
ax2.set_xticklabels(years, rotation=45, ha='right', fontsize=12)

# Adjust layout
plt.tight_layout(pad=3.0)

# Show the plot
plt.show()