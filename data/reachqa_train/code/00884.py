import matplotlib.pyplot as plt
import numpy as np

# Data setup: Monthly energy consumption (in megawatt-hours) for five districts
district_1 = [150, 160, 170, 180, 175, 185, 190, 195, 200, 205, 210, 215]
district_2 = [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]
district_3 = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
district_4 = [90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
district_5 = [180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235]

data = [district_1, district_2, district_3, district_4, district_5]
district_names = ['Downtown', 'Suburban', 'Industrial', 'Residential', 'Commercial']

# Calculate year-over-year percentage change as additional data for line plot overlay
yoy_change = [
    [100 * (n - p) / p for p, n in zip(d[:-1], d[1:])] for d in data
]

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Box plot
boxprops = dict(facecolor='lightblue', color='navy')
whiskerprops = dict(color='navy', linestyle='--')
medianprops = dict(color='orange', linewidth=2)
flierprops = dict(marker='o', color='red', markersize=8)

ax1.boxplot(data, vert=False, patch_artist=True, notch=True, 
            boxprops=boxprops, whiskerprops=whiskerprops,
            medianprops=medianprops, flierprops=flierprops)

# Set titles and labels
ax1.set_title('Energy Consumption Patterns Across Urban Districts\nMonthly Analysis Over One Year', 
              fontsize=14, weight='bold')
ax1.set_xlabel('Monthly Energy Consumption (MWh)', fontsize=12)
ax1.set_yticks(np.arange(1, len(district_names) + 1))
ax1.set_yticklabels(district_names)

# Additional axis for line plot
ax2 = ax1.twinx()

# Line plot overlay for year-over-year change
for index, changes in enumerate(yoy_change):
    ax2.plot(changes, [index + 1] * len(changes), marker='s', label=f'{district_names[index]} Change', linewidth=1.5)

ax2.set_ylabel('YoY Change (%)', fontsize=12)
ax2.set_yticks(np.arange(1, len(district_names) + 1))
ax2.set_yticklabels([])  # Remove y-tick labels on ax2 to avoid duplicate labels
ax2.legend(loc='upper right', fontsize=10)

# Adding grid for readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()