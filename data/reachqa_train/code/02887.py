import matplotlib.pyplot as plt
import numpy as np

# Original data: Percentage of energy derived from renewable sources over time in different regions
years = np.arange(2010, 2021)
solaria = np.array([10, 15, 20, 30, 40, 50, 60, 65, 70, 72, 75])
windmere = np.array([5, 10, 15, 25, 35, 45, 55, 60, 68, 72, 80])
hydrovania = np.array([20, 22, 25, 27, 30, 32, 33, 35, 38, 40, 42])
geotopia = np.array([3, 5, 7, 10, 14, 18, 22, 25, 30, 35, 40])
biomassia = np.array([8, 10, 12, 20, 25, 30, 35, 38, 40, 42, 45])

# Additional data: Cumulative renewable energy for all regions
cumulative_energy = solaria + windmere + hydrovania + geotopia + biomassia

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Line plots for each region
axs[0].plot(years, solaria, label='Solaria', marker='o', linestyle='-', linewidth=2, color='gold')
axs[0].plot(years, windmere, label='Windmere', marker='s', linestyle='-', linewidth=2, color='skyblue')
axs[0].plot(years, hydrovania, label='Hydrovania', marker='D', linestyle='-', linewidth=2, color='blue')
axs[0].plot(years, geotopia, label='Geotopia', marker='^', linestyle='-', linewidth=2, color='darkred')
axs[0].plot(years, biomassia, label='Biomassia', marker='x', linestyle='-', linewidth=2, color='green')

# Annotations for significant points on the line plots
annotations = {
    (2015, 50): ('Solar Breakthrough', 'gold'),
    (2018, 68): ('Wind Policy Reforms', 'skyblue'),
    (2014, 27): ('Hydro Expansion', 'blue'),
    (2019, 35): ('Geothermal Spike', 'darkred'),
    (2017, 35): ('Biomass Initiatives', 'green')
}
for (x, y), (text, color) in annotations.items():
    axs[0].annotate(text, xy=(x, y), xytext=(x-1, y+10),
                    arrowprops=dict(facecolor=color, shrink=0.05, edgecolor=color),
                    fontsize=9, color=color, backgroundcolor='white')

axs[0].set_title('Renewable Energy Adoption in TerraNova Regions\n(2010-2020)', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Renewable Energy (%)', fontsize=12)
axs[0].set_xticks(years)
axs[0].set_xticklabels(years, rotation=45)
axs[0].set_yticks(np.arange(0, 101, 10))
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', fontsize=10, title='Regions', title_fontsize='12')

# Second subplot: Stacked bar chart for cumulative renewable energy
axs[1].bar(years, solaria, label='Solaria', color='gold')
axs[1].bar(years, windmere, bottom=solaria, label='Windmere', color='skyblue')
axs[1].bar(years, hydrovania, bottom=solaria+windmere, label='Hydrovania', color='blue')
axs[1].bar(years, geotopia, bottom=solaria+windmere+hydrovania, label='Geotopia', color='darkred')
axs[1].bar(years, biomassia, bottom=solaria+windmere+hydrovania+geotopia, label='Biomassia', color='green')

axs[1].set_title('Cumulative Renewable Energy Contributions\n(2010-2020)', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Renewable Energy (%)', fontsize=12)
axs[1].set_xticks(years)
axs[1].set_xticklabels(years, rotation=45)
axs[1].set_yticks(np.arange(0, 301, 50))
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend(loc='upper left', fontsize=10, title='Regions', title_fontsize='12')

# Automatically adjust layout for better readability
plt.tight_layout()

# Show the plot
plt.show()