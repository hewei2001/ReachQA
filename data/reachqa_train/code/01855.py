import matplotlib.pyplot as plt
import numpy as np

# Data for the number of tree species in different forest zones
# Each list contains species counts from sample plots in that forest zone
tropical_zone = [45, 50, 52, 48, 51, 53, 47, 49, 52, 50]
temperate_zone = [25, 28, 22, 24, 29, 30, 26, 27, 23, 25]
boreal_zone = [15, 12, 14, 16, 13, 14, 11, 15, 12, 13]
rainforest_zone = [55, 58, 59, 57, 60, 62, 55, 56, 59, 61]
savanna_zone = [20, 21, 19, 22, 23, 20, 18, 19, 21, 20]

# Aggregate the data into a list of lists
data = [tropical_zone, temperate_zone, boreal_zone, rainforest_zone, savanna_zone]

# Names of the forest zones
zones = ["Tropical", "Temperate", "Boreal", "Rainforest", "Savanna"]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Create the box plot
boxplot = ax.boxplot(data, patch_artist=True, vert=True, labels=zones, notch=True)

# Customizing the box plot
colors = ['#FFDDC1', '#FA6E59', '#FF9F68', '#FFBC87', '#FFD39C']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize whiskers, caps, and medians
plt.setp(boxplot['whiskers'], color='black', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='blue', linewidth=2)

# Adding title and labels
ax.set_title("Diversity of Tree Species\nAcross Different Forest Zones", fontsize=14, fontweight='bold')
ax.set_xlabel("Forest Zones", fontsize=12)
ax.set_ylabel("Number of Different Tree Species", fontsize=12)

# Customizing grid and layout
ax.grid(True, linestyle='--', alpha=0.6)

# Enhance visual clarity by tightening the layout
plt.tight_layout()

# Display the chart
plt.show()