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

# Set up the plot
plt.figure(figsize=(12, 6))

# Plot each region with error bars
plt.errorbar(years, solar_installations_na, yerr=errors_na, label='North America', fmt='-o', capsize=4, capthick=1, color='tab:blue', alpha=0.8)
plt.errorbar(years, solar_installations_eu, yerr=errors_eu, label='Europe', fmt='-s', capsize=4, capthick=1, color='tab:green', alpha=0.8)
plt.errorbar(years, solar_installations_asia, yerr=errors_asia, label='Asia', fmt='-^', capsize=4, capthick=1, color='tab:red', alpha=0.8)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Solar Installations (GW)')
plt.title('Adoption of Solar Energy in Different Regions (2000-2020)\nwith Error Margins', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(title='Regions', loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()