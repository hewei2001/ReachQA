import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the x-axis
decades = ['1990s', '2000s', '2010s', '2020s']

# Contribution of each renewable source (in arbitrary units)
solar_energy = [5, 15, 50, 120]    # Exponential growth
wind_energy = [10, 25, 60, 150]    # Rapid growth
hydroelectric = [100, 120, 150, 160] # Stable growth
biomass_energy = [20, 30, 40, 55]  # Steady growth

# Stack these contributions for the area chart
energy_data = np.array([solar_energy, wind_energy, hydroelectric, biomass_energy])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Define colors for each energy source
colors = ['#FFA07A', '#20B2AA', '#87CEEB', '#FFD700']

# Create stacked area chart
ax.stackplot(decades, energy_data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass'], colors=colors, alpha=0.8)

# Customize the plot with title, labels, and legend
ax.set_title('Contribution of Renewable Energy Sources Over Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Energy Contribution\n(Arbitrary Units)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title='Energy Type')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to prevent label overlapping
plt.tight_layout()

# Show the plot
plt.show()