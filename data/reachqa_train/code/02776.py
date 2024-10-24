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

# Create additional time-series data for line chart
years = np.arange(2015, 2024)
solar_growth = np.array([5, 10, 15, 20, 22, 25, 28, 30, 33])  # Hypothetical growth in Solar energy consumption
wind_growth = np.array([10, 13, 16, 18, 20, 23, 25, 28, 30])

# Create the plot with two subplots side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot stacked bar chart
bottom_values = np.zeros(len(continents))
for idx, (data, color) in enumerate(zip(energy_data_transposed, colors)):
    ax1.bar(continents, data, label=energy_sources[idx], color=color, bottom=bottom_values)
    bottom_values += data

# Bar chart configuration
ax1.set_title('Energy Consumption Distribution Across Continents in 2023\nTransition Towards Sustainable Energy', 
              fontsize=14, fontweight='bold')
ax1.set_xlabel('Continents', fontsize=12)
ax1.set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=12)
ax1.set_xticklabels(continents, rotation=30, ha='right')
ax1.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1.05, 1))
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Plot line chart
ax2.plot(years, solar_growth, label='Solar', color=colors[0], marker='o')
ax2.plot(years, wind_growth, label='Wind', color=colors[1], marker='o')

# Line chart configuration
ax2.set_title('Growth Trend of Renewable Energy\n(2015-2023)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Energy Consumption (%)', fontsize=12)
ax2.legend(title='Energy Sources', loc='upper left')
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()