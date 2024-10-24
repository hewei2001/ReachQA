import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data for each type of green space (in hectares)
parks = np.array([100, 102, 105, 108, 112, 115, 120, 125, 130, 135, 140])
community_gardens = np.array([20, 22, 25, 28, 32, 35, 39, 43, 47, 50, 55])
rooftop_gardens = np.array([5, 7, 10, 13, 17, 22, 28, 35, 43, 52, 60])
urban_forests = np.array([40, 42, 43, 45, 48, 50, 53, 57, 60, 63, 67])

# Calculate total green space area
total_area = parks + community_gardens + rooftop_gardens + urban_forests

# Investment data for green spaces (in million dollars)
investments = np.array([10, 12, 14, 18, 22, 25, 30, 40, 55, 70, 85])

# Create figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot stacked area chart
ax1.stackplot(years, parks, community_gardens, rooftop_gardens, urban_forests,
              labels=['Parks', 'Community Gardens', 'Rooftop Gardens', 'Urban Forests'],
              colors=['#81c784', '#aed581', '#c5e1a5', '#dcedc8'], alpha=0.85)

# Title and labels for primary axis
ax1.set_title('Greening Metropolis: Evolution of Urban Green Spaces and Investments\n(2010-2020)', 
              fontsize=18, fontweight='bold', loc='center')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Area (Hectares)', fontsize=14)

# Add grid
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)

# Create secondary axis for investment data
ax2 = ax1.twinx()
ax2.plot(years, investments, label='Investments (Million $)', color='crimson', linestyle='--', marker='o')
ax2.set_ylabel('Investment (Million $)', fontsize=14)

# Add legend for both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', title='Types of Green Spaces & Investment', fontsize=12, frameon=False)

# Rotating x-axis labels
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Annotations for key trends
ax1.annotate('Rapid Growth\nof Rooftop Gardens', xy=(2018, 225), xytext=(2015, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')
ax1.annotate('Steady Expansion\nof Urban Forests', xy=(2020, 320), xytext=(2016, 330),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')
ax2.annotate('Surge in Investments', xy=(2019, 70), xytext=(2016, 80),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=12, ha='center', color='crimson')

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()