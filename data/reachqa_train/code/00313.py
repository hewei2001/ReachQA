import matplotlib.pyplot as plt
import numpy as np

# Define data for galaxies and their priority allocations (percentages)
galaxies = ['Milky Way', 'Andromeda', 'Triangulum']
priorities = ['Tech Dev.', 'Resource Acq.', 'Cultural Exch.']
allocations = [
    [50, 30, 20],  # Milky Way
    [35, 45, 20],  # Andromeda
    [40, 25, 35]   # Triangulum
]

# Define colors for each priority
colors = ['#2a9d8f', '#e9c46a', '#f4a261']

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set positions for each bar
bar_positions = np.arange(len(galaxies))

# Initialize cumulative bottom values for the stacked bar
bottoms = np.zeros(len(galaxies))

# Plot each priority as a stacked bar
for idx, (priority, color) in enumerate(zip(priorities, colors)):
    values = [alloc[idx] for alloc in allocations]
    ax.bar(bar_positions, values, bottom=bottoms, color=color, label=priority)
    bottoms += values

# Customizing the chart
ax.set_title("Galaxy Exploration Fund Allocation:\nUnderstanding Investment Priorities", fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(bar_positions)
ax.set_xticklabels(galaxies, fontsize=12)
ax.set_xlim(-0.5, len(galaxies)-0.5)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f"{i}%" for i in range(0, 101, 10)], fontsize=10)
ax.set_ylabel('Allocation Percentage', fontsize=12)
ax.legend(title='Priorities', title_fontsize='13', fontsize='10', loc='upper right')

# Add percentage labels on the bars
for i, galaxy in enumerate(galaxies):
    cumulative = 0
    for j, priority in enumerate(priorities):
        percentage = allocations[i][j]
        ax.text(i, cumulative + percentage / 2, f"{percentage}%", ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        cumulative += percentage

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()