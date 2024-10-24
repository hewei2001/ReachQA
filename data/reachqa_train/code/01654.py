import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Data preparation
years = np.arange(2010, 2021)
solar_power = np.array([30, 45, 70, 100, 150, 225, 320, 430, 560, 700, 850])
wind_power = np.array([140, 170, 220, 290, 360, 450, 560, 690, 850, 950, 1100])
total_power = solar_power + wind_power
solar_percentage = (solar_power / total_power) * 100
wind_percentage = (wind_power / total_power) * 100

fig, ax = plt.subplots(figsize=(14, 8))

# Plot solar and wind power with gradient-like effect by adjusting alpha
for i in range(len(years)-1):
    ax.plot(years[i:i+2], solar_power[i:i+2], marker='o', linestyle='-', color='#FDB927', linewidth=2, alpha=(i+1)/len(years))
    ax.plot(years[i:i+2], wind_power[i:i+2], marker='^', linestyle='-', color='#0074D9', linewidth=2, alpha=(i+1)/len(years))

# Add shading between the lines
ax.fill_between(years, solar_power, wind_power, color='gray', alpha=0.1)

# Titles and labels
ax.set_title('The Rise of Renewable Energy:\nSolar and Wind Power Trends (2010-2020)', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (TWh)', fontsize=12)

# Customize the x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 1201, 100))

# Add a legend
ax.legend(['Solar Power', 'Wind Power'], title='Energy Source', loc='upper left')

# Annotations for key milestones
ax.annotate('Solar Boom\nBegins', xy=(2014, 150), xytext=(2012, 320),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

ax.annotate('Wind Milestone:\n1,000 TWh', xy=(2020, 1100), xytext=(2018, 1000),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

# Annotate each data point with its value
for i, (y_solar, y_wind) in enumerate(zip(solar_power, wind_power)):
    ax.text(years[i], y_solar + 20, f'{y_solar}', ha='center', fontsize=9, color='#FDB927')
    ax.text(years[i], y_wind + 20, f'{y_wind}', ha='center', fontsize=9, color='#0074D9')

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.7)

# Secondary Y-Axis: Cumulative power generation bar chart
ax2 = ax.twinx()
ax2.bar(years - 0.2, total_power, width=0.4, color='lightgreen', alpha=0.3, label='Total Renewable')
ax2.set_ylabel('Total Energy Generation (TWh)', fontsize=12)
ax2.legend(loc='upper right')

# Inset plot: Percentage share of solar and wind
ax_inset = inset_axes(ax, width="30%", height="30%", loc='lower right', borderpad=2)
ax_inset.plot(years, solar_percentage, color='#FDB927', linewidth=1.5, label='Solar %')
ax_inset.plot(years, wind_percentage, color='#0074D9', linewidth=1.5, label='Wind %')
ax_inset.set_title('Share of Total (%)', fontsize=10)
ax_inset.set_xticks([2010, 2015, 2020])
ax_inset.set_yticks(np.arange(0, 101, 20))
ax_inset.grid(True, linestyle='--', alpha=0.5)
ax_inset.legend(fontsize=8, loc='upper left')

plt.tight_layout()

plt.show()