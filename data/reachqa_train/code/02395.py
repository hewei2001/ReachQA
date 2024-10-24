import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for each type of green space (in hectares)
parks = np.array([100, 102, 105, 108, 112, 115, 120, 125, 130, 135, 140])
community_gardens = np.array([20, 22, 25, 28, 32, 35, 39, 43, 47, 50, 55])
rooftop_gardens = np.array([5, 7, 10, 13, 17, 22, 28, 35, 43, 52, 60])
urban_forests = np.array([40, 42, 43, 45, 48, 50, 53, 57, 60, 63, 67])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the stacked area chart
ax.stackplot(years, parks, community_gardens, rooftop_gardens, urban_forests,
             labels=['Parks', 'Community Gardens', 'Rooftop Gardens', 'Urban Forests'],
             colors=['#81c784', '#aed581', '#c5e1a5', '#dcedc8'], alpha=0.85)

# Title and labels
ax.set_title('Greening Metropolis: Evolution of Urban Green Spaces\n(2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Area (Hectares)', fontsize=14)

# Grid lines for better readability
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Adding legend
ax.legend(loc='upper left', title='Types of Green Spaces', fontsize=12, frameon=False)

# Rotating x-axis labels to prevent overlap
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

# Annotations for key trends
ax.annotate('Rapid Growth\nof Rooftop Gardens', xy=(2018, 225), xytext=(2015, 250),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')
ax.annotate('Steady Expansion\nof Urban Forests', xy=(2020, 320), xytext=(2016, 330),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Automatically adjust the layout to avoid overlaps
plt.tight_layout()

# Show the plot
plt.show()