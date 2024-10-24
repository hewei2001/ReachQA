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

# Growth projections data (hypothetical) for the overlay line plot
growth_data = np.array([
    [37, 28, 42],  # New York
    [43, 22, 41],  # London
    [32, 38, 37],  # Tokyo
    [52, 18, 38],  # Berlin
    [48, 23, 37],  # Sydney
])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Colors for each sector
colors = ['#FF5733', '#33FF57', '#3357FF']

# Plot the stacked bar chart
bottoms = np.zeros(len(cities))
for i, (sector, color) in enumerate(zip(sectors, colors)):
    ax1.bar(cities, data[:, i], bottom=bottoms, label=sector, color=color, alpha=0.8)
    bottoms += data[:, i]

# Customize main chart
ax1.set_title("Intergalactic Eco-Integration 2050:\nCity Contributions by Sector and Growth Projections", fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Contribution Units', fontsize=12)
ax1.set_xlabel('Cities', fontsize=12)
ax1.set_xticks(range(len(cities)))
ax1.set_xticklabels(cities, fontsize=10, rotation=30, ha='right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add a secondary y-axis for the line plot
ax2 = ax1.twinx()
growth_totals = growth_data.sum(axis=1)
ax2.plot(cities, growth_totals, color='black', marker='o', linestyle='-', linewidth=2, label='Total Growth Projection')
ax2.set_ylabel('Projected Growth Units', fontsize=12)

# Add a legend
ax1.legend(title='Sectors', fontsize=10, loc='upper left')
ax2.legend(title='Growth Projection', fontsize=10, loc='upper right')

# Annotate values on each bar segment
for i in range(len(cities)):
    y = 0
    for j in range(len(sectors)):
        ax1.text(i, y + data[i, j] / 2, f"{data[i, j]}", ha='center', va='center', color='white', fontsize=9)
        y += data[i, j]

# Annotate the line plot points
for i in range(len(cities)):
    ax2.text(i, growth_totals[i], f"{growth_totals[i]}", ha='center', va='bottom', color='black', fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()