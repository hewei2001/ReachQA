import matplotlib.pyplot as plt
import numpy as np

# Define categories of energy sources and continents
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Coal', 'Oil']
continents = ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia']

# Hypothetical energy consumption data (% of total energy consumption by source)
energy_data = np.array([
    [25, 20, 15, 30, 10],  # North America
    [30, 25, 20, 15, 10],  # South America
    [40, 25, 15, 10, 10],  # Europe
    [15, 10, 20, 30, 25],  # Africa
    [10, 20, 25, 30, 15],  # Asia
    [35, 30, 20, 10, 5]    # Australia
])

# Transpose the data for plotting
energy_data_transposed = energy_data.T

# Define colors for each energy source
colors = ['#ffcc00', '#66c2a5', '#3288bd', '#e31a1c', '#fb9a99']

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot stacked bar chart
bottom_values = np.zeros(len(continents))
for idx, (data, color) in enumerate(zip(energy_data_transposed, colors)):
    ax.bar(continents, data, label=energy_sources[idx], color=color, bottom=bottom_values)
    bottom_values += data  # Update the bottom values for stacking

# Set title and labels with line breaks for clarity
ax.set_title('Energy Consumption Distribution Across Continents in 2023\nTransition Towards Sustainable Energy', 
             fontsize=16, fontweight='bold', linespacing=1.5)
ax.set_xlabel('Continents', fontsize=14)
ax.set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=14)

# Rotate x-axis labels to prevent overlap
ax.set_xticklabels(continents, rotation=30, ha='right')

# Add legend and position it outside the plot area
ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1.05, 1))

# Enable grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()