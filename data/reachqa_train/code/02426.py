import matplotlib.pyplot as plt
import numpy as np

# Data for growth rates in different climate zones (in cm/year)
tropical_growth = [60, 65, 58, 62, 68, 61, 63, 64, 66, 60, 67, 65]
temperate_growth = [35, 40, 38, 42, 37, 39, 41, 36, 34, 43, 38, 39]
desert_growth = [10, 12, 11, 9, 13, 14, 8, 11, 12, 15, 10, 9]
polar_growth = [5, 4, 6, 3, 4, 5, 5, 6, 3, 4, 4, 5]

# Combine all growth data into a single dataset
growth_data = [tropical_growth, temperate_growth, desert_growth, polar_growth]

# Define labels for each climate zone
climate_zones = ['Tropical', 'Temperate', 'Desert', 'Polar']

# Create the vertical box plot
plt.figure(figsize=(10, 6))
box = plt.boxplot(
    growth_data, patch_artist=True, labels=climate_zones, 
    notch=True, medianprops={'color': 'red'}, vert=True
)

# Customize box plot appearance
colors = ['#2E8B57', '#4682B4', '#FFD700', '#D3D3D3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add title and labels
plt.title('Growth Rates of Plantus Hypotheticus\nin Different Climate Zones', fontsize=14, fontweight='bold')
plt.xlabel('Climate Zones', fontsize=12)
plt.ylabel('Growth Rate (cm/year)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()