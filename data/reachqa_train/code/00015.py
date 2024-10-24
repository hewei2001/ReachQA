import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Artificial data for renewable energy generation (in GWh) per year for each country
solaria_energy = [20, 25, 35, 45, 55, 70, 85, 100, 120, 135, 150]
windlandia_energy = [15, 30, 50, 65, 80, 95, 110, 130, 150, 170, 200]
hydrovia_energy = [50, 52, 54, 55, 60, 63, 65, 68, 70, 75, 78]
geothermalia_energy = [5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70]
biomassia_energy = [10, 15, 22, 30, 40, 50, 65, 80, 100, 125, 150]

# Combine datasets for stackplot
energy_sources = np.array([solaria_energy, windlandia_energy, hydrovia_energy, geothermalia_energy, biomassia_energy])

# Calculate percentage contributions of each energy source per year
total_energy_per_year = energy_sources.sum(axis=0)
percentage_contributions = (energy_sources / total_energy_per_year) * 100

# Create a figure with two subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

# Plot 1: Stacked Area Chart
axes[0].stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'],
                  colors=['gold', 'skyblue', 'lightgreen', 'orange', 'brown'], alpha=0.8)
axes[0].set_title("Renewable Energy Generation in Simulated Countries\n(2020-2030)", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Energy Generation (GWh)", fontsize=12)
axes[0].legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source')
axes[0].grid(alpha=0.3)

# Plot 2: Line Chart for Percentage Contributions
for i, energy_source in enumerate(['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']):
    axes[1].plot(years, percentage_contributions[i], label=energy_source,
                 linestyle='--', marker='o', linewidth=1.5)
axes[1].set_title("Percentage Contribution of Each Energy Source\n(2020-2030)", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Percentage Contribution (%)", fontsize=12)
axes[1].legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source')
axes[1].grid(alpha=0.3)

# Adjust layout to prevent overlap and ensure proper spacing
plt.tight_layout()

# Display the final plots
plt.show()