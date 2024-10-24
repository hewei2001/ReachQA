import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])
solar = np.array([20, 25, 30, 35, 42, 50, 60, 65, 70])  # Solar energy generation (in TWh)
wind = np.array([15, 18, 22, 28, 35, 40, 45, 50, 55])    # Wind energy generation (in TWh)
hydro = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18])   # Hydro energy generation (in TWh)
geothermal = np.array([5, 5, 6, 7, 8, 9, 10, 11, 12])    # Geothermal energy generation (in TWh)
biomass = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])  # Biomass energy generation (in TWh)

# Calculate total energy and solar percentage
total_energy = solar + wind + hydro + geothermal + biomass
solar_percentage = (solar / total_energy) * 100

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stacked area plot for energy sources
ax1.stackplot(years, solar, wind, hydro, geothermal, biomass, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'],
              colors=['gold', 'lightskyblue', 'lightgreen', 'salmon', 'peru'], alpha=0.85)

# Overlay line plot for total renewable energy
ax1.plot(years, total_energy, 'k--', label='Total Renewable Energy', linewidth=2)
ax1.set_title('Renewable Energy Generation Trends\nin Solaria (2015-2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Generation (TWh)', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Second y-axis for solar energy percentage
ax2 = ax1.twinx()
ax2.plot(years, solar_percentage, 'r-', label='Solar % of Total', linewidth=2)
ax2.set_ylabel('Solar Energy (%)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Legend for both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1, 1), title='Legend')

# Add a marker and annotate a significant milestone
milestone_year_idx = 5  # Year 2020
ax1.plot(years[milestone_year_idx], total_energy[milestone_year_idx], 'ro')
ax1.annotate('Milestone:\n2020 Exceeds 100 TWh',
             xy=(years[milestone_year_idx], total_energy[milestone_year_idx]), xytext=(5, 125),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, ha='center', fontweight='bold')

# Adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()