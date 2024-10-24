import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2019
years = np.arange(2010, 2020)

# Average tree height data for four parks (in meters)
central_park = [3.1, 3.4, 3.8, 4.0, 4.3, 4.6, 4.9, 5.1, 5.5, 5.8]
westside_park = [2.8, 3.0, 3.3, 3.5, 3.8, 4.1, 4.3, 4.6, 4.8, 5.1]
greenwood_park = [2.5, 2.7, 3.0, 3.2, 3.5, 3.7, 3.9, 4.2, 4.5, 4.7]
riverside_park = [3.0, 3.2, 3.5, 3.7, 4.0, 4.3, 4.5, 4.8, 5.0, 5.4]

# Annual rainfall data in millimeters for each year
rainfall_data = [800, 850, 780, 820, 870, 760, 890, 910, 860, 900]

# Combine the tree height data into a list of arrays
tree_height_data = [central_park, westside_park, greenwood_park, riverside_park]
park_names = ["Central Park", "Westside Park", "Greenwood Park", "Riverside Park"]

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 8))

# Define colors and markers for the lines
colors = ['#76c7c0', '#ff8c94', '#6a0572', '#f8a488']
markers = ['o', 's', 'D', '^']

# Plot the tree height data
for data, name, color, marker in zip(tree_height_data, park_names, colors, markers):
    ax1.plot(years, data, label=name, color=color, marker=marker, linewidth=2)

    # Annotate data points with the height values
    for (x, y) in zip(years, data):
        ax1.annotate(f'{y:.1f}m', xy=(x, y), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontsize=9)

# Set title and labels
ax1.set_title('Rise of Urban Green Spaces:\nMonitoring Tree Growth and Rainfall Over a Decade', 
              fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Tree Height (m)', fontsize=12)

# Add gridlines
ax1.grid(True, linestyle='--', which='major', color='grey', alpha=0.3)

# Add second y-axis for rainfall
ax2 = ax1.twinx()
ax2.bar(years, rainfall_data, alpha=0.3, color='b', label='Annual Rainfall (mm)')
ax2.set_ylabel('Annual Rainfall (mm)', fontsize=12)

# Adding legends
ax1.legend(title='Urban Parks', title_fontsize='13', loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()