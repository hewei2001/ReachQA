import matplotlib.pyplot as plt
import numpy as np

# Define years for the analysis
years = np.array([2018, 2019, 2020, 2021, 2022])

# Economic contributions (in million USD) for each sector
solar_contribution = np.array([50, 70, 90, 110, 130])
wind_contribution = np.array([40, 60, 85, 95, 105])
hydro_contribution = np.array([45, 50, 55, 60, 65])
biomass_contribution = np.array([25, 30, 35, 40, 45])

# Calculate the total contributions for each year
total_contribution = solar_contribution + wind_contribution + hydro_contribution + biomass_contribution

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the stacked bars
ax1.bar(years, solar_contribution, label='Solar', color='#FDB813', edgecolor='grey', alpha=0.9)
ax1.bar(years, wind_contribution, bottom=solar_contribution, label='Wind', color='#00A86B', edgecolor='grey', alpha=0.9)
ax1.bar(years, hydro_contribution, bottom=solar_contribution + wind_contribution, label='Hydro', color='#1F78B4', edgecolor='grey', alpha=0.9)
ax1.bar(years, biomass_contribution, bottom=solar_contribution + wind_contribution + hydro_contribution, label='Biomass', color='#8B4513', edgecolor='grey', alpha=0.9)

# Create a secondary axis for the line plot
ax2 = ax1.twinx()

# Plot the line chart representing total contribution
ax2.plot(years, total_contribution, color='black', linestyle='-', marker='o', linewidth=2, markersize=8, label='Total Contribution')

# Customize the appearance
ax1.set_title("Economic Contribution of Renewable Energy in GreenVille\n(2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Economic Contribution (Million USD)", fontsize=14)
ax2.set_ylabel("Total Contribution (Million USD)", fontsize=14, color='black')

# Add a combined legend
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left', fontsize=12, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Grid and styling
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Show the plot
plt.show()