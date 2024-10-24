import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Solar energy production data in gigawatts (GW) for five cities
san_francisco = np.array([1.0, 1.2, 1.5, 1.9, 2.3, 3.0, 3.7, 4.5, 5.5, 6.8, 7.5])
berlin = np.array([0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.1, 3.8, 4.2, 4.9, 5.3])
tokyo = np.array([2.5, 2.8, 3.2, 3.6, 4.0, 4.5, 5.0, 5.7, 6.3, 7.0, 7.8])
sydney = np.array([0.9, 1.1, 1.3, 1.6, 2.1, 2.7, 3.4, 4.0, 4.7, 5.4, 6.0])
cape_town = np.array([0.5, 0.6, 0.8, 1.0, 1.3, 1.6, 2.0, 2.5, 3.0, 3.6, 4.2])

# Calculating percentage changes for a secondary y-axis
sf_percentage_change = 100 * np.diff(san_francisco) / san_francisco[:-1]
sf_percentage_change = np.insert(sf_percentage_change, 0, 0)  # No change in the first year

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plotting each city's data with distinct styles
ax1.plot(years, san_francisco, label='San Francisco', marker='o', linestyle='-', linewidth=2, color='b')
ax1.plot(years, berlin, label='Berlin', marker='s', linestyle='--', linewidth=2, color='g')
ax1.plot(years, tokyo, label='Tokyo', marker='^', linestyle='-.', linewidth=2, color='r')
ax1.plot(years, sydney, label='Sydney', marker='D', linestyle=':', linewidth=2, color='c')
ax1.plot(years, cape_town, label='Cape Town', marker='x', linestyle='-', linewidth=2, color='m')

# Adding a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, sf_percentage_change, color='tab:orange', linestyle='--', linewidth=2, label='SF % Change')
ax2.set_ylabel('Percentage Change in SF (%)', fontsize=12, color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Title and labels
ax1.set_title('Decadal Growth in Solar Energy Production\nAcross Major Cities', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Solar Energy Production (GW)', fontsize=12)
ax1.set_xticks(years)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Adding a legend
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Adding grid lines
ax1.grid(True, linestyle='--', alpha=0.6)

# Annotate maximum value
max_value = np.max(san_francisco)
max_year = years[np.argmax(san_francisco)]
ax1.annotate(f'Max: {max_value:.1f} GW', xy=(max_year, max_value), xytext=(max_year-2, max_value+1),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()