import matplotlib.pyplot as plt
import numpy as np

# Define the data for each country and plant-based milk type (liters per capita)
countries = ['USA', 'Germany', 'India', 'Brazil', 'China']
almond_milk = np.array([4.2, 2.7, 1.5, 3.3, 2.0])
soy_milk = np.array([3.5, 1.9, 4.5, 2.8, 3.7])
oat_milk = np.array([2.8, 3.6, 0.7, 1.2, 2.9])
coconut_milk = np.array([1.6, 1.2, 2.1, 3.7, 1.5])
rice_milk = np.array([1.1, 1.3, 1.0, 0.9, 2.0])

# Construct additional data for percentage growth from previous year
growth_rate = np.array([5, 10, -3, 7, 12])

fig, ax1 = plt.subplots(figsize=(12, 8))
width = 0.15  # Width of each bar
y_pos = np.arange(len(countries))

# Plot bars for each milk type
ax1.barh(y_pos - 2*width, almond_milk, height=width, label='Almond Milk', color='sandybrown')
ax1.barh(y_pos - width, soy_milk, height=width, label='Soy Milk', color='lightgreen')
ax1.barh(y_pos, oat_milk, height=width, label='Oat Milk', color='wheat')
ax1.barh(y_pos + width, coconut_milk, height=width, label='Coconut Milk', color='lightblue')
ax1.barh(y_pos + 2*width, rice_milk, height=width, label='Rice Milk', color='tan')

# Configure the primary y-axis
ax1.set_yticks(y_pos)
ax1.set_yticklabels(countries)
ax1.set_xlabel('Liters per Capita', fontsize=12)
ax1.set_title('Global Trends in Plant-Based Milk Consumption\nand Growth Rates Across Countries in 2023', 
              fontsize=14, fontweight='bold')

# Adding grid lines for x-axis
ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Secondary axis for growth rate line plot
ax2 = ax1.twinx()
ax2.plot(growth_rate, y_pos, 'r--o', label='Growth Rate (%)', color='darkred', linewidth=2, markersize=8)
ax2.set_yticks([])  # Hide secondary y-ticks
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Adding legends
ax1.legend(loc='upper left', title='Milk Types')
ax2.legend(loc='lower right', title='Additional Data')

# Annotate consumption values on each bar
def add_values(bars, ax):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'{width:.1f}', va='center', fontsize=9)

for bar_group in ax1.containers:
    add_values(bar_group, ax1)

# Annotate growth rate values on line plot
for i, rate in enumerate(growth_rate):
    ax2.text(rate + 0.5, i, f'{rate}%', color='darkred', va='center', fontsize=9)

plt.tight_layout()
plt.show()