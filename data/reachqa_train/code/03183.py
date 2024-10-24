import matplotlib.pyplot as plt
import numpy as np

# Years for the data
years = ['2018', '2020', '2023']

# Percentage usage data for each year
# Each sublist represents [Desktop, Mobile, Tablet] percentages
usage_data = [
    [60, 30, 10],  # 2018
    [50, 40, 10],  # 2020
    [40, 50, 10]   # 2023
]

# Convert usage data into a numpy array
usage_data = np.array(usage_data)

# Define colors for each device type
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Stack the bar chart to show percentages
bars = []
bars.append(ax.bar(years, usage_data[:, 0], color=colors[0], label='Desktop'))
bars.append(ax.bar(years, usage_data[:, 1], bottom=usage_data[:, 0], color=colors[1], label='Mobile'))
bars.append(ax.bar(years, usage_data[:, 2], bottom=usage_data[:, 0] + usage_data[:, 1], color=colors[2], label='Tablet'))

# Add title and labels
ax.set_title('Global Internet Usage by Device Type\n(2018-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Internet Usage', fontsize=12)

# Set y-axis to represent 0-100%
ax.set_ylim(0, 100)

# Add a legend
ax.legend(title='Device Type', loc='upper right', fontsize=10)

# Adding data annotations
for i in range(len(years)):
    for j in range(len(bars)):
        height = bars[j][i].get_height()
        bottom = bars[j][i].get_y()
        ax.text(bars[j][i].get_x() + bars[j][i].get_width() / 2, bottom + height / 2,
                f'{int(height)}%', ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()