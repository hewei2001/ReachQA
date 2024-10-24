import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Define the years and corresponding average EV range data
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
avg_range = np.array([60, 75, 90, 120, 150, 200, 250])

# Additional data: battery cost in $/kWh (hypothetical data)
battery_cost = np.array([1000, 800, 600, 400, 300, 200, 150])

# Create the figure with subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Primary line plot for average range
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(vmin=min(avg_range), vmax=max(avg_range))
colors = cmap(norm(avg_range))
ax1.plot(years, avg_range, marker='o', linestyle='-', linewidth=2, label='Average Range', color='black')

# Annotate the data points
for year, range_val, color in zip(years, avg_range, colors):
    ax1.annotate(f'{range_val} mi', xy=(year, range_val), xytext=(0, 10), 
                 textcoords='offset points', ha='center', fontsize=9, color=color)

# Add a secondary axis for battery cost
ax2 = ax1.twinx()
ax2.plot(years, battery_cost, marker='s', linestyle='--', color='red', linewidth=2, label='Battery Cost')
ax2.set_ylabel('Battery Cost ($/kWh)', fontsize=12, color='red')
ax2.tick_params(axis='y', colors='red')
ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'${int(x)}'))

# Titles and labels
plt.title('Evolution of Electric Vehicle Technology\nOver the Decades (1990-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average EV Range (miles)', fontsize=12, color='black')

# Legends
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0.05, 1))
ax2.legend(loc='upper right', fontsize=10, bbox_to_anchor=(0.95, 1))

# Grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.5)
fig.tight_layout()

# Display the plot
plt.show()