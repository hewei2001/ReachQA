import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Define the energy share data for each source
wind_energy = np.array([5, 10, 15, 20, 25, 30])
solar_energy = np.array([2, 5, 8, 12, 18, 25])
hydroelectric_energy = np.array([10, 12, 13, 14, 15, 15])
biomass_energy = np.array([3, 5, 7, 8, 9, 10])

# Additional data for a new chart (e.g., growth rates between periods)
growth_rates = np.array([
    wind_energy[1:] - wind_energy[:-1],
    solar_energy[1:] - solar_energy[:-1],
    hydroelectric_energy[1:] - hydroelectric_energy[:-1],
    biomass_energy[1:] - biomass_energy[:-1]
])

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Plot the stacked area chart on the first subplot
axs[0].stackplot(years, wind_energy, solar_energy, hydroelectric_energy, biomass_energy, 
                 labels=['Wind', 'Solar', 'Hydroelectric', 'Biomass'],
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)
axs[0].set_title('Renewable Energy Transition in EcoLandia\n(2010-2020)', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Energy Share (%)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45, ha='right')
axs[0].legend(loc='upper left', fontsize=10, title='Energy Sources')
axs[0].set_ylim(0, 100)
axs[0].grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Plot the grouped bar chart on the second subplot
bar_width = 0.2
indices = np.arange(len(years) - 1)

# Align bars to make a grouped bar chart
for i, data in enumerate(growth_rates):
    axs[1].bar(indices + i * bar_width, data, bar_width, label=['Wind', 'Solar', 'Hydroelectric', 'Biomass'][i],
               color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'][i], alpha=0.8)

axs[1].set_title('Growth in Renewable Energy Share\n(Yearly Increments)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Time Periods', fontsize=12)
axs[1].set_ylabel('Growth in Energy Share (%)', fontsize=12)
axs[1].set_xticks(indices + bar_width * 1.5)
axs[1].set_xticklabels(['2010-12', '2012-14', '2014-16', '2016-18', '2018-20'], rotation=45, ha='right')
axs[1].legend(loc='upper left', fontsize=10, title='Energy Sources')
axs[1].grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()