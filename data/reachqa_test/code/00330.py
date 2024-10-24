import matplotlib.pyplot as plt
import numpy as np

# Data: Solar and Wind energy production from 2013 to 2023
years = np.arange(2013, 2024)
solar_production = np.array([50, 55, 65, 80, 100, 130, 160, 190, 225, 260, 300])
wind_production = np.array([40, 50, 60, 70, 90, 120, 150, 180, 210, 240, 280])

# Additional Data: Year-over-Year Growth Percentage for Solar and Wind
solar_growth = np.round(((solar_production[1:] - solar_production[:-1]) / solar_production[:-1]) * 100, 2)
wind_growth = np.round(((wind_production[1:] - wind_production[:-1]) / wind_production[:-1]) * 100, 2)

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Line plot for energy production
axs[0].plot(years, solar_production, marker='o', color='gold', linestyle='-', linewidth=2, label='Solar Energy')
axs[0].plot(years, wind_production, marker='s', color='skyblue', linestyle='--', linewidth=2, label='Wind Energy')

# Annotate key milestones on the first subplot
annotations = {
    2015: (solar_production[years.tolist().index(2015)], "Solar Expansion Initiative"),
    2018: (wind_production[years.tolist().index(2018)], "Wind Turbine Upgrade"),
    2023: (solar_production[years.tolist().index(2023)], "Goal Achieved")
}

for year, (y_position, annotation) in annotations.items():
    axs[0].annotate(
        annotation,
        xy=(year, y_position),
        xytext=(0, 15),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='grey'),
        fontsize=10,
        color='darkgreen',
        ha='center'
    )

# Setting titles and labels for subplot 1
axs[0].set_title(
    'Greensville Renewable Energy Production\n2013-2023: Solar and Wind Power Expansion',
    fontsize=14,
    fontweight='bold'
)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Energy Production (MW)', fontsize=12)

# Display value labels on each data point in subplot 1
for year, solar, wind in zip(years, solar_production, wind_production):
    axs[0].text(year, solar + 5, f'{solar}', ha='center', va='bottom', fontsize=9, color='goldenrod')
    axs[0].text(year, wind + 5, f'{wind}', ha='center', va='bottom', fontsize=9, color='steelblue')

# Customize ticks and grid for subplot 1
axs[0].set_xticks(years)
axs[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
axs[0].grid(True, linestyle='--', alpha=0.5)

# Adding a legend for subplot 1
axs[0].legend(loc='upper left', fontsize=10)

# Subplot 2: Bar chart for growth rate
bar_width = 0.35
indices = np.arange(len(solar_growth))

bars1 = axs[1].bar(indices, solar_growth, bar_width, label='Solar Growth (%)', color='coral', alpha=0.7)
bars2 = axs[1].bar(indices + bar_width, wind_growth, bar_width, label='Wind Growth (%)', color='deepskyblue', alpha=0.7)

# Setting titles and labels for subplot 2
axs[1].set_title('Year-over-Year Growth in Renewable Energy Production', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Rate (%)', fontsize=12)
axs[1].set_xticks(indices + bar_width / 2)
axs[1].set_xticklabels(years[1:], rotation=45)

# Adding value labels on top of bars
for bar in bars1:
    axs[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f'{bar.get_height()}%', ha='center', va='bottom', fontsize=9)

for bar in bars2:
    axs[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f'{bar.get_height()}%', ha='center', va='bottom', fontsize=9)

# Adding a legend for subplot 2
axs[1].legend(loc='best', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()