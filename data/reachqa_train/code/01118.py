import matplotlib.pyplot as plt
import numpy as np

# Artificial height data in cm for various zones
desert_zone_heights = [35, 45, 50, 55, 60, 65, 70]
tropical_zone_heights = [150, 160, 170, 180, 190, 200, 210, 220, 230]
temperate_zone_heights = [85, 90, 95, 100, 110, 115]
alpine_zone_heights = [10, 15, 20, 25, 30, 35, 40]

# Combine the data into a list
heights_data = [desert_zone_heights, tropical_zone_heights, temperate_zone_heights, alpine_zone_heights]

# Define the labels for each zone
zone_labels = ['Desert Zone', 'Tropical Zone', 'Temperate Zone', 'Alpine Zone']

# Define colors for each box plot
colors = ['#FFCC99', '#66B3FF', '#99FF99', '#FF6666']

# Create the horizontal box chart
plt.figure(figsize=(12, 7))
boxplots = plt.boxplot(heights_data, vert=False, patch_artist=True, 
                       positions=np.arange(1, len(heights_data) + 1),
                       boxprops=dict(facecolor='lightgrey', color='black'),
                       whiskerprops=dict(color='black'),
                       capprops=dict(color='black'),
                       medianprops=dict(color='darkorange'),
                       flierprops=dict(marker='o', color='red', alpha=0.5),
                       notch=True)

# Fill each box with a different color
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Add labels and title
plt.yticks(np.arange(1, len(zone_labels) + 1), zone_labels)
plt.xlabel('Height (cm)', fontsize=12)
plt.title('Diverse Flora Heights:\nA Comparative Study in GreenFields Botanical Reserve', fontsize=14, weight='bold')

# Add grid lines for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()