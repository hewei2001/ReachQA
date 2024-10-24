import matplotlib.pyplot as plt
import numpy as np

# Years from 1980 to 2020
years = np.arange(1980, 2021, 5)

# Adjusted hypothetical data for energy generation over time (in arbitrary units)
solar = [0, 2, 5, 10, 20, 35, 60, 90, 140]
wind = [0, 1, 4, 8, 15, 30, 50, 85, 120]
hydro = [25, 30, 35, 40, 50, 55, 60, 65, 70]
biomass = [4, 5, 6, 7, 8, 10, 12, 14, 15]
geothermal = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# Stack data
data = np.array([solar, wind, hydro, biomass, geothermal])

# Plot configuration
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'], colors=['#ffcc00', '#87ceeb', '#4682b4', '#32cd32', '#8b4513'], alpha=0.8)

# Customize the plot
ax.set_title('Emergence of Renewable Energy Sources Over Time\n(1980-2020)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (arbitrary units)', fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 250)
ax.grid(True, linestyle='--', alpha=0.5)

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Add legend outside of the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Energy Sources")

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()