import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2025
years = np.arange(2010, 2026)

# Hypothetical data: Adoption rates in percentage for different energy sources
solar_adoption = np.array([2, 3, 5, 7, 10, 13, 17, 21, 25, 30, 34, 38, 43, 47, 52, 58])
wind_adoption = np.array([1, 2, 3, 5, 7, 9, 12, 15, 19, 23, 27, 30, 34, 37, 40, 43])
hydro_adoption = np.array([4, 5, 7, 9, 12, 15, 18, 21, 25, 28, 31, 34, 37, 40, 43, 46])

# Error margins
solar_error = np.array([0.5, 0.6, 0.7, 0.8, 1.0, 1.1, 1.3, 1.5, 1.6, 1.8, 1.9, 2.0, 2.2, 2.3, 2.4, 2.5])
wind_error = np.array([0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.1, 1.3, 1.5, 1.6, 1.7, 1.9, 2.0, 2.2, 2.3, 2.5])
hydro_error = np.array([0.4, 0.5, 0.6, 0.8, 0.9, 1.0, 1.2, 1.3, 1.5, 1.6, 1.7, 1.8, 2.0, 2.1, 2.2, 2.3])

# Cumulative adoption rates for stacked area chart
cumulative_adoption = np.vstack((solar_adoption, wind_adoption, hydro_adoption))

# Set up the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Line chart with error bars
ax1.errorbar(years, solar_adoption, yerr=solar_error, label='Solar Energy', fmt='-o', color='orange', capsize=5, alpha=0.7)
ax1.errorbar(years, wind_adoption, yerr=wind_error, label='Wind Energy', fmt='-s', color='green', capsize=5, alpha=0.7)
ax1.errorbar(years, hydro_adoption, yerr=hydro_error, label='Hydro Power', fmt='-^', color='blue', capsize=5, alpha=0.7)

ax1.set_title("Renewable Energy Adoption Rates\nwith Error Margins (2010-2025)", fontsize=14, fontweight='bold', loc='center')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Adoption Rate (%)", fontsize=12)
ax1.legend(title="Energy Source", fontsize=10, loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(2010, 2025)
ax1.set_ylim(0, 60)
ax1.annotate('Govt. Incentives\nBoost', xy=(2018, 30), xytext=(2013, 40),
             arrowprops=dict(facecolor='darkred', shrink=0.05, width=1.5),
             fontsize=10, ha='center', color='darkred', bbox=dict(boxstyle="round", fc="w", ec="k", lw=0.5))

# Second subplot: Stacked area chart
ax2.stackplot(years, cumulative_adoption, labels=['Solar', 'Wind', 'Hydro'], colors=['orange', 'green', 'blue'], alpha=0.5)

ax2.set_title("Cumulative Renewable Energy Adoption\n(2010-2025)", fontsize=14, fontweight='bold', loc='center')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Cumulative Adoption Rate (%)", fontsize=12)
ax2.legend(title="Energy Source", fontsize=10, loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xlim(2010, 2025)
ax2.set_ylim(0, 150)

plt.tight_layout()
plt.show()