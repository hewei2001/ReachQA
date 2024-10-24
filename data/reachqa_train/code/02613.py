import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Satellite launches per year
asa_launches = [5, 6, 7, 10, 12, 15, 20, 18, 22, 24, 30, 35, 38, 40, 45, 50, 55, 58, 60, 65, 70]
cve_launches = [3, 4, 5, 6, 8, 11, 15, 14, 16, 20, 25, 30, 33, 35, 38, 45, 48, 50, 55, 60, 68]

# Error margins for launches (standard deviation)
asa_errors = [0.5, 0.6, 0.7, 0.8, 1, 1.2, 1.5, 1.7, 2, 2.2, 2.5, 2.7, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.2, 4.5, 5]
cve_errors = [0.4, 0.5, 0.5, 0.6, 0.8, 1, 1.3, 1.5, 1.7, 2, 2.3, 2.5, 2.8, 3, 3.2, 3.4, 3.6, 3.9, 4.1, 4.3, 4.6]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot line charts with error bars
ax.errorbar(years, asa_launches, yerr=asa_errors, label='AetherSpace Agency (ASA)', fmt='-o',
            color='b', capsize=4, linestyle='-', linewidth=2, alpha=0.8)
ax.errorbar(years, cve_launches, yerr=cve_errors, label='CosmicVoyage Enterprises (CVE)', fmt='-s',
            color='g', capsize=4, linestyle='--', linewidth=2, alpha=0.8)

# Title and labels
plt.title('Evolution of Satellite Launch Frequencies\nwith Technology Error Margins (2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Satellite Launches', fontsize=12)

# Legend and Grid
plt.legend(title='Space Agencies', loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Improved axis ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 80, 5))

# Highlight significant developments
significant_years = [2005, 2015]
for year in significant_years:
    ax.axvline(x=year, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.annotate('Tech Milestone', xy=(year, 60), xytext=(year, 65),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, horizontalalignment='center')

# Adjust layout for clarity
plt.tight_layout()

# Show the plot
plt.show()