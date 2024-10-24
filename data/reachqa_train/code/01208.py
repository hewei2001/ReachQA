import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

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

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Define a color map
colors = [cm.viridis(i / len(energy_sources)) for i in range(len(energy_sources))]

# Plot the stacked area chart with gradient effect
ax.stackplot(years, energy_data, labels=energy_sources, colors=colors, alpha=0.85)

# Set titles and labels with improved readability
ax.set_title('Renewable Energy Growth in a Hypothetical Country\n'
             'Contribution by Source (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (GW)', fontsize=12)

# Format x-axis for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add legend outside of the plot
ax.legend(title='Energy Sources', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1), frameon=False)

# Add grid lines for better readability
ax.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Add annotations for key data points
annotations = {
    2020: 'Solar becomes significant',
    2012: 'Start of rapid growth in Wind',
    2015: 'Hydroelectric stable'
}

for year, annotation in annotations.items():
    ax.annotate(annotation, xy=(year, energy_data[:, years.tolist().index(year)].sum()), 
                xytext=(year, energy_data[:, years.tolist().index(year)].sum() + 5),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9, ha='center')

# Adding a line plot for total energy production
total_energy = energy_data.sum(axis=0)
ax.plot(years, total_energy, label='Total Production', color='black', linestyle='-', marker='o', linewidth=1.5)
ax.fill_between(years, total_energy, color='black', alpha=0.1)

# Adding a secondary y-axis for total energy production
ax2 = ax.twinx()
ax2.set_ylabel('Total Production (GW)', fontsize=12)
ax2.plot(years, total_energy, color='black', linestyle='-', linewidth=0)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()