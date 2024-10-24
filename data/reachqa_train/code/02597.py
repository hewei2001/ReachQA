import matplotlib.pyplot as plt
import numpy as np

# Define the years and the types of renewable energy
years = np.arange(2000, 2021)
energy_sources = ['Solar', 'Wind', 'Hydropower']

# Define the data for each energy source in gigawatt-hours
solar_energy = [1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192]
wind_energy = [0, 1, 2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173]
hydropower_energy = [5, 6, 7, 8, 10, 13, 17, 22, 28, 35, 43, 52, 62, 73, 85, 98, 112, 127, 143, 160, 178]

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stackplot
ax.stackplot(years, solar_energy, wind_energy, hydropower_energy, labels=energy_sources, colors=['#FFD700', '#87CEEB', '#32CD32'], alpha=0.8)

# Title and labels
ax.set_title('Tracing the Evolution of Renewable Energy Adoption\nin Metropolis (2000-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=12)

# Legend
ax.legend(loc='upper left', fontsize=11)

# Customize ticks
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 450, 50))

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Add annotations
for i, energy in enumerate(energy_sources):
    ax.annotate(energy, xy=(2020, solar_energy[-1] if i == 0 else solar_energy[-1] + wind_energy[-1] if i == 1 else solar_energy[-1] + wind_energy[-1] + hydropower_energy[-1]), 
                xytext=(2021, 350 - i*50), textcoords='data',
                arrowprops=dict(facecolor='gray', shrink=0.05),
                fontsize=10, fontweight='bold')

# Final adjustments
plt.tight_layout()

# Display the plot
plt.show()