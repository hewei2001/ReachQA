import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = np.arange(2050, 2060)

# Data for each renewable energy source (in percentage)
solar = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
wind = [5, 10, 15, 20, 25, 30, 32, 34, 35, 36]
hydro = [60, 55, 50, 45, 40, 35, 30, 25, 20, 15]
biomass = [25, 20, 15, 10, 5, 0, 0, 0, 0, 0]

# Stack the data
energy_sources = np.vstack([solar, wind, hydro, biomass])

# Define colors for each energy source
colors = ['#ffcc00', '#66ccff', '#009933', '#996600']

# Set up the figure
plt.figure(figsize=(14, 8))

# Plot the stacked area chart
plt.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Title and labels
plt.title('Renewable Energy Generation Over a Decade\nin Futuristic City X (2050-2059)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Generation (%)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Energy Sources', bbox_to_anchor=(1, 1), fontsize=10)

# Customize the plot grid
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Annotate a significant transition
plt.annotate('Biomass phase-out', xy=(2054, biomass[4]), xytext=(2055, 10),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkred', fontweight='bold')

# Adjust the layout for better presentation
plt.tight_layout()

# Display the chart
plt.show()