import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2025
years = np.arange(2015, 2026)

# Synthetic data for the percentage of total energy consumption from renewable sources
solar = np.array([5, 7, 10, 12, 15, 17, 20, 23, 25, 28, 30])
wind = np.array([3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 20])
hydro = np.array([10, 11, 11, 12, 13, 13, 14, 14, 15, 15, 16])
biomass = np.array([2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10])

# Stack the data vertically for the stackplot
data = np.vstack([solar, wind, hydro, biomass])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], 
             colors=['#ffd700', '#87ceeb', '#4682b4', '#8fbc8f'], alpha=0.8)

# Set title and labels with multiline title for clarity
plt.title("Rise of Renewable Energy Sources\nin EcoCity: 2015-2025", fontsize=16, weight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage of Total Energy Consumption (%)", fontsize=14)

# Add legend and customize its position
plt.legend(title='Renewable Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhance grid visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust x-ticks to improve visibility and rotate x-labels if necessary
ax.set_xticks(years)
plt.xticks(rotation=45)

# Automatically adjust layout for better visual representation
plt.tight_layout()

# Display the plot
plt.show()