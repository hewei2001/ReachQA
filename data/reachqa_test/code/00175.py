import matplotlib.pyplot as plt
import numpy as np

# Expanded Data: Renewable energy sources and their respective installed capacities in 2018 and 2023 projections (in GW)
energy_sources = [
    'Solar Photovoltaic', 'Solar Thermal', 'Wind Onshore', 'Wind Offshore',
    'Hydropower Large', 'Hydropower Small', 'Biomass Solid', 'Biomass Gas', 'Geothermal'
]
installed_capacity_2018 = [420, 50, 560, 30, 800, 250, 80, 40, 10]
installed_capacity_2023 = [710, 70, 620, 60, 900, 300, 120, 60, 15]

# Calculate growth rates
growth_rates = [
    (installed_capacity_2023[i] - installed_capacity_2018[i]) / installed_capacity_2018[i] * 100
    for i in range(len(energy_sources))
]

# Create positions for the bars on the x-axis
x_pos = np.arange(len(energy_sources))

# Create the figure and a set of subplots with shared y-axis
fig, ax1 = plt.subplots(figsize=(15, 9))

# Bar chart for 2023 projected capacities
bars1 = ax1.bar(x_pos - 0.2, installed_capacity_2018, width=0.4, label='2018', color='#FFD700', alpha=0.7)
bars2 = ax1.bar(x_pos + 0.2, installed_capacity_2023, width=0.4, label='2023 Projection', color='#00BFFF', alpha=0.7)

# Annotate each bar with its respective value
for bars, installed_capacities in zip([bars1, bars2], [installed_capacity_2018, installed_capacity_2023]):
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, yval + 15, f'{yval} GW', ha='center', va='bottom', fontsize=9)

# Add line plot for growth rates
ax2 = ax1.twinx()
ax2.plot(x_pos, growth_rates, color='green', marker='o', label='Growth Rate (%)')
for i, txt in enumerate(growth_rates):
    ax2.annotate(f'{txt:.1f}%', (x_pos[i], growth_rates[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

# Add titles and labels
ax1.set_title('Comparison of Global Installed Capacity of Renewable Energy Sources\n'
              'Between 2018 and 2023 Projections with Growth Rates', fontsize=15, fontweight='bold')
ax1.set_xlabel('Energy Source', fontsize=12)
ax1.set_ylabel('Installed Capacity (GW)', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='green')

# Customize x-ticks
ax1.set_xticks(x_pos)
ax1.set_xticklabels(energy_sources, fontsize=10, rotation=30, ha='right')

# Enhance the grid and style
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Add legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the chart
plt.show()