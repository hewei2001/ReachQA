import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Years from 2020 to 2025
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])

# Percentage contributions of each energy source over the years
# Rows: Solar, Wind, Hydropower, Biomass
percentages = np.array([
    [20, 22, 24, 25, 27, 28],  # Solar
    [30, 32, 31, 33, 34, 35],  # Wind
    [35, 33, 32, 30, 28, 27],  # Hydropower
    [15, 13, 13, 12, 11, 10],  # Biomass
])

# Colors for each energy source
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513']

# Create the 3D plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar positions
num_sources = percentages.shape[0]
x_positions = np.arange(len(years))
bar_width = 0.2

# Plot bars for each energy source
for idx, (color, percent) in enumerate(zip(colors, percentages)):
    y_positions = idx * bar_width  # Separate each energy source
    ax.bar3d(x_positions, y_positions, np.zeros_like(x_positions), 
             bar_width, bar_width, percent, color=color, alpha=0.8)

# Set labels and ticks
ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Energy Source', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_title('Evolution of Renewable Energy Source Contributions\nin Global Energy Production (2020-2025)', fontsize=14, pad=30)
ax.set_xticks(x_positions + bar_width * 1.5)
ax.set_xticklabels(years)
ax.set_yticks([bar_width * i + bar_width / 2 for i in range(num_sources)])
ax.set_yticklabels(['Solar', 'Wind', 'Hydropower', 'Biomass'])

# Set Z limit to 100 for percentage representation
ax.set_zlim(0, 100)

# Adjust view angle
ax.view_init(elev=20., azim=-60)

# Add a legend
ax.legend(['Solar', 'Wind', 'Hydropower', 'Biomass'], loc='upper right', fontsize=10, frameon=True)

# Automatically adjust subplot params for a good layout
plt.tight_layout()

# Display the plot
plt.show()