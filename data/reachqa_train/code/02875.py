import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data for the chart
countries = ['Germany', 'China', 'United States', 'India', 'Brazil', 'United Kingdom', 'Australia', 'France', 'Canada', 'Japan']
installed_capacity = [150, 1200, 1000, 800, 600, 300, 200, 250, 400, 500]  # in Gigawatts
populations = [83, 1393, 331, 1380, 213, 68, 26, 65, 38, 125]  # in millions

fig, ax1 = plt.subplots(figsize=(14, 8))

# Create a color gradient based on installed capacity
bar_colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(countries)))
bars = ax1.barh(countries, installed_capacity, color=bar_colors, edgecolor='black')

# Customizing primary y-axis and labels
ax1.set_xlabel('Installed Capacity (Gigawatts)', fontsize=12)
ax1.set_title('Global Leadership in Renewable Energy:\nInstalled Capacity by Country and Population (2023)', fontsize=16, fontweight='bold', loc='left')
ax1.set_xlim(0, max(installed_capacity) + 100)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Add a secondary y-axis for population
ax2 = ax1.twiny()
ax2.set_xlim(0, max(populations) + 50)
ax2.set_xlabel('Population (Millions)', fontsize=12)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

# Overlaying a line plot on the bar chart for population
pop_line, = ax2.plot(populations, countries, 'o-', color='tab:red', label='Population (Millions)', linewidth=2, markersize=6)

# Enhance readability by adding annotations
for i, bar in enumerate(bars):
    ax1.annotate(f'{installed_capacity[i]} GW',
                 xy=(installed_capacity[i], bar.get_y() + bar.get_height() / 2),
                 xytext=(5, 0), textcoords='offset points',
                 ha='left', va='center', fontsize=10, fontweight='bold')

# Adding a legend to describe different elements
ax2.legend(loc='upper right')

# Using tight layout for optimal spacing
plt.tight_layout()

# Display the plot
plt.show()