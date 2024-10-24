import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2012, 2022)

# Hypothetical energy production in TWh by source over the years
solar = np.array([100, 120, 150, 190, 240, 300, 360, 430, 510, 600])
wind = np.array([200, 230, 270, 320, 380, 450, 530, 620, 710, 810])
hydro = np.array([1000, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100])
geothermal = np.array([50, 52, 55, 58, 62, 67, 73, 80, 88, 97])
biomass = np.array([75, 80, 88, 95, 105, 118, 130, 143, 157, 172])

# Stacking the energy data
energy_sources = np.vstack([solar, wind, hydro, geothermal, biomass])

# Colors for each energy source
colors = ['#FFD700', '#00BFFF', '#1E90FF', '#FF6347', '#32CD32']

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Create a stacked area chart
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], colors=colors, alpha=0.8)

# Adding title and labels
ax.set_title('Trends in Global Renewable Energy Production\n(2012-2021)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TWh)', fontsize=14)

# Adding legend
ax.legend(loc='upper left', title='Energy Source', fontsize=12)

# Customizing the x-ticks for better readability
ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], fontsize=12)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to ensure no overlapping elements
plt.tight_layout()

# Display the plot
plt.show()