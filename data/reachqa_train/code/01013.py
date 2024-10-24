import matplotlib.pyplot as plt
import numpy as np

# Define the types of coffee beans
bean_types = ['Arabica', 'Robusta', 'Liberica', 'Excelsa']

# Define the continents
continents = ['North America', 'Europe', 'Asia', 'Africa', 'South America']

# Number of coffee roasteries primarily using each bean type per continent
roastery_data = [
    [200, 50, 20, 10],  # North America
    [180, 60, 25, 15],  # Europe
    [150, 80, 35, 20],  # Asia
    [90, 120, 40, 25],  # Africa
    [170, 70, 30, 15]   # South America
]

# Convert data into a numpy array for manipulation
roastery_data = np.array(roastery_data)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Bar width
bar_width = 0.18

# Create an array for the x-axis indices
x_indices = np.arange(len(continents))

# Plot bars for each coffee bean type
colors = ['#8B4513', '#CD853F', '#DAA520', '#D2B48C']
for i, bean_type in enumerate(bean_types):
    ax.bar(x_indices + i * bar_width, roastery_data[:, i], width=bar_width, label=bean_type, color=colors[i])

# Add data annotations
for i, continent_data in enumerate(roastery_data):
    for j, value in enumerate(continent_data):
        ax.text(i + j * bar_width, value + 3, str(value), ha='center', va='bottom', fontsize=9, color='black')

# Set the labels and ticks
ax.set_xlabel('Continents', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Roasteries', fontsize=12, labelpad=10)
ax.set_title('Evolution of Coffee Preferences Across Continents\nin 2023', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(continents)

# Rotate x-axis labels for better readability
plt.xticks(rotation=20)

# Add a legend to the plot
ax.legend(title='Coffee Bean Types', loc='upper right', bbox_to_anchor=(1.15, 1))

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()