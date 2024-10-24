import matplotlib.pyplot as plt
import numpy as np

# Years from 1980 to 2020
years = np.arange(1980, 2021, 5)

# Adjusted hypothetical data for energy generation over time (in arbitrary units)
solar = np.array([0, 2, 5, 10, 20, 35, 60, 90, 140])
wind = np.array([0, 1, 4, 8, 15, 30, 50, 85, 120])
hydro = np.array([25, 30, 35, 40, 50, 55, 60, 65, 70])
biomass = np.array([4, 5, 6, 7, 8, 10, 12, 14, 15])
geothermal = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

# Stack data
data = np.array([solar, wind, hydro, biomass, geothermal])
total_energy = np.sum(data, axis=0)

# Calculate percentage contribution for each energy source
percentages = data / total_energy * 100

# Plot configuration
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Stacked Area Chart
ax1.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'], 
              colors=['#ffcc00', '#87ceeb', '#4682b4', '#32cd32', '#8b4513'], alpha=0.8)
ax1.set_title('Renewable Energy Generation\nOver Time (1980-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Energy Generation (arbitrary units)')
ax1.set_xlim(years[0], years[-1])
ax1.set_ylim(0, 250)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=9, title="Energy Sources")

# Subplot 2: Line Chart for Percentage Contribution
for i, label in enumerate(['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']):
    ax2.plot(years, percentages[i], label=label, linewidth=2)

ax2.set_title('Percentage Contribution of\nEach Energy Source (1980-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year')
ax2.set_ylabel('Percentage Contribution (%)')
ax2.set_xlim(years[0], years[-1])
ax2.set_ylim(0, 100)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left', fontsize=9, title="Energy Sources")

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()