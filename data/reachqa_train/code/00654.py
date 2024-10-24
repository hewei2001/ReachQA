import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2012, 2022)

# Data: hypothetical energy production values in TWh for each source
solar = np.array([10, 15, 20, 30, 40, 55, 70, 85, 100, 120])
wind = np.array([30, 35, 45, 55, 70, 85, 95, 110, 120, 130])
hydro = np.array([60, 60, 65, 70, 75, 80, 85, 90, 95, 100])
biomass = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 70])

# Stack the data for plotting
data = np.vstack([solar, wind, hydro, biomass])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=['#FFD700', '#1E90FF', '#32CD32', '#8B4513'], alpha=0.8)

# Customize the plot
ax.set_title("Renewable Energy Production by Source\n2012-2021", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, weight='bold')
ax.set_ylabel("Energy Production (TWh)", fontsize=12, weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, title='Energy Source')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Show y-ticks with grid lines for readability
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)} TWh'))
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, rotation=45)
ax.set_yticks(np.arange(0, 301, 50))
ax.set_yticklabels(np.arange(0, 301, 50), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()