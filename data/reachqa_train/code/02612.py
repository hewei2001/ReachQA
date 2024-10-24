import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2081, 1)  # Annual data for increased granularity

# Define energy usage data as a percentage of total transportation energy
# with additional sources and dynamic complexity
fossil_fuels = np.clip(np.linspace(80, 0, len(years)), 0, 100)
electric = np.clip(np.linspace(10, 60, len(years)) + np.sin(years/2)*5, 0, 100)
hydrogen = np.clip(np.linspace(5, 30, len(years)) + np.cos(years/2)*3, 0, 100)
biofuels = np.clip(np.linspace(5, 15, len(years)), 0, 100)
solar = np.clip(np.linspace(0, 20, len(years)) + np.sin(years/3)*2, 0, 100)
wind = np.clip(np.linspace(0, 10, len(years)) + np.cos(years/3)*2, 0, 100)

# Normalize so the sum is always 100
total_energy = np.array([fossil_fuels, electric, hydrogen, biofuels, solar, wind])
total_energy_normalized = total_energy / total_energy.sum(axis=0) * 100

# Set up the figure and axes for a subplot
fig, axs = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Create stacked area chart for energy distribution
axs[0].stackplot(years, *total_energy_normalized,
                 labels=['Fossil Fuels', 'Electric', 'Hydrogen', 'Biofuels', 'Solar', 'Wind'],
                 colors=['#d95f02', '#7570b3', '#1b9e77', '#e7298a', '#66c2a5', '#fc8d62'],
                 alpha=0.85)

# Title and labels
axs[0].set_title('Transportation Energy Evolution\nFrom Fossil Fuels to Future Energy (2020-2080)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_ylabel('Energy Source Proportion (%)', fontsize=12)

# Customize legend
axs[0].legend(title="Energy Sources", fontsize=10, title_fontsize='12', loc='upper left', bbox_to_anchor=(1, 1))

# Ensure grid lines for y-axis
axs[0].grid(axis='y', linestyle='--', alpha=0.6)

# Create additional plot for cumulative adoption of renewables
renewable_sources = total_energy_normalized[1:]  # Excluding fossil fuels
cumulative_renewable = renewable_sources.sum(axis=0)

axs[1].plot(years, cumulative_renewable, color='b', lw=2)
axs[1].fill_between(years, 0, cumulative_renewable, color='b', alpha=0.3)
axs[1].set_title('Cumulative Adoption of Renewable Energy Sources (2020-2080)', fontsize=14, pad=15)
axs[1].set_ylabel('Cumulative Proportion (%)', fontsize=12)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].grid(axis='y', linestyle='--', alpha=0.6)

# Enhance readability
plt.xticks(years[::5], rotation=45, ha='right')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()