import matplotlib.pyplot as plt
import numpy as np

# Define the years for the chart
years = np.arange(2010, 2021)

# Define the energy sources
energy_sources = ["Solar", "Wind", "Hydroelectric", "Biomass"]

# Energy contribution data (in gigawatts)
energy_data = np.array([
    [1, 2, 3, 5, 7, 10, 14, 18, 22, 28, 35],  # Solar
    [2, 3, 5, 7, 9, 12, 15, 18, 21, 24, 27],  # Wind
    [10, 10, 11, 11, 12, 12, 13, 14, 14, 15, 15],  # Hydroelectric
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]   # Biomass
])

# Define the colors for each energy source
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF8C00']

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, energy_data, labels=energy_sources, colors=colors, alpha=0.85)

# Set titles and labels
ax.set_title('Renewable Energy Growth in a Hypothetical Country\nContribution by Source (2010-2020)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (GW)', fontsize=12)

# Format x-axis for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add legend outside of the plot
ax.legend(title='Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1), frameon=False)

# Add grid lines to the y-axis for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Adjust layout to prevent overlap and ensure visibility
plt.tight_layout()

# Show the plot
plt.show()