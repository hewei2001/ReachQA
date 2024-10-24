import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']

# Coffee types
coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Cold Brew']

# Data for the average number of cups consumed per week for each coffee type by age group
consumption_data = np.array([
    [5, 3, 4, 2, 1],  # 18-24
    [4, 5, 2, 3, 2],  # 25-34
    [3, 4, 4, 4, 3],  # 35-44
    [2, 3, 3, 5, 4],  # 45-54
    [1, 2, 3, 4, 5]   # 55+
])

# Bar width and positions for grouped bar chart
bar_width = 0.15
x_positions = np.arange(len(age_groups))

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each coffee type's consumption across age groups with new color palette
colors = plt.cm.viridis(np.linspace(0, 1, len(coffee_types)))

for i, (coffee_type, color) in enumerate(zip(coffee_types, colors)):
    bars = ax.bar(x_positions + i * bar_width, consumption_data[:, i], bar_width, label=coffee_type, color=color, edgecolor='black')
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, f'{int(yval)}', ha='center', va='bottom', fontsize=10, color=color)

# Titles and labels
ax.set_title("Caffeination Nation\nCoffee Preferences Across Age Groups", fontsize=18, fontweight='bold', pad=30)
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Average Cups per Week', fontsize=14)
ax.set_xticks(x_positions + bar_width * 2)
ax.set_xticklabels(age_groups, fontsize=12)

# Enhancing grid and borders
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.xaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adding a secondary y-axis for total consumption across age groups
total_consumption = consumption_data.sum(axis=1)
ax2 = ax.twinx()
ax2.plot(x_positions + 2 * bar_width, total_consumption, color='red', marker='o', linestyle='-', linewidth=2, label='Total Consumption')
ax2.set_ylabel('Total Cups per Week', fontsize=14)
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', colors='red')

# Customizing legend
lines_labels = ax.get_legend_handles_labels()
lines_labels2 = ax2.get_legend_handles_labels()
ax.legend(lines_labels[0] + lines_labels2[0], lines_labels[1] + lines_labels2[1], title='Legend', fontsize=12, loc='upper right')

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()