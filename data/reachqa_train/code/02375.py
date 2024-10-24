import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Percentage contribution of each renewable energy type
solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

# Total energy generation capacity (in gigawatts)
total_capacity = [45, 47, 50, 58, 64, 72, 90, 105, 126, 140, 160]

# Plot configuration
fig, ax1 = plt.subplots(figsize=(12, 8))

# Line plots for percentage contributions
ax1.plot(years, solar_power, marker='o', linestyle='-', color='#FFA07A', linewidth=2, label='Solar Power (%)')
ax1.plot(years, wind_energy, marker='^', linestyle='--', color='#6495ED', linewidth=2, label='Wind Energy (%)')
ax1.plot(years, hydroelectric_power, marker='s', linestyle='-.', color='#90EE90', linewidth=2, label='Hydroelectric Power (%)')

# Secondary y-axis for total capacity
ax2 = ax1.twinx()
ax2.fill_between(years, total_capacity, color='#D3D3D3', alpha=0.3, label='Total Capacity (GW)')

# Annotations for key milestones
annotations = {
    2012: ("Solar Surge\nTech Breakthrough", solar_power[2]),
    2016: ("Wind Energy\nMajor Project", wind_energy[6]),
    2020: ("Hydro\nEfficiency Boost", hydroelectric_power[10])
}

for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 3),
                 arrowprops=dict(facecolor='gray', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='center')

# Title and axis labels
plt.title('Growth of Renewable Energy Sources (2010-2020)\nwith Total Capacity Overlay', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage Contribution (%)', fontsize=12)
ax2.set_ylabel('Total Energy Generation Capacity (GW)', fontsize=12)

# Legends
ax1.legend(loc='upper left', fontsize=10, title='Energy Source')
ax2.legend(loc='upper right', fontsize=10, title='Energy Capacity')

# X-ticks customization
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()