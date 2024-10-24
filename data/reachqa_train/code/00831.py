import matplotlib.pyplot as plt
import numpy as np

# Extended time range for the plot
years = np.arange(2010, 2026)

# Fictional data for the number of breweries in each region over the extended period
northland = np.array([80, 90, 100, 110, 125, 140, 155, 170, 185, 200, 215, 230, 245, 260, 275, 290])
eastwood = np.array([60, 65, 75, 85, 100, 115, 130, 145, 160, 170, 180, 190, 200, 210, 220, 230])
westlake = np.array([50, 55, 60, 70, 85, 95, 110, 125, 135, 145, 155, 165, 175, 185, 195, 205])
south_valley = np.array([40, 50, 55, 65, 75, 85, 95, 110, 120, 130, 140, 150, 160, 170, 180, 190])
central_plains = np.array([30, 35, 45, 55, 65, 75, 85, 100, 110, 120, 130, 140, 150, 160, 170, 180])

# Error margins representing uncertainty or variance in the data
errors = {
    'northland': np.array([6, 5, 7, 6, 8, 7, 6, 5, 7, 6, 5, 7, 6, 5, 7, 6]),
    'eastwood': np.array([5, 4, 5, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]),
    'westlake': np.array([4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]),
    'south_valley': np.array([3, 3, 4, 5, 3, 3, 4, 5, 3, 3, 4, 5, 3, 3, 4, 5]),
    'central_plains': np.array([2, 2, 3, 4, 3, 4, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3])
}

# Calculate CAGR
def calculate_cagr(start, end, periods):
    return (end / start) ** (1 / periods) - 1

cagr_northland = calculate_cagr(northland[0], northland[-1], len(years))
cagr_eastwood = calculate_cagr(eastwood[0], eastwood[-1], len(years))

# Figure and subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 12))

# Main plot: Number of Breweries
ax[0].errorbar(years, northland, yerr=errors['northland'], label='Northland', fmt='-o', capsize=5, color='tab:blue', alpha=0.8)
ax[0].errorbar(years, eastwood, yerr=errors['eastwood'], label='Eastwood', fmt='-^', capsize=5, color='tab:orange', alpha=0.8)
ax[0].errorbar(years, westlake, yerr=errors['westlake'], label='Westlake', fmt='-s', capsize=5, color='tab:green', alpha=0.8)
ax[0].errorbar(years, south_valley, yerr=errors['south_valley'], label='South Valley', fmt='-d', capsize=5, color='tab:red', alpha=0.8)
ax[0].errorbar(years, central_plains, yerr=errors['central_plains'], label='Central Plains', fmt='-x', capsize=5, color='tab:purple', alpha=0.8)

# Title and labels
ax[0].set_title('Growth of Breweries in Various Regions (2010-2025)', fontsize=16, fontweight='bold', ha='center')
ax[0].set_xlabel('Year', fontsize=14)
ax[0].set_ylabel('Number of Breweries', fontsize=14)
ax[0].legend(title='Regions', loc='upper left')
ax[0].grid(True, linestyle='--', alpha=0.7)

# Annotations
ax[0].annotate(f'Northland CAGR: {cagr_northland:.2%}', xy=(2020, 215), fontsize=10, color='tab:blue')
ax[0].annotate(f'Eastwood CAGR: {cagr_eastwood:.2%}', xy=(2020, 170), fontsize=10, color='tab:orange')

# Subplot: Normalized Growth
normalized_northland = northland / northland[0]
normalized_eastwood = eastwood / eastwood[0]

ax[1].plot(years, normalized_northland, label='Northland', color='tab:blue', linestyle='--')
ax[1].plot(years, normalized_eastwood, label='Eastwood', color='tab:orange', linestyle='--')
ax[1].set_title('Normalized Growth of Breweries (Relative to 2010)', fontsize=14)
ax[1].set_xlabel('Year', fontsize=14)
ax[1].set_ylabel('Normalized Growth', fontsize=14)
ax[1].legend(loc='upper left')
ax[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()