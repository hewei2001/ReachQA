import matplotlib.pyplot as plt
import numpy as np

# Cities and their corresponding percentage of urban area dedicated to green spaces
cities = ['New York', 'Tokyo', 'Paris', 'Sydney', 'Toronto', 'Rio de Janeiro', 'Cape Town', 'Mumbai']
green_space_percentage = [27, 20, 30, 46, 36, 48, 23, 15]

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Define the positions for the bars
positions = np.arange(len(cities))

# Plot bars with distinct colors
colors = plt.cm.viridis(np.linspace(0, 1, len(cities)))
bars = ax.bar(positions, green_space_percentage, color=colors, width=0.6)

# Add title and labels with appropriate font size and style
ax.set_title('Percentage of Urban Areas Dedicated to Green Spaces', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Green Space (%)', fontsize=12)

# Set x-ticks to the position of cities and rotate labels for better readability
ax.set_xticks(positions)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

# Add data labels on top of each bar
for bar, percentage in zip(bars, green_space_percentage):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{percentage}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Enable grid lines for y-axis to enhance readability
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Apply tight layout to ensure everything fits without overlapping
plt.tight_layout()

# Show the plot
plt.show()