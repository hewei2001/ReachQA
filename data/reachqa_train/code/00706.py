import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Define city names
cities = ["New York", "London", "Tokyo", "Paris", "Toronto", "Sydney", "Berlin", "Singapore"]

# Define the number of parks per square mile for each city
parks_per_square_mile = np.array([3.2, 4.1, 2.8, 5.0, 3.5, 6.3, 4.5, 3.7])

# Define hypothetical average annual rainfall for each city (in inches)
average_rainfall = np.array([49.9, 23.8, 60.4, 25.3, 32.1, 50.3, 22.7, 92.0])

# Set the positions and width for the bars
positions = np.arange(len(cities))
bar_width = 0.6

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Color map for the gradient effect
color_map = cm.viridis(parks_per_square_mile / max(parks_per_square_mile))

# Create the primary bar chart for parks per square mile
bars = ax1.bar(positions, parks_per_square_mile, color=color_map, width=bar_width, alpha=0.9, edgecolor='black', label='Parks per Square Mile')

# Add data labels on top of each bar
for bar, height in zip(bars, parks_per_square_mile):
    ax1.text(bar.get_x() + bar.get_width()/2, height - 0.1, f'{height:.1f}', ha='center', va='bottom', color='white', fontsize=10)

# Adding a secondary Y-axis for average annual rainfall
ax2 = ax1.twinx()
ax2.plot(positions, average_rainfall, color='orange', marker='o', linewidth=2.5, label='Average Annual Rainfall (inches)')
ax2.set_ylabel('Average Annual Rainfall (inches)', fontsize=12, color='orange')

# Customize x-ticks and labels
ax1.set_xticks(positions)
ax1.set_xticklabels(cities, rotation=45, ha='right')
ax1.set_xlabel('City', fontsize=12)

# Customize y-ticks and labels
ax1.set_ylabel('Parks per Square Mile', fontsize=12)
ax1.set_ylim(0, max(parks_per_square_mile) + 2)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Chart title
plt.title('Rise of Urban Green Spaces & Climate Impact:\nParks and Rainfall in Major Cities (2023)', fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Create legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show plot
plt.show()