import matplotlib.pyplot as plt
import numpy as np

# Define the cities and sectors
cities = ['New York', 'London', 'Tokyo', 'Berlin', 'Sydney']
sectors = ['Renewable Energy', 'Space Projects', 'Biodiversity']

# Contribution data in hypothetical units
data = np.array([
    [35, 25, 40],  # New York
    [40, 20, 40],  # London
    [30, 35, 35],  # Tokyo
    [50, 15, 35],  # Berlin
    [45, 20, 35],  # Sydney
])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Colors for each sector
colors = ['#FF5733', '#33FF57', '#3357FF']

# Plot each sector's contributions
bottoms = np.zeros(len(cities))
for i, (sector, color) in enumerate(zip(sectors, colors)):
    bars = ax.bar(cities, data[:, i], bottom=bottoms, label=sector, color=color, alpha=0.8)
    bottoms += data[:, i]

# Title and axis labels
ax.set_title("Intergalactic Eco-Integration 2050:\nCity Contributions by Sector", 
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Contribution Units', fontsize=12)
ax.set_xlabel('Cities', fontsize=12)

# Customize x-axis labels
ax.set_xticklabels(cities, fontsize=10, rotation=30, ha='right')

# Add legend
ax.legend(title='Sectors', fontsize=10, loc='upper left')

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotating values on each bar segment
for i in range(len(cities)):
    y = 0
    for j in range(len(sectors)):
        ax.text(i, y + data[i, j] / 2, f"{data[i, j]}",
                ha='center', va='center', color='white', fontsize=9)
        y += data[i, j]

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()