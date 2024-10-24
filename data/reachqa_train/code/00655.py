import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

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
fig, ax = plt.subplots(figsize=(14, 10))

# Gradient color scheme using colormap
colors = cm.get_cmap('viridis', 4)
ax.stackplot(years, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors(np.linspace(0.2, 0.8, 4)), alpha=0.8)

# Add trendlines for each energy source
for idx, y in enumerate(data):
    ax.plot(years, np.cumsum(y), color=colors(idx/3), lw=2, ls='--')

# Customize the plot
ax.set_title("Renewable Energy Production by Source\n2012-2021", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, weight='bold')
ax.set_ylabel("Energy Production (TWh)", fontsize=12, weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, title='Energy Source')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight significant year with a vertical line
ax.axvline(x=2018, color='grey', linestyle='--', lw=1)
ax.annotate("Notable Increase in Solar", xy=(2018, 200), xytext=(2015.5, 250), 
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkred')

# Y-axis customization
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)} TWh'))
ax.set_yticks(np.arange(0, 301, 50))
ax.set_yticklabels(np.arange(0, 301, 50), fontsize=10)

# X-axis customization
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10, rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()