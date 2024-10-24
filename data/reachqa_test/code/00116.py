import matplotlib.pyplot as plt
import numpy as np

# Time period from 1000 BCE to 1 BCE (in centuries)
years = np.arange(-1000, 1, 100)  # Array representing the centuries

# Literacy rates in percentages for Ancient Egypt, Ancient Greece, and Ancient China
egypt_literacy = np.array([5, 6, 7, 10, 12, 15, 18, 20, 25, 28, 30])
greece_literacy = np.array([4, 5, 9, 15, 20, 25, 30, 35, 38, 40, 45])
china_literacy = np.array([3, 5, 7, 8, 10, 14, 17, 19, 23, 26, 30])

# Hypothetical error margins
egypt_error = np.array([0.5, 0.7, 0.9, 1.0, 1.2, 1.0, 1.3, 1.5, 1.4, 1.6, 1.5])
greece_error = np.array([0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.4, 1.3, 1.5, 1.6, 1.7])
china_error = np.array([0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 1.8])

# Derived data: Hypothetical population estimates (in millions)
population = np.array([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])
egypt_population_literate = egypt_literacy * population / 100
greece_population_literate = greece_literacy * population / 100
china_population_literate = china_literacy * population / 100

# Initialize plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Literacy rates over time
ax1.errorbar(years, egypt_literacy, yerr=egypt_error, label='Ancient Egypt',
             fmt='-o', capsize=5, color='tab:blue', linestyle='-', linewidth=2, alpha=0.8)
ax1.errorbar(years, greece_literacy, yerr=greece_error, label='Ancient Greece',
             fmt='-s', capsize=5, color='tab:green', linestyle='--', linewidth=2, alpha=0.8)
ax1.errorbar(years, china_literacy, yerr=china_error, label='Ancient China',
             fmt='-^', capsize=5, color='tab:red', linestyle=':', linewidth=2, alpha=0.8)
ax1.set_title("The Evolution of Ancient Civilization Literacy\nA Millennium of Change", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Years (BCE)', fontsize=12)
ax1.set_ylabel('Literacy Rate (%)', fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels([-year for year in years], rotation=45)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title="Civilizations", loc='upper left', fontsize=11)

# Second subplot: Population Literate
width = 20
ax2.bar(years - width, egypt_population_literate, width=width, label='Ancient Egypt', color='tab:blue', alpha=0.8)
ax2.bar(years, greece_population_literate, width=width, label='Ancient Greece', color='tab:green', alpha=0.8)
ax2.bar(years + width, china_population_literate, width=width, label='Ancient China', color='tab:red', alpha=0.8)
ax2.set_title("Estimated Literate Population\nby Civilization", fontsize=14, fontweight='bold')
ax2.set_xlabel('Years (BCE)', fontsize=12)
ax2.set_ylabel('Population Literate (Millions)', fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels([-year for year in years], rotation=45)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(title="Civilizations", fontsize=11)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()