import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Adoption rates (in percentage) for each continent (artificial data)
europe_adoption = [12, 14, 17, 20, 24, 28, 33, 39, 45, 51, 56]
asia_adoption = [5, 7, 9, 12, 16, 20, 23, 27, 31, 34, 38]
africa_adoption = [3, 5, 7, 9, 11, 15, 18, 21, 24, 28, 30]

# Error margins (in percentage points)
europe_errors = [1.5, 1.2, 1.0, 1.3, 1.1, 1.4, 1.6, 1.5, 1.3, 1.2, 1.1]
asia_errors = [1.0, 1.3, 1.2, 1.1, 1.5, 1.7, 1.6, 1.4, 1.3, 1.5, 1.2]
africa_errors = [0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 1.3, 1.4, 1.5, 1.6, 1.2]

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

# Line plot with error bars for Europe
ax.errorbar(years, europe_adoption, yerr=europe_errors, fmt='o-', 
            label='Europe', color='blue', capsize=5, capthick=2, linewidth=2, alpha=0.8)

# Line plot with error bars for Asia
ax.errorbar(years, asia_adoption, yerr=asia_errors, fmt='s-', 
            label='Asia', color='green', capsize=5, capthick=2, linewidth=2, alpha=0.8)

# Line plot with error bars for Africa
ax.errorbar(years, africa_adoption, yerr=africa_errors, fmt='^-', 
            label='Africa', color='orange', capsize=5, capthick=2, linewidth=2, alpha=0.8)

# Title and labels
ax.set_title("Renewable Energy Adoption Rates\nAcross Continents: 2010-2020", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Adoption Rate (%)", fontsize=14)

# Legend
ax.legend(title="Continents", fontsize=12)

# Grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust axes limits to make sure all data is clearly visible
ax.set_xlim(2009, 2021)
ax.set_ylim(0, 60)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()