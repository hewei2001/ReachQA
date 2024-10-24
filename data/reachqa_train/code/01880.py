import matplotlib.pyplot as plt
import numpy as np

# Define states and data for the current year
states = ['California', 'Texas', 'New York', 'Florida', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
solar_energy = [25, 15, 10, 20, 18, 12, 22, 16, 14]
wind_energy = [15, 30, 12, 10, 25, 20, 18, 21, 17]
hydro_energy = [12, 5, 15, 5, 10, 8, 6, 7, 5]
geothermal_energy = [8, 3, 5, 2, 4, 6, 4, 3, 3]
biomass_energy = [10, 7, 8, 9, 6, 5, 7, 5, 6]

# Define bar width and positions
width = 0.6
ind = np.arange(len(states))

# Create figure and main plot
fig, ax = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [3, 2]})

# Stacked bar chart for current year
ax[0].bar(ind, solar_energy, width, label='Solar', color='goldenrod', edgecolor='black')
ax[0].bar(ind, wind_energy, width, label='Wind', color='skyblue', edgecolor='black', bottom=solar_energy)
ax[0].bar(ind, hydro_energy, width, label='Hydroelectric', color='seagreen', edgecolor='black', 
          bottom=np.array(solar_energy) + np.array(wind_energy))
ax[0].bar(ind, geothermal_energy, width, label='Geothermal', color='tomato', edgecolor='black',
          bottom=np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy))
ax[0].bar(ind, biomass_energy, width, label='Biomass', color='purple', edgecolor='black',
          bottom=np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy) + np.array(geothermal_energy))

# Annotate total on top of stacks
for i, (s, w, h, g, b) in enumerate(zip(solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy)):
    total = s + w + h + g + b
    ax[0].text(i, total + 1, f"{total}%", ha='center', va='bottom', fontsize=9, fontweight='bold')

# Title and labels for main plot
ax[0].set_title('Comprehensive Renewable Energy Adoption\nin U.S. States (2023)', fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel('Percentage of Total Energy Consumption', fontsize=12, labelpad=10)
ax[0].set_xticks(ind)
ax[0].set_xticklabels(states, fontsize=10, rotation=45, ha='right')
ax[0].legend(title='Energy Source', fontsize=10, title_fontsize=12)
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Subplot: Trend over previous years for California
years = np.array([2020, 2021, 2022, 2023])
solar_trend = np.array([20, 21, 24, 25])
wind_trend = np.array([13, 14, 15, 15])
hydro_trend = np.array([10, 11, 12, 12])

ax[1].plot(years, solar_trend, '-o', label='Solar', color='goldenrod')
ax[1].plot(years, wind_trend, '-o', label='Wind', color='skyblue')
ax[1].plot(years, hydro_trend, '-o', label='Hydroelectric', color='seagreen')

# Title and labels for subplot
ax[1].set_title('Energy Adoption Trends Over Time in California', fontsize=14, fontweight='bold', pad=15)
ax[1].set_xlabel('Year', fontsize=12, labelpad=10)
ax[1].set_ylabel('Percentage of Total Energy Consumption', fontsize=12, labelpad=10)
ax[1].legend(fontsize=10)
ax[1].grid(linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()