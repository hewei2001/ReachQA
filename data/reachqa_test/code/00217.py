import matplotlib.pyplot as plt
import numpy as np

# Define years from 2015 to 2025
years = np.arange(2015, 2026)

# Electric vehicle adoption rates (%) over the years (fictitious data)
ev_adoption_rate = np.array([2, 3, 5, 7, 11, 15, 20, 25, 33, 40, 50])

# Charging infrastructure growth (stations in thousands)
charging_stations = np.array([10, 12, 15, 19, 25, 35, 47, 63, 80, 100, 130])

# Error margins representing uncertainties
ev_adoption_error = np.array([0.5, 0.6, 0.8, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
charging_error = np.array([1, 1.2, 1.5, 1.8, 2.2, 2.5, 3, 3.5, 4, 4.5, 5])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set color palette
color_ev = 'tab:blue'
color_cs = 'tab:green'

# Plot EV adoption rates with error bars
ax1.errorbar(years, ev_adoption_rate, yerr=ev_adoption_error, label='EV Adoption Rate (%)',
             fmt='o-', color=color_ev, ecolor='lightblue', elinewidth=1.5, capsize=3, alpha=0.8)
ax1.fill_between(years, ev_adoption_rate - ev_adoption_error, ev_adoption_rate + ev_adoption_error,
                 color=color_ev, alpha=0.1)

# Customize first y-axis
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('EV Adoption Rate (%)', color=color_ev, fontsize=12)
ax1.tick_params(axis='y', labelcolor=color_ev)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')

# Create a second y-axis for charging stations
ax2 = ax1.twinx()
ax2.errorbar(years, charging_stations, yerr=charging_error, label='Charging Stations (k)',
             fmt='s--', color=color_cs, ecolor='lightgreen', elinewidth=1.5, capsize=3, alpha=0.8)
ax2.fill_between(years, charging_stations - charging_error, charging_stations + charging_error,
                 color=color_cs, alpha=0.1)

# Customize second y-axis
ax2.set_ylabel('Charging Stations (k)', color=color_cs, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color_cs)

# Adding title with a line break
plt.title('EV Adoption and Charging Infrastructure Growth (2015-2025)\nTracking Sustainable Transportation Trends', 
          fontsize=14, fontweight='bold')

# Enhanced grid
ax1.grid(True, linestyle='--', alpha=0.6)

# Adding legends
fig.legend(loc='upper left', bbox_to_anchor=(0.15, 0.85), fontsize=10, frameon=True)

# Subplot for milestone annotations
important_years = [2018, 2022]
important_ev_rates = ev_adoption_rate[np.isin(years, important_years)]
for i, year in enumerate(important_years):
    ax1.annotate(f'{year}\n{important_ev_rates[i]}%', 
                 xy=(year, important_ev_rates[i]), 
                 xytext=(year, important_ev_rates[i] + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, ha='center')

# Adjust layout
fig.tight_layout()

# Show the plot
plt.show()