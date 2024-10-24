import matplotlib.pyplot as plt
import numpy as np

# Extended timeline from 2050 to 2100
years = np.arange(2050, 2101)

# Constructing a more complex dataset with nonlinear growth patterns
solar = np.clip(20 + 30 * np.sin(np.linspace(0, 3 * np.pi, len(years))), 0, 60)
wind = np.clip(10 + np.cumsum(np.linspace(0.5, 0.6, len(years))), 0, 50)
hydro = np.clip(50 - np.cumsum(np.linspace(0.5, 0.7, len(years))), 0, 60)
biomass = np.clip(30 - np.cumsum(np.linspace(0.2, 0.4, len(years))), 0, 30)
geothermal = np.clip(5 + np.cumsum(np.linspace(0.1, 0.3, len(years))), 0, 20)
tidal = np.clip(2 * np.sin(np.linspace(0, 2 * np.pi, len(years))), 0, 10)

# Stack the data
energy_sources = np.vstack([solar, wind, hydro, biomass, geothermal, tidal])

# Define colors for each energy source
colors = ['#ffcc00', '#66ccff', '#009933', '#996600', '#ff6600', '#0066cc']

# Set up the figure
plt.figure(figsize=(16, 10))

# Plot the stacked area chart
plt.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal', 'Tidal'], colors=colors, alpha=0.8)

# Titles and labels
plt.title('Renewable Energy Generation: 2050-2100\nFuturistic City X Energy Projection', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Generation (%)', fontsize=12)

# Add a legend outside the plot
plt.legend(loc='upper left', title='Energy Sources', bbox_to_anchor=(1.05, 1), fontsize=10)

# Customize the plot grid
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(np.arange(2050, 2101, 5), rotation=45)

# Annotate significant transitions or events
plt.annotate('Hydro Decline', xy=(2065, hydro[15]), xytext=(2070, 40),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkred', fontweight='bold')

plt.annotate('Introduction of Tidal Energy', xy=(2080, tidal[30]), xytext=(2085, 7),
             arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
             fontsize=10, color='navy', fontweight='bold')

# Normalize and adjust layout for better presentation
plt.tight_layout()

# Display the chart
plt.show()