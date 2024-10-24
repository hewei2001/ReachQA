import matplotlib.pyplot as plt
import numpy as np

# Years and energy sources
years = ['2010', '2013', '2016', '2019', '2022']
sources = ['Coal', 'Natural Gas', 'Oil', 'Nuclear', 'Renewables']

# Data in terawatt-hours (TWh)
coal = [4200, 4000, 3800, 3600, 3300]
natural_gas = [3000, 3200, 3400, 3600, 3800]
oil = [3800, 3700, 3600, 3500, 3400]
nuclear = [800, 850, 900, 950, 1000]
renewables = [600, 800, 1100, 1500, 2000]

# Calculate total energy and percentage of renewables
total_energy = np.sum([coal, natural_gas, oil, nuclear, renewables], axis=0)
renewable_percent = [r / t * 100 for r, t in zip(renewables, total_energy)]

# Stacked data preparation
energy_data = np.array([coal, natural_gas, oil, nuclear, renewables])

# Plotting the stacked bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))
bottom_values = np.zeros(len(years))

# Define colors for each energy source
colors = ['#8b0000', '#ff6347', '#ff8c00', '#ffd700', '#32cd32']

# Stack bars for each energy source
for i, source in enumerate(sources):
    ax1.bar(years, energy_data[i], bottom=bottom_values, color=colors[i], label=source, alpha=0.85, edgecolor='black')
    bottom_values += energy_data[i]

# Primary axis labels and grid
ax1.set_title('Decade of Transition: Global Energy Consumption\nby Source', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Energy Consumption (TWh)', fontsize=12, fontweight='bold')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Secondary y-axis for percentage of renewables
ax2 = ax1.twinx()
ax2.plot(years, renewable_percent, color='blue', marker='o', linestyle='--', linewidth=2, label='Renewables %')
ax2.set_ylabel('Renewables Share (%)', fontsize=12, fontweight='bold', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Customize legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Annotations with arrows
for i, year in enumerate(years):
    energy_sum = total_energy[i]
    ax1.text(year, energy_sum + 150, f'{energy_sum} TWh', ha='center', fontweight='bold')
    if i > 0:
        ax2.annotate('', xy=(years[i], renewable_percent[i]), xytext=(years[i-1], renewable_percent[i-1]),
                     arrowprops=dict(arrowstyle='->', color='blue'))

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()