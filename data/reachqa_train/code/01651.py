import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2030, 2041)

# Energy consumption in PetaJoules for each energy source
solar_energy = np.array([40, 60, 80, 105, 135, 170, 210, 255, 305, 360, 420])
wind_energy = np.array([50, 70, 95, 125, 160, 200, 245, 295, 350, 410, 475])
nuclear_energy = np.array([90, 92, 95, 98, 101, 104, 108, 112, 115, 118, 120])
fossil_fuels = np.array([600, 570, 540, 510, 480, 450, 420, 390, 360, 330, 300])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart with enhanced colors
colors = ['#FFD700', '#87CEEB', '#228B22', '#FF6347']  # Gold, SkyBlue, ForestGreen, Tomato
ax.stackplot(years, solar_energy, wind_energy, nuclear_energy, fossil_fuels,
             labels=['Solar Energy', 'Wind Energy', 'Nuclear Energy', 'Fossil Fuels'],
             colors=colors, alpha=0.8)

# Set the title and labels
ax.set_title('Projected Energy Consumption by Source (2030-2040)\nTransitioning Towards Renewable Energy Dominance', 
             fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (PetaJoules)', fontsize=14)

# Enhanced legend within plot area
ax.legend(loc='upper left', fontsize=10, frameon=True, bbox_to_anchor=(0.75, 1.1))

# Grid and axis modifications
ax.grid(True, which='major', linestyle='--', alpha=0.6)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Highlight the transition point with detailed annotation
ax.annotate('Renewables Surpass\nFossil Fuels',
            xy=(2040, solar_energy[-1] + wind_energy[-1] + nuclear_energy[-1]), 
            xytext=(2035, 750),
            textcoords="offset points", ha='center', fontsize=12, color='black',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

# Adding trendlines to emphasize growth paths
for y_data, color in zip([solar_energy, wind_energy, nuclear_energy, fossil_fuels], colors):
    z = np.polyfit(years, y_data, 1)
    p = np.poly1d(z)
    ax.plot(years, p(years), linestyle='--', color=color, linewidth=1.5, alpha=0.7)

# Secondary plot with total renewable energy
total_renewables = solar_energy + wind_energy + nuclear_energy
fig, ax2 = plt.subplots(figsize=(7, 5))
ax2.plot(years, total_renewables, '-o', color='#4169E1', label='Total Renewable Energy', linewidth=2)

# Title, labels, and legend for the secondary plot
ax2.set_title('Total Renewable Energy Growth (2030-2040)', fontsize=16, pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total Renewable Energy (PetaJoules)', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plots
plt.show()