import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the characteristics and their respective scores for two different regions of the Amazon rainforest
categories = ['Biodiversity', 'Carbon Storage', 'Precipitation', 
              'Temperature Stability', 'Human Impact']

# Data for protected reserves and deforested regions
protected_reserves = [9, 8, 9, 7, 3]
deforested_regions = [4, 5, 6, 5, 8]

# Number of variables
N = len(categories)

# Compute angle for each category on the radar chart
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the radar chart

# Append the starting value to the end for both areas to close the radar chart
protected_reserves += protected_reserves[:1]
deforested_regions += deforested_regions[:1]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one filled area for protected reserves
ax.fill(angles, protected_reserves, color='green', alpha=0.25)
ax.plot(angles, protected_reserves, color='green', linewidth=2, label='Protected Reserves')

# Draw another filled area for deforested regions
ax.fill(angles, deforested_regions, color='red', alpha=0.25)
ax.plot(angles, deforested_regions, color='red', linewidth=2, label='Deforested Regions')

# Customize the plot: set labels, ticks, and title
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 10)  # Set radial limits

# Add title and legend
ax.set_title('Ecosystem Resilience: A Radar Analysis\nof Rainforest Characteristics', 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Ensure no overlapping elements
plt.tight_layout()

# Display the radar chart
plt.show()