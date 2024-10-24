import matplotlib.pyplot as plt
import numpy as np

# Define the years and sectors
years = np.array([2018, 2019, 2020, 2021, 2022])
sectors = ['Residential', 'Commercial', 'Industrial', 'Transportation']

# Define fictional energy consumption data in GWh
energy_consumption = np.array([
    [120, 135, 145, 155, 160],  # Residential
    [200, 215, 225, 235, 240],  # Commercial
    [300, 290, 280, 270, 265],  # Industrial
    [180, 195, 205, 220, 230]   # Transportation
])

# Calculate percentage change for the new subplot
percentage_change = np.diff(energy_consumption, axis=1) / energy_consumption[:, :-1] * 100
# Add zero for the initial year as there's no change from a previous year
percentage_change = np.hstack((np.zeros((percentage_change.shape[0], 1)), percentage_change))

# Colors for each sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Plotting both the stacked bar chart and line chart
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
fig.suptitle("Energy Consumption and Trends in Solar City (2018-2022)\n", fontsize=18)

# First subplot: Stacked Bar Chart
ax1 = axes[0]
bottoms = np.zeros(len(years))

for i, (sector, color) in enumerate(zip(sectors, colors)):
    ax1.bar(years, energy_consumption[i], bottom=bottoms, label=sector, color=color, alpha=0.85)
    bottoms += energy_consumption[i]

ax1.set_title("Energy Consumption by Sector", fontsize=14)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Consumption (GWh)", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)
ax1.set_ylim(0, np.max(bottoms) + 50)

for i, (consumptions, bottom) in enumerate(zip(energy_consumption, np.cumsum(energy_consumption, axis=0))):
    for j, (consumption, b) in enumerate(zip(consumptions, bottom)):
        ax1.text(years[j], b - consumption / 2, f'{consumption}', ha='center', va='center', color='black', fontsize=9)

ax1.legend(title='Sector', title_fontsize=12, fontsize=10, loc='upper right')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Second subplot: Line Plot for Percentage Change
ax2 = axes[1]

for i, (sector, color) in enumerate(zip(sectors, colors)):
    ax2.plot(years, percentage_change[i], marker='o', label=sector, color=color, linestyle='-')

ax2.set_title("Year-over-Year Percentage Change", fontsize=14)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Percentage Change (%)", fontsize=12)
ax2.axhline(0, color='grey', linewidth=0.8, linestyle='--')
ax2.legend(title='Sector', title_fontsize=12, fontsize=10, loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()