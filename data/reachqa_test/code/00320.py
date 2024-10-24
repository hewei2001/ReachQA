import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the continents and crops
continents = ['North America', 'South America', 'Europe', 'Asia', 'Africa']
crops = ['Wheat', 'Rice', 'Corn', 'Soybeans', 'Barley']

# Proportional production data (in percentages)
production_data = np.array([
    [25, 5, 40, 20, 10],   # North America
    [10, 5, 35, 45, 5],    # South America
    [30, 10, 10, 5, 45],   # Europe
    [15, 60, 10, 5, 10],   # Asia
    [20, 5, 20, 15, 40]    # Africa
])

# Normalize data to percentages
production_data = production_data / production_data.sum(axis=1)[:, np.newaxis] * 100

# Additional data for new subplot (e.g., 5-year production growth in %)
growth_data = np.array([
    [3, 2, 4, 5, 1],   # North America
    [4, 1, 3, 6, 2],   # South America
    [1, 2, 3, 1, 3],   # Europe
    [5, 3, 2, 1, 2],   # Asia
    [2, 4, 2, 3, 4]    # Africa
])

# Initialize the figure
fig = plt.figure(figsize=(18, 8))

# 3D Bar Chart for production proportions
ax1 = fig.add_subplot(121, projection='3d')
width = 0.5
depth = 0.3
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

for i, continent in enumerate(continents):
    xs = np.arange(len(crops))
    ys = np.full_like(xs, i)
    zs = np.zeros_like(xs)
    ax1.bar3d(xs, ys, zs, width, depth, production_data[i], color=colors, alpha=0.8)

ax1.set_xlabel('Crops', labelpad=15)
ax1.set_ylabel('Continents', labelpad=15)
ax1.set_zlabel('Production (%)', labelpad=15)
ax1.set_title('Global Agricultural Production Proportions:\nMajor Crops by Continent (2022)', fontsize=14, fontweight='bold', pad=20)
ax1.set_yticks(np.arange(len(continents)))
ax1.set_yticklabels(continents, fontsize=9)
ax1.set_xticks(np.arange(len(crops)))
ax1.set_xticklabels(crops, fontsize=9, rotation=45, ha='right')
ax1.view_init(elev=30, azim=120)
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(crops))]
ax1.legend(handles, crops, title="Crops", loc="upper left", fontsize=10)

# Subplot for 5-year production growth
ax2 = fig.add_subplot(122)
bar_width = 0.15
for i, continent in enumerate(continents):
    positions = np.arange(len(crops)) + (i * bar_width)
    ax2.bar(positions, growth_data[i], bar_width, label=continent, alpha=0.8)

ax2.set_xlabel('Crops', fontsize=12)
ax2.set_ylabel('5-Year Growth (%)', fontsize=12)
ax2.set_title('5-Year Agricultural Production Growth\nby Continent and Crop', fontsize=14, fontweight='bold')
ax2.set_xticks(np.arange(len(crops)) + bar_width * (len(continents) / 2 - 0.5))
ax2.set_xticklabels(crops, fontsize=10, rotation=45, ha='right')
ax2.legend(title="Continents", fontsize=10, loc='upper left')

# Adjust layout for readability
plt.tight_layout()

# Display the combined chart
plt.show()