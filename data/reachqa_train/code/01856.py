import matplotlib.pyplot as plt
import numpy as np

# Data for the number of tree species in different forest zones
tropical_zone = [45, 50, 52, 48, 51, 53, 47, 49, 52, 50]
temperate_zone = [25, 28, 22, 24, 29, 30, 26, 27, 23, 25]
boreal_zone = [15, 12, 14, 16, 13, 14, 11, 15, 12, 13]
rainforest_zone = [55, 58, 59, 57, 60, 62, 55, 56, 59, 61]
savanna_zone = [20, 21, 19, 22, 23, 20, 18, 19, 21, 20]

# Aggregate the data into a list of lists
data = [tropical_zone, temperate_zone, boreal_zone, rainforest_zone, savanna_zone]

# Names of the forest zones
zones = ["Tropical", "Temperate", "Boreal", "Rainforest", "Savanna"]

# Hypothetical trend data representing average species counts over time
average_trend_data = {
    "Tropical": [48, 49, 51, 50, 52],
    "Temperate": [24, 25, 26, 27, 29],
    "Boreal": [13, 14, 13, 14, 15],
    "Rainforest": [57, 58, 60, 61, 62],
    "Savanna": [19, 20, 21, 22, 21]
}

# Time points for trend data
time_points = ["2018", "2019", "2020", "2021", "2022"]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create the box plot
boxplot = ax.boxplot(data, patch_artist=True, vert=True, labels=zones, notch=True)

# Customizing the box plot colors
colors = ['#FFDDC1', '#FA6E59', '#FF9F68', '#FFBC87', '#FFD39C']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize whiskers, caps, and medians
plt.setp(boxplot['whiskers'], color='black', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='blue', linewidth=2)

# Adding trend lines for average species counts
for idx, zone in enumerate(zones):
    ax.plot(range(1, len(time_points) + 1), average_trend_data[zone], 
            label=f'Avg Trend - {zone}', marker='o', linewidth=2)

# Adding title and labels
ax.set_title("Diversity of Tree Species\nAcross Different Forest Zones\nand Trends Over Time", fontsize=14, fontweight='bold')
ax.set_xlabel("Forest Zones", fontsize=12)
ax.set_ylabel("Number of Different Tree Species", fontsize=12)

# Customize the x-axis to show both zones and years
ax.set_xticks(np.arange(1, len(zones) + 1))
ax.set_xticklabels([f"{zone}\n{year}" for zone, year in zip(zones, time_points)], rotation=0)

# Adding a legend for clarity
ax.legend(loc='upper right', fontsize=9)

# Customizing grid and layout
ax.grid(True, linestyle='--', alpha=0.6)

# Enhance visual clarity by tightening the layout
plt.tight_layout()

# Display the chart
plt.show()