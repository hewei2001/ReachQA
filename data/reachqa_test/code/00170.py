import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Define cities and days
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define hypothetical AQI data for each city across the days
aqi_data = np.array([
    [90, 100, 85, 110, 95, 80, 70],   # New York
    [75, 80, 70, 65, 60, 58, 55],     # Los Angeles
    [60, 65, 75, 70, 80, 85, 90],     # Chicago
    [85, 90, 95, 100, 85, 80, 75],    # Houston
    [95, 100, 105, 110, 115, 90, 85]  # Phoenix
])

# Create a new figure with a GridSpec layout
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 1, height_ratios=[2, 1])

# First subplot: Heatmap
ax1 = fig.add_subplot(gs[0, 0])
heatmap = ax1.imshow(aqi_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')
ax1.set_title('Urban Air Quality Monitoring:\nWeeklong Pollution Levels Across Cities', fontsize=16, pad=20)
ax1.set_xlabel('Days of the Week', fontsize=14)
ax1.set_ylabel('Cities', fontsize=14)
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days, fontsize=12, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(cities)))
ax1.set_yticklabels(cities, fontsize=12)

# Add color bar for heatmap
colorbar = fig.colorbar(heatmap, ax=ax1)
colorbar.set_label('Air Quality Index (AQI)', fontsize=12)

# Add value annotations on the heatmap
for i in range(len(cities)):
    for j in range(len(days)):
        ax1.text(j, i, f'{aqi_data[i, j]}', ha="center", va="center", color="black", fontsize=10, weight='bold')

# Second subplot: Line Plot
ax2 = fig.add_subplot(gs[1, 0])
for i, city in enumerate(cities):
    ax2.plot(days, aqi_data[i, :], marker='o', label=city)

ax2.set_title('Daily AQI Trends Across Cities', fontsize=16, pad=10)
ax2.set_xlabel('Days of the Week', fontsize=14)
ax2.set_ylabel('AQI', fontsize=14)
ax2.legend(loc='upper left', fontsize=12, ncol=2)
ax2.grid(True, linestyle='--', alpha=0.7)

# Automatic adjustment of layout to avoid overlaps
plt.tight_layout()

# Show the plot
plt.show()