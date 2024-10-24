import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Define the energy share data for each source
wind_energy = np.array([5, 10, 15, 20, 25, 30])
solar_energy = np.array([2, 5, 8, 12, 18, 25])
hydroelectric_energy = np.array([10, 12, 13, 14, 15, 15])
biomass_energy = np.array([3, 5, 7, 8, 9, 10])

# Aggregate these data to fit into an area chart
data = np.vstack([wind_energy, solar_energy, hydroelectric_energy, biomass_energy])

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, data, labels=['Wind', 'Solar', 'Hydroelectric', 'Biomass'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Set the title and labels
ax.set_title('Renewable Energy Transition in EcoLandia\n(2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Share (%)', fontsize=12)

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a legend and customize its position
ax.legend(loc='upper left', fontsize=10, title='Energy Sources')

# Set limits for the y-axis
ax.set_ylim(0, 100)

# Adding grid lines for clarity
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Customize the line and fill style
plt.tight_layout()

# Display the plot
plt.show()