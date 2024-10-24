import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the years and genres
years = np.array([2018, 2019, 2020, 2021, 2022])
genres = ['Strategy', 'Party', 'Cooperative', 'Abstract', 'Thematic']

# Define the sales data (in thousands of units) for each genre over the years
sales_data = np.array([
    [60, 70, 80, 95, 110],  # Strategy
    [50, 55, 65, 75, 85],   # Party
    [40, 50, 60, 80, 100],  # Cooperative
    [30, 35, 40, 45, 50],   # Abstract
    [20, 30, 45, 60, 75]    # Thematic
])

# Calculate percentage change year-over-year for the heatmap
percentage_change = np.diff(sales_data) / sales_data[:, :-1] * 100

# Create figure with two subplots
fig = plt.figure(figsize=(18, 8))

# 3D Bar Chart
ax1 = fig.add_subplot(121, projection='3d')
x_pos, y_pos = np.meshgrid(np.arange(len(years)), np.arange(len(genres)))
x_pos = x_pos.flatten()
y_pos = y_pos.flatten()
z_pos = np.zeros_like(x_pos)
sales = sales_data.flatten()
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#FF8333']
colors = np.repeat(colors, len(years))
ax1.bar3d(x_pos, y_pos, z_pos, 0.5, 0.5, sales, color=colors, shade=True)

# Axes labels for the 3D plot
ax1.set_xlabel('Year', labelpad=10)
ax1.set_ylabel('Genre', labelpad=10)
ax1.set_zlabel('Units Sold (Thousands)', labelpad=10)
ax1.set_title('Board Game Genre Popularity (2018-2022)', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(genres)))
ax1.set_yticklabels(genres)
ax1.view_init(elev=20, azim=120)

# Heatmap for percentage change
ax2 = fig.add_subplot(122)
heatmap = ax2.imshow(percentage_change, aspect='auto', cmap='coolwarm', interpolation='nearest')

# Axes labels and title for the heatmap
ax2.set_xlabel('Year')
ax2.set_ylabel('Genre')
ax2.set_title('Year-over-Year Sales Growth (%)', fontsize=14, fontweight='bold')
ax2.set_xticks(np.arange(len(years) - 1))
ax2.set_xticklabels(years[1:], rotation=45, ha='right')
ax2.set_yticks(np.arange(len(genres)))
ax2.set_yticklabels(genres)

# Add colorbar for heatmap
cbar = fig.colorbar(heatmap, ax=ax2, orientation='vertical')
cbar.set_label('Percentage Change (%)', rotation=270, labelpad=15)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plots
plt.show()