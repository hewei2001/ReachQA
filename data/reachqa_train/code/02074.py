import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])
solar = np.array([20, 25, 30, 35, 42, 50, 60, 65, 70])  # Solar energy generation (in TWh)
wind = np.array([15, 18, 22, 28, 35, 40, 45, 50, 55])    # Wind energy generation (in TWh)
hydro = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18])   # Hydro energy generation (in TWh)
geothermal = np.array([5, 5, 6, 7, 8, 9, 10, 11, 12])    # Geothermal energy generation (in TWh)
biomass = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])  # Biomass energy generation (in TWh)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area plot
ax.stackplot(years, solar, wind, hydro, geothermal, biomass, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], colors=['gold', 'lightskyblue', 'lightgreen', 'salmon', 'peru'], alpha=0.85)

# Title and Labels
ax.set_title('Renewable Energy Generation Trends\nin Solaria (2015-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (TWh)', fontsize=12)

# Grid and Legend
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources', fontsize=11)

# Additional Context
# Add a marker and annotate a significant milestone
milestone_year_idx = 5  # Year 2020
milestone_value = solar[milestone_year_idx] + wind[milestone_year_idx] + hydro[milestone_year_idx] + geothermal[milestone_year_idx] + biomass[milestone_year_idx]
ax.plot(years[milestone_year_idx], milestone_value, 'ro')
ax.annotate('Milestone:\n2020 Exceeds 100 TWh',
            xy=(years[milestone_year_idx], milestone_value), xytext=(5, 125),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center', fontweight='bold')

# Adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()