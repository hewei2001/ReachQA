import matplotlib.pyplot as plt
import numpy as np

# Define centuries
centuries = np.array(['600 BC', '500 BC', '400 BC', '300 BC'])

# Contribution data for each civilization and sector (slightly modified for clarity)
egyptian_contributions = np.array([
    [50, 30, 10, 10],  # 600 BC
    [55, 25, 10, 10],  # 500 BC
    [60, 20, 10, 10],  # 400 BC
    [70, 15, 10, 5]    # 300 BC
])

greek_contributions = np.array([
    [20, 40, 30, 10],  # 600 BC
    [25, 45, 20, 10],  # 500 BC
    [30, 50, 10, 10],  # 400 BC
    [35, 55, 5, 5]     # 300 BC
])

chinese_contributions = np.array([
    [30, 20, 10, 40],  # 600 BC
    [35, 25, 10, 30],  # 500 BC
    [40, 30, 10, 20],  # 400 BC
    [45, 35, 5, 15]    # 300 BC
])

# Stack colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot for each civilization
bar_width = 0.25
x = np.arange(len(centuries))

# Egyptian civilization
ax.bar(x - bar_width, egyptian_contributions[:, 0], width=bar_width, color=colors[0], label='Egyptian - Agriculture')
ax.bar(x - bar_width, egyptian_contributions[:, 1], width=bar_width, bottom=egyptian_contributions[:, 0], color=colors[1], label='Egyptian - Trade')
ax.bar(x - bar_width, egyptian_contributions[:, 2], width=bar_width, bottom=egyptian_contributions[:, :2].sum(axis=1), color=colors[2], label='Egyptian - Warfare')
ax.bar(x - bar_width, egyptian_contributions[:, 3], width=bar_width, bottom=egyptian_contributions[:, :3].sum(axis=1), color=colors[3], label='Egyptian - Science')

# Greek civilization
ax.bar(x, greek_contributions[:, 0], width=bar_width, color=colors[0], alpha=0.6, label='Greek - Agriculture')
ax.bar(x, greek_contributions[:, 1], width=bar_width, bottom=greek_contributions[:, 0], color=colors[1], alpha=0.6, label='Greek - Trade')
ax.bar(x, greek_contributions[:, 2], width=bar_width, bottom=greek_contributions[:, :2].sum(axis=1), color=colors[2], alpha=0.6, label='Greek - Warfare')
ax.bar(x, greek_contributions[:, 3], width=bar_width, bottom=greek_contributions[:, :3].sum(axis=1), color=colors[3], alpha=0.6, label='Greek - Science')

# Chinese civilization
ax.bar(x + bar_width, chinese_contributions[:, 0], width=bar_width, color=colors[0], alpha=0.3, label='Chinese - Agriculture')
ax.bar(x + bar_width, chinese_contributions[:, 1], width=bar_width, bottom=chinese_contributions[:, 0], color=colors[1], alpha=0.3, label='Chinese - Trade')
ax.bar(x + bar_width, chinese_contributions[:, 2], width=bar_width, bottom=chinese_contributions[:, :2].sum(axis=1), color=colors[2], alpha=0.3, label='Chinese - Warfare')
ax.bar(x + bar_width, chinese_contributions[:, 3], width=bar_width, bottom=chinese_contributions[:, :3].sum(axis=1), color=colors[3], alpha=0.3, label='Chinese - Science')

# Title and labels
ax.set_title('The Rise of Ancient Civilizations:\nSector Contributions Over Centuries', fontsize=18, fontweight='bold')
ax.set_xlabel('Century', fontsize=14)
ax.set_ylabel('Contribution Index (Hypothetical Units)', fontsize=14)

# Set x-ticks
ax.set_xticks(x)
ax.set_xticklabels(centuries)

# Add grid lines
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Legend handling
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=9, title='Legend')

# Adjust layout to prevent clipping of tick-labels and legend
plt.tight_layout()

# Display the plot
plt.show()