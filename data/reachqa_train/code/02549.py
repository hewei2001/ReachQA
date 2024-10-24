import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2019
years = np.arange(2010, 2020)

# Artificial data for the percentage of total magic energy usage from different elements
fire = np.array([25, 27, 29, 30, 28, 26, 27, 29, 31, 33])
water = np.array([20, 22, 21, 23, 24, 25, 24, 22, 21, 20])
earth = np.array([15, 16, 17, 18, 19, 20, 21, 20, 19, 18])
air = np.array([10, 9, 10, 11, 12, 13, 14, 15, 16, 17])

# Stack the data vertically for the stackplot
data = np.vstack([fire, water, earth, air])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=['Fire', 'Water', 'Earth', 'Air'],
             colors=['#ff4500', '#00bfff', '#8b4513', '#d3d3d3'], alpha=0.8)

# Set title and labels with multi-line title for clarity
plt.title("Arcana's Magical Energy Utilization\nA Decade of Elemental Mastery", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage of Total Magic Energy (%)", fontsize=14)

# Add legend and customize its position
plt.legend(title='Elemental Magics', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-ticks to improve visibility and rotate x-labels if necessary
ax.set_xticks(years)
plt.xticks(rotation=45)

# Automatically adjust layout for better visual representation
plt.tight_layout()

# Display the plot
plt.show()