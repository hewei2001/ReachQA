import matplotlib.pyplot as plt
import numpy as np

# Define the futuristic energy sources and city names
energy_sources = ['Solar Panels', 'Wind Turbines', 'Biofuel Cells', 'Hydrogen Power', 'Geothermal']
cities = ['Neo Tokyo', 'Future Paris', 'Cyber Berlin', 'New Delhi Next', 'Quantum New York']

# Create artificial data for each city's energy source efficiency (unit: megawatts)
energy_data = {
    'Neo Tokyo': [120, 95, 85, 130, 100],
    'Future Paris': [110, 85, 90, 140, 105],
    'Cyber Berlin': [115, 100, 80, 135, 110],
    'New Delhi Next': [125, 90, 75, 125, 95],
    'Quantum New York': [130, 105, 95, 150, 115]
}

# Box plot data preparation
box_data = [list(city_data) for city_data in zip(*energy_data.values())]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
bplot = ax.boxplot(box_data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightblue', color='blue'),
                   medianprops=dict(color='darkblue'),
                   whiskerprops=dict(color='blue'),
                   capprops=dict(color='blue'),
                   flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Color each box differently
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Set axis labels and title
ax.set_yticklabels(energy_sources)
ax.set_xlabel('Efficiency (Megawatts)')
ax.set_title('Efficiency of Futuristic Home Energy Sources\nin Urban Smart Homes (2050)', fontsize=14, fontweight='bold')

# Customize the y-axis labels
ax.set_yticks(np.arange(1, len(energy_sources) + 1))
ax.tick_params(axis='y', which='both', length=0)  # Remove tick marks from y-axis
for label in ax.get_yticklabels():
    label.set_fontsize(12)

# Add grid and layout adjustments
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()