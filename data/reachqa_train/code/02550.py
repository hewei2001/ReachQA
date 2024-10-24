import matplotlib.pyplot as plt
import numpy as np

# Define extended time range with increased temporal resolution
years = np.arange(2010, 2025, 0.25)  # Quarterly data from 2010 to 2025

# Artificial data for the percentage of total magic energy usage from different elements
fire = 25 + 3*np.sin(0.5 * np.pi * (years - 2010))
water = 20 + 2*np.sin(0.6 * np.pi * (years - 2011))
earth = 15 + 1.5*np.sin(0.7 * np.pi * (years - 2012))
air = 10 + 1.8*np.sin(0.5 * np.pi * (years - 2013))
ether = 5 + np.cos(0.8 * np.pi * (years - 2014))
void = 7 + 0.8*np.sin(0.9 * np.pi * (years - 2015))

# Normalize to ensure the sum of percentages does not exceed 100%
total_usage = fire + water + earth + air + ether + void
fire /= total_usage.sum(axis=0) / 100
water /= total_usage.sum(axis=0) / 100
earth /= total_usage.sum(axis=0) / 100
air /= total_usage.sum(axis=0) / 100
ether /= total_usage.sum(axis=0) / 100
void /= total_usage.sum(axis=0) / 100

# Stack the data vertically for the stackplot
data = np.vstack([fire, water, earth, air, ether, void])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Fire', 'Water', 'Earth', 'Air', 'Ether', 'Void'],
             colors=['#ff4500', '#00bfff', '#8b4513', '#d3d3d3', '#8a2be2', '#2f4f4f'], alpha=0.8)

# Set title and labels with multi-line title for clarity
plt.title("Arcana's Magical Energy Utilization\nA Complex Analysis of Elemental Energies Over 15 Years", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage of Total Magic Energy (%)", fontsize=14)

# Add legend and customize its position
plt.legend(title='Elemental Magics', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-ticks to improve visibility and rotate x-labels
ax.set_xticks(np.arange(2010, 2026, 1))
plt.xticks(rotation=45)

# Automatically adjust layout for better visual representation
plt.tight_layout()

# Display the plot
plt.show()