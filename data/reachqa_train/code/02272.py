import matplotlib.pyplot as plt
import numpy as np

# Define architectural periods and their contributions
periods = ['Romanesque', 'Gothic', 'Renaissance', 'Baroque', 'Neoclassical', 'Modern']
contributions = [10, 20, 15, 10, 5, 30]

# Calculate the cumulative contributions
initial_value = 0
cumulative_contributions = np.insert(np.cumsum(contributions), 0, initial_value)

# Determine the positions and heights of the bars
bar_positions = np.arange(len(periods))
bar_heights = np.diff(cumulative_contributions)

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors for positive changes
colors = ['#28a745' if h > 0 else '#dc3545' for h in bar_heights]

# Plot each bar of the waterfall chart
bars = ax.bar(bar_positions, bar_heights, bottom=cumulative_contributions[:-1],
              color=colors, edgecolor='black', linewidth=1.5)

# Connect bars with a line
ax.step(range(len(periods)), cumulative_contributions[1:], where='mid', color='black', linestyle='--', linewidth=1)

# Title and labels
ax.set_title('Evolution of Architectural Styles\nContributing to Modern Architecture', fontsize=16, pad=20)
ax.set_ylabel('Cumulative Contribution', fontsize=12)
ax.set_xlabel('Architectural Period', fontsize=12)

# Annotate each bar with contribution value
for bar, contrib in zip(bars, contributions):
    height = bar.get_height()
    label_y = bar.get_y() + height / 2
    ax.text(bar.get_x() + bar.get_width() / 2, label_y,
            f'+{contrib}', ha='center', va='center', color='white', fontsize=10)

# X-axis settings
ax.set_xticks(bar_positions)
ax.set_xticklabels(periods, rotation=45, ha='right', fontsize=11)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight the starting baseline
ax.axhline(initial_value, color='blue', linewidth=1.5, linestyle='--', label='Starting Baseline')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display legend
ax.legend(loc='upper left', fontsize=10)

# Show plot
plt.show()