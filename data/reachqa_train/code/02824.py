import matplotlib.pyplot as plt
import numpy as np

# Define the decades for x-axis
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Define the percentage share of each renewable energy source in urban energy supply
solar = [2, 3, 5, 10, 20, 30, 40]
wind = [1, 2, 10, 15, 25, 30, 25]
geothermal = [3, 4, 6, 7, 10, 8, 5]
hydropower = [25, 30, 35, 28, 22, 18, 15]
biomass = [9, 8, 6, 5, 3, 2, 2]

# Stack the data vertically to prepare for the stackplot
data = np.vstack([solar, wind, geothermal, hydropower, biomass])

# Create a figure and an axis object
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a stacked area chart
ax.stackplot(decades, data, labels=['Solar', 'Wind', 'Geothermal', 'Hydropower', 'Biomass'],
             colors=['#FFD700', '#1E90FF', '#32CD32', '#4682B4', '#8B4513'], alpha=0.85)

# Set the title and axes labels
ax.set_title('The Rise and Fall of Renewable Energy Sources in Urban Development\n(1960s to 2020s)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Energy Share (%)', fontsize=12)

# Configure the legend to be outside the plot to avoid overlapping
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent overlap of elements
plt.tight_layout()

# Display the plot
plt.show()