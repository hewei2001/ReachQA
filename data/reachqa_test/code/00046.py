import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of EVs (in thousands) from 2010 to 2020
years = np.arange(2010, 2021)
evs_on_road = [5, 7, 9, 15, 30, 75, 120, 200, 350, 500, 650]

# Secondary data: Number of charging stations (in hundreds) from 2010 to 2020
charging_stations = [1, 1, 2, 4, 7, 15, 30, 45, 70, 90, 120]

fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot EVs on road
color_evs = 'royalblue'
ax1.plot(years, evs_on_road, marker='o', linestyle='-', linewidth=2, color=color_evs, label='EVs on Road')
ax1.fill_between(years, evs_on_road, color=color_evs, alpha=0.1)

# Enhance annotations with styled arrows
annotations = {
    2013: "Gov incentives",
    2015: "Affordable long-range EVs",
    2018: "EV infrastructure boom",
    2020: "Consumer awareness"
}

for year, text in annotations.items():
    y_position = evs_on_road[year - 2010] + 50 if year % 2 == 0 else evs_on_road[year - 2010] - 80
    ax1.annotate(
        text,
        xy=(year, evs_on_road[year - 2010]),
        xytext=(year + 0.5, y_position),
        arrowprops=dict(facecolor='darkgrey', arrowstyle="-|>", lw=1.5),
        fontsize=9,
        bbox=dict(facecolor='lightgrey', alpha=0.7, edgecolor='none')
    )

# Add a secondary y-axis for charging stations
ax2 = ax1.twinx()
color_stations = 'seagreen'
ax2.plot(years, charging_stations, marker='s', linestyle='--', linewidth=2, color=color_stations, label='Charging Stations')
ax2.fill_between(years, charging_stations, color=color_stations, alpha=0.1)

# Titles and labels
ax1.set_title('Decade of Change:\nElectric Vehicle Adoption & Infrastructure (2010-2020)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('EVs on Road (thousands)', fontsize=12, color=color_evs)
ax2.set_ylabel('Charging Stations (hundreds)', fontsize=12, color=color_stations)

# Customize x-ticks
ax1.set_xticks(years)

# Grid for better readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Legends
lns1 = ax1.get_lines()
lns2 = ax2.get_lines()
labs1 = [l.get_label() for l in lns1]
labs2 = [l.get_label() for l in lns2]
ax1.legend(lns1 + lns2, labs1 + labs2, loc='upper left', frameon=False, fontsize=10)

# Automatically adjust layout
fig.tight_layout()

# Display the chart
plt.show()