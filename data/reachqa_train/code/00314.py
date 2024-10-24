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

# Future potential scores for each galaxy
future_potential_scores = [65, 75, 60]

# Define colors for each priority and line plot
colors = ['#2a9d8f', '#e9c46a', '#f4a261']
line_color = '#264653'

# Initialize plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Set positions for each bar
bar_positions = np.arange(len(galaxies))
bottoms = np.zeros(len(galaxies))

# Plot each priority as a stacked bar
for idx, (priority, color) in enumerate(zip(priorities, colors)):
    values = [alloc[idx] for alloc in allocations]
    ax1.bar(bar_positions, values, bottom=bottoms, color=color, label=priority)
    bottoms += values

# Add percentage labels on the bars
for i, galaxy in enumerate(galaxies):
    cumulative = 0
    for j, percentage in enumerate(allocations[i]):
        ax1.text(i, cumulative + percentage / 2, f"{percentage}%", ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        cumulative += percentage

# Secondary y-axis for future potential scores
ax2 = ax1.twinx()
ax2.plot(bar_positions, future_potential_scores, color=line_color, marker='o', linestyle='--', label='Future Potential', linewidth=2, markersize=8)

# Customizing the chart
ax1.set_title("Galaxy Exploration Fund Allocation:\nUnderstanding Investment Priorities", fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(galaxies, fontsize=12)
ax1.set_xlim(-0.5, len(galaxies)-0.5)
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_yticklabels([f"{i}%" for i in range(0, 101, 10)], fontsize=10)
ax1.set_ylabel('Allocation Percentage', fontsize=12)
ax1.legend(title='Priorities', title_fontsize='13', fontsize='10', loc='upper left')

# Customizing secondary axis
ax2.set_ylabel('Future Potential Score', fontsize=12, color=line_color)
ax2.set_ylim(50, 100)
ax2.tick_params(axis='y', labelcolor=line_color)
ax2.legend(loc='upper right')

# Optimize layout
fig.tight_layout()

# Display the plot
plt.show()