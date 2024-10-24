import matplotlib.pyplot as plt
import numpy as np

# Regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']

# Solar power capacity data (in megawatts) for each region
north_america = [150, 160, 165, 170, 155, 160, 165, 180, 175, 160]
europe = [100, 110, 105, 115, 110, 120, 130, 125, 115, 105]
asia = [200, 210, 205, 220, 215, 225, 230, 240, 235, 210]
africa = [50, 55, 60, 65, 70, 55, 60, 75, 65, 60]
south_america = [80, 85, 90, 95, 85, 100, 105, 90, 95, 100]

# Aggregating all data
data = [north_america, europe, asia, africa, south_america]

# Create a vertical boxplot
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, patch_artist=True, labels=regions, notch=True, widths=0.6)

# Customize box plot colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize other properties
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='grey', linewidth=2)
    cap.set(color='grey', linewidth=2)
    
for median in box['medians']:
    median.set(color='orange', linewidth=3)
    
for flier in box['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

# Title and labels
plt.title("Distribution of Solar Energy Installations\nAcross Regions (in MW)", fontsize=16, weight='bold')
plt.ylabel("Solar Power Capacity (MW)", fontsize=12)
plt.xlabel("Regions", fontsize=12)

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend for regions
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
plt.legend(handles, regions, title="Regions", loc='upper right')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()