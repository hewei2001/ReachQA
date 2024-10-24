import matplotlib.pyplot as plt
import numpy as np

# Define the years and regions
years = np.arange(2000, 2021)
regions = ['North America', 'Europe', 'Asia']

# Create data for solar installations in gigawatts (GW)
solar_installations_na = np.array([0.5, 0.6, 0.8, 1.0, 1.4, 2.0, 2.8, 3.5, 4.2, 5.0, 6.5, 8.0, 10.0, 12.5, 15.0, 18.0, 21.0, 25.0, 30.0, 35.0, 40.0])
solar_installations_eu = np.array([0.6, 0.8, 1.2, 1.5, 2.0, 2.8, 3.8, 4.8, 5.8, 7.0, 9.0, 12.0, 15.0, 19.0, 22.0, 26.0, 30.0, 35.0, 41.0, 48.0, 55.0])
solar_installations_asia = np.array([0.4, 0.7, 1.0, 1.4, 1.9, 2.6, 3.4, 4.6, 5.5, 7.0, 9.5, 12.5, 17.0, 22.0, 28.0, 35.0, 44.0, 54.0, 66.0, 80.0, 95.0])

# Define errors for each region
errors_na = np.array([0.3 for _ in range(len(years))])
errors_eu = np.array([0.5 for _ in range(len(years))])
errors_asia = np.array([0.7 for _ in range(len(years))])

# Calculate cumulative installations for stacked bar chart
cumulative_na = np.cumsum(solar_installations_na)
cumulative_eu = np.cumsum(solar_installations_eu)
cumulative_asia = np.cumsum(solar_installations_asia)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

# Plot 1: Line plot with error bars
ax1.errorbar(years, solar_installations_na, yerr=errors_na, label='North America', fmt='-o', capsize=4, capthick=1, color='tab:blue', alpha=0.8)
ax1.errorbar(years, solar_installations_eu, yerr=errors_eu, label='Europe', fmt='-s', capsize=4, capthick=1, color='tab:green', alpha=0.8)
ax1.errorbar(years, solar_installations_asia, yerr=errors_asia, label='Asia', fmt='-^', capsize=4, capthick=1, color='tab:red', alpha=0.8)
ax1.set_xlabel('Year')
ax1.set_ylabel('Solar Installations (GW)')
ax1.set_title('Adoption of Solar Energy in Different Regions (2000-2020)\nwith Error Margins', fontsize=14, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title='Regions', loc='upper left')

# Plot 2: Stacked bar chart for cumulative installations
ax2.bar(years, cumulative_na, label='North America', color='tab:blue', alpha=0.7)
ax2.bar(years, cumulative_eu, bottom=cumulative_na, label='Europe', color='tab:green', alpha=0.7)
ax2.bar(years, cumulative_asia, bottom=cumulative_na + cumulative_eu, label='Asia', color='tab:red', alpha=0.7)
ax2.set_xlabel('Year')
ax2.set_ylabel('Cumulative Installations (GW)')
ax2.set_title('Cumulative Solar Installations by Year', fontsize=14, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(title='Regions', loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()