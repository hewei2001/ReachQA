import matplotlib.pyplot as plt
import numpy as np

# Observatory data
observatories = [
    'Mount Cosmic', 'Sky Haven', 'Nebula Peak', 
    'Starlight Ridge', 'Astro Valley', 'Galaxy Summit'
]
altitudes = np.array([4200, 2500, 3000, 1500, 2700, 5000])  # Altitude in meters
apertures = np.array([10.0, 6.5, 8.0, 5.0, 7.2, 12.0])  # Aperture size in meters
clear_nights = np.array([280, 200, 220, 180, 210, 290])  # Average clear nights per year

# Create scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(altitudes, apertures, 
                      s=clear_nights, alpha=0.7,
                      c=apertures, cmap='coolwarm', edgecolors='k')

# Title and labels
plt.title("Exploring the Cosmos:\nObservatory Capabilities and Locations", fontsize=14, fontweight='bold')
plt.xlabel("Altitude of Observatory (meters)", fontsize=12)
plt.ylabel("Telescope Aperture Size (meters)", fontsize=12)

# Annotate observatories
for i, name in enumerate(observatories):
    plt.text(altitudes[i], apertures[i], name, fontsize=10, ha='right', va='bottom')

# Add color bar for aperture size
colorbar = plt.colorbar(scatter)
colorbar.set_label('Telescope Aperture Size (meters)', fontsize=11)

# Add legend for bubble size
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='180 Clear Nights',
           markerfacecolor='grey', markersize=np.sqrt(180)),
    Line2D([0], [0], marker='o', color='w', label='250 Clear Nights',
           markerfacecolor='grey', markersize=np.sqrt(250)),
    Line2D([0], [0], marker='o', color='w', label='300 Clear Nights',
           markerfacecolor='grey', markersize=np.sqrt(300))
]
plt.legend(handles=legend_elements, loc='upper left', title='Clear Nights Bubble Size')

# Grid for improved readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()