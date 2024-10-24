import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = ['2018', '2020', '2023']

# Percentage usage data for each year
# Each sublist represents [Desktop, Mobile, Tablet] percentages
usage_data = np.array([
    [60, 30, 10],  # 2018
    [50, 40, 10],  # 2020
    [40, 50, 10]   # 2023
])

# Define colors for each device type
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Data for line plot - Total Internet Users in billions
internet_users = np.array([3.9, 4.3, 4.8])

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting the stacked bar chart
bars = []
bars.append(ax1.bar(years, usage_data[:, 0], color=bar_colors[0], label='Desktop'))
bars.append(ax1.bar(years, usage_data[:, 1], bottom=usage_data[:, 0], color=bar_colors[1], label='Mobile'))
bars.append(ax1.bar(years, usage_data[:, 2], bottom=usage_data[:, 0] + usage_data[:, 1], color=bar_colors[2], label='Tablet'))

# Set y-axis to represent 0-100%
ax1.set_ylim(0, 100)
ax1.set_ylabel('Percentage of Internet Usage', fontsize=12)

# Add title and labels
ax1.set_title('Global Internet Usage by Device Type\nand Total Internet Users (2018-2023)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)

# Adding a second y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(years, internet_users, color='magenta', marker='o', linestyle='--', linewidth=2, label='Total Internet Users')
ax2.set_ylabel('Internet Users (billions)', fontsize=12)
ax2.set_ylim(3.5, 5)

# Adding legends
bar_legend = ax1.legend(title='Device Type', loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)
ax1.add_artist(bar_legend)

# Adding data annotations for bar segments
for i, year in enumerate(years):
    for j in range(len(bars)):
        height = bars[j][i].get_height()
        bottom = bars[j][i].get_y()
        ax1.text(bars[j][i].get_x() + bars[j][i].get_width() / 2, bottom + height / 2,
                 f'{int(height)}%', ha='center', va='center', color='white', fontsize=9, fontweight='bold')

# Adding data annotations for line plot
for i, user in enumerate(internet_users):
    ax2.text(years[i], user + 0.05, f'{user:.1f}B', color='magenta', fontsize=9, ha='center')

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()