import matplotlib.pyplot as plt
import numpy as np

# Years for plotting
years = np.arange(2030, 2040)

# Hypothetical data: Number of tourists in thousands for each exoplanet
planet_a_tourists = [20, 22, 27, 35, 40, 43, 45, 50, 56, 65]
planet_b_tourists = [15, 18, 21, 26, 30, 32, 37, 40, 44, 50]
planet_c_tourists = [10, 12, 15, 19, 23, 28, 31, 35, 38, 42]
planet_d_tourists = [8, 10, 12, 15, 20, 24, 27, 30, 33, 38]
planet_e_tourists = [5, 7, 10, 12, 16, 18, 21, 25, 28, 30]

# Error margins in thousands, simulating uncertainty
planet_a_errors = [2, 2, 3, 3, 4, 3, 3, 4, 4, 5]
planet_b_errors = [1.5, 1.8, 2, 2.5, 3, 2.5, 3, 3.5, 3, 4]
planet_c_errors = [1, 1.2, 1.5, 1.8, 2, 2.8, 3, 3.2, 3.5, 4]
planet_d_errors = [0.8, 1, 1.2, 1.5, 1.8, 2.4, 2.7, 3, 3.3, 3.8]
planet_e_errors = [0.5, 0.7, 1, 1.2, 1.6, 1.8, 2.1, 2.5, 2.8, 3]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each exoplanet's data with error bars
ax.errorbar(years, planet_a_tourists, yerr=planet_a_errors, label='Planet A', fmt='-o', capsize=5, color='#FF5733', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_b_tourists, yerr=planet_b_errors, label='Planet B', fmt='-s', capsize=5, color='#33FFCE', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_c_tourists, yerr=planet_c_errors, label='Planet C', fmt='-^', capsize=5, color='#335BFF', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_d_tourists, yerr=planet_d_errors, label='Planet D', fmt='-D', capsize=5, color='#FF33A6', linewidth=2, alpha=0.8)
ax.errorbar(years, planet_e_tourists, yerr=planet_e_errors, label='Planet E', fmt='-p', capsize=5, color='#FFD700', linewidth=2, alpha=0.8)

# Customize the plot
ax.set_title('Annual Growth in Galactic Tourism:\nExploring Space Travel Enthusiasm', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Tourists (in thousands)', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Add legend
ax.legend(title='Exoplanets', title_fontsize='13', fontsize='11', loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()