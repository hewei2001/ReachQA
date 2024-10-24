import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Artificial data representing player levels in Arcadia Online
levels = np.array(
    [1] * 50 + [2] * 70 + [3] * 90 + [4] * 120 + [5] * 150 +
    [6] * 180 + [7] * 200 + [8] * 220 + [9] * 200 + [10] * 170 +
    [11] * 150 + [12] * 120 + [13] * 100 + [14] * 80 + [15] * 60 +
    [16] * 50 + [17] * 30 + [18] * 20 + [19] * 15 + [20] * 10
)

# Define bins: focused on grouping for better contrast
bins = np.arange(1, 22)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))
n, bins, patches = ax.hist(levels, bins=bins, edgecolor='black', alpha=0.75)

# Apply a gradient color to the histogram bars
colormap = plt.cm.viridis
for bin_idx in range(len(bins) - 1):
    patches[bin_idx].set_facecolor(colormap(bin_idx / len(bins)))

# Title and axis labels with multiline support
ax.set_title("Level Distribution Among Players in\nArcadia Online", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Player Levels", fontsize=12)
ax.set_ylabel("Number of Players", fontsize=12)

# Add data labels above the bars
for rect in patches:
    height = rect.get_height()
    ax.annotate(f'{int(height)}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5),  # Offset text by 5 points in y direction
                textcoords='offset points',
                ha='center', va='bottom')

# Add a grid and major ticks
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set x-ticks and limits for clarity
ax.set_xticks(np.arange(1, 21, 1))
ax.set_xlim(0.5, 20.5)
ax.set_ylim(0, max(n) + 20)

# Add a secondary y-axis for cumulative percentage
ax2 = ax.twinx()
cumulative_counts = np.cumsum(n)
ax2.plot(bins[:-1] + 0.5, cumulative_counts / cumulative_counts[-1] * 100, 'r-', marker='o', label='Cumulative Percentage')
ax2.set_ylabel('Cumulative Percentage (%)', fontsize=12)
ax2.set_ylim(0, 100)
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))

# Include legends where necessary
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.85))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()