import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define regions and architectural styles
regions = ['Europe', 'Asia', 'Americas']
styles = ['Gothic', 'Baroque', 'Classical', 'Modernist', 'Renaissance']

# Data for percentage influence in each region
europe_data = [40, 20, 25, 10, 5]
asia_data = [15, 10, 35, 30, 10]
americas_data = [10, 15, 20, 40, 15]

# Combine all data for easier indexing
data = [europe_data, asia_data, americas_data]

# Define positions using meshgrid for placement
x = np.arange(len(regions))
y = np.arange(len(styles))
x, y = np.meshgrid(x, y)

# Transpose data for bar placement
data_values = np.array(data).T

# Create a 3D bar chart
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define colors for each architectural style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot 3D bars using bar3d
for i in range(len(styles)):
    ax.bar3d(x[i], y[i], np.zeros_like(data_values[i]), 0.4, 0.4, data_values[i], color=colors[i], alpha=0.8, label=styles[i])

# Title and labels
ax.set_title("Inspiration from the Past:\nModern Architectural Trends Influenced by Ancient Styles", fontsize=14, weight='bold', pad=30)
ax.set_xlabel('Regions', labelpad=15)
ax.set_ylabel('Styles', labelpad=15)
ax.set_zlabel('Influence (%)', labelpad=15)

# Set tick labels
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, fontsize=10, rotation=45, ha='right')
ax.set_yticks(np.arange(len(styles)))
ax.set_yticklabels(styles, fontsize=10)

# Normalize Z-axis
ax.set_zlim(0, 100)

# Add legend
ax.legend(title='Architectural Styles', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Overlay plot - Trend line for Europe's historical influence
historical_years = [2000, 2005, 2010, 2015, 2020]
historical_influence_gothic = [30, 35, 37, 38, 40]  # Hypothetical trend data

# Add 2D line plot in 3D space
ax.plot(np.full(len(historical_years), 0), np.full(len(historical_years), 0), historical_years, historical_influence_gothic, 
        color='black', marker='o', linestyle='-', linewidth=2, label='Gothic Trend in Europe')

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()