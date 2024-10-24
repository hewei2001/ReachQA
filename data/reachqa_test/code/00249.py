import matplotlib.pyplot as plt
import numpy as np

# Data: Carbon Emission Levels (arbitrary units) for each continent from 2000 to 2020
years = np.arange(2000, 2021)

# Carbon emission data for each continent
asia_emissions = [3.5, 3.8, 4.0, 4.3, 4.5, 4.7, 5.0, 5.2, 5.4, 5.6, 6.0, 6.5, 7.0, 7.5, 8.0, 8.3, 8.5, 8.6, 8.9, 9.0, 9.2]
africa_emissions = [1.1, 1.2, 1.3, 1.5, 1.4, 1.3, 1.5, 1.6, 1.8, 1.9, 2.1, 2.0, 2.2, 2.3, 2.4, 2.5, 2.7, 2.8, 2.9, 3.0, 3.2]
europe_emissions = [4.8, 4.7, 4.5, 4.4, 4.3, 4.1, 4.0, 3.9, 3.8, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5]
north_america_emissions = [5.5, 5.6, 5.8, 5.7, 5.5, 5.3, 5.0, 4.9, 4.7, 4.6, 4.4, 4.2, 4.1, 4.0, 3.8, 3.7, 3.6, 3.4, 3.2, 3.0, 2.9]
south_america_emissions = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
australia_emissions = [1.5, 1.6, 1.7, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.5, 2.5, 2.6, 2.7, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3]

emissions_data = [
    asia_emissions,
    africa_emissions,
    europe_emissions,
    north_america_emissions,
    south_america_emissions,
    australia_emissions
]

# Add global trend data (inspired by the given emissions)
global_average_emissions = np.mean(emissions_data, axis=0)

# Define continent labels
continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia']

# Plot settings
fig, ax = plt.subplots(figsize=(14, 8))

# Boxplot with additional mean markers
box = ax.boxplot(emissions_data, labels=continents, notch=True, patch_artist=True,
                 boxprops=dict(facecolor='lightblue', color='darkblue'),
                 whiskerprops=dict(color='darkblue'),
                 capprops=dict(color='darkblue'),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(marker='o', color='black', markersize=5))

# Set colors for each box plot
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB266']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add mean markers
for i in range(len(emissions_data)):
    mean_value = np.mean(emissions_data[i])
    ax.plot(i + 1, mean_value, marker='D', color='purple', markersize=8, label='Mean' if i == 0 else "")

# Inset plot for global trend
ax_inset = ax.inset_axes([0.6, 0.6, 0.35, 0.35])
ax_inset.plot(years, global_average_emissions, color='green', marker='o', label='Global Avg')
ax_inset.set_title('Global Average Trend', fontsize=10)
ax_inset.set_xlabel('Year', fontsize=8)
ax_inset.set_ylabel('Emissions', fontsize=8)
ax_inset.grid(True, linestyle='--', alpha=0.5)
ax_inset.tick_params(axis='both', which='major', labelsize=8)

# Main plot decorations
ax.set_title("Global Carbon Emission Levels by Continent\nAssessing Environmental Impact from 2000 to 2020", fontsize=14, fontweight='bold')
ax.set_xlabel("Continents", fontsize=12)
ax.set_ylabel("Carbon Emissions (Arbitrary Units)", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add a legend for mean markers
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()