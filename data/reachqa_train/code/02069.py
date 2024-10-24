import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2010, 2021)
solar_energy = np.array([2, 3, 5, 8, 12, 20, 30, 45, 60, 80, 95])
wind_energy = np.array([4, 6, 8, 12, 18, 25, 30, 35, 40, 45, 50])
hydro_energy = np.array([10, 10, 11, 12, 13, 15, 18, 21, 24, 28, 30])
geothermal_energy = np.array([1, 1, 2, 3, 5, 7, 9, 11, 13, 14, 15])

# Stack the data for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], 
             colors=['#FFD700', '#87CEEB', '#3CB371', '#FF6347'], alpha=0.75)

# Customize the chart with title and labels
ax.set_title('Renewable Energy Adoption Trends in Greenlandia\nFrom 2010 to 2020', fontsize=16, weight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Energy Output (TWh)', fontsize=12, weight='bold')

# Highlight specific years with vertical lines
highlight_years = [2015, 2020]
for year in highlight_years:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1)

# Annotate significant points
ax.annotate('Paris Agreement\n(2015)', xy=(2015, 65), xytext=(2013, 80),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Adding grid for better readability
ax.grid(visible=True, linestyle='--', alpha=0.6)

# Rotate x-axis labels for better readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Sources', fontsize=11, shadow=True)

# Add data points markers
for y, color in zip(energy_data, ['#FFD700', '#87CEEB', '#3CB371', '#FF6347']):
    ax.plot(years, y, marker='o', markersize=4, color=color, linestyle='None', alpha=0.9)

# Create an additional subplot for yearly growth rates
growth_rate = np.diff(energy_data, axis=1)
avg_growth_rate = np.mean(growth_rate, axis=0)

ax_growth = ax.twinx()
ax_growth.plot(years[1:], avg_growth_rate, color='black', linestyle='--', marker='x', label='Avg Growth Rate')
ax_growth.set_ylabel('Avg Growth Rate (TWh/year)', fontsize=12, weight='bold')
ax_growth.set_ylim(0, max(avg_growth_rate) * 1.2)

# Tight layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()