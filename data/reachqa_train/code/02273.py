import matplotlib.pyplot as plt
import numpy as np

# Define architectural periods and their contributions
periods = ['Romanesque', 'Gothic', 'Renaissance', 'Baroque', 'Neoclassical', 'Modern']
contributions = [10, 20, 15, 10, 5, 30]

# Construct related data for the overlay plot
# Represents the "popularity score" of each architectural period
popularity_trend = [5, 25, 18, 15, 10, 40]

# Calculate cumulative contributions
initial_value = 0
cumulative_contributions = np.insert(np.cumsum(contributions), 0, initial_value)

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Waterfall Chart
bar_positions = np.arange(len(periods))
bar_heights = np.diff(cumulative_contributions)
colors = ['#28a745' if h > 0 else '#dc3545' for h in bar_heights]
bars = ax1.bar(bar_positions, bar_heights, bottom=cumulative_contributions[:-1],
               color=colors, edgecolor='black', linewidth=1.5)

ax1.step(range(len(periods)), cumulative_contributions[1:], where='mid', color='black', linestyle='--', linewidth=1)
ax1.set_ylabel('Cumulative Contribution', fontsize=12, color='black')
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(periods, rotation=45, ha='right', fontsize=11)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.axhline(initial_value, color='blue', linewidth=1.5, linestyle='--', label='Starting Baseline')

# Line Plot - Popularity Trend
ax2 = ax1.twinx()
ax2.plot(bar_positions, popularity_trend, color='purple', marker='o', linewidth=2, markersize=8, label='Popularity Trend')
ax2.set_ylabel('Popularity Score', fontsize=12, color='purple')
ax2.set_ylim(0, max(popularity_trend) + 10)

# Title and Labels
ax1.set_title('Evolution and Popularity of Architectural Styles\nContributing to Modern Architecture',
              fontsize=16, pad=20)

# Annotations
for bar, contrib in zip(bars, contributions):
    height = bar.get_height()
    label_y = bar.get_y() + height / 2
    ax1.text(bar.get_x() + bar.get_width() / 2, label_y,
             f'+{contrib}', ha='center', va='center', color='white', fontsize=10)

# Adjust layout
plt.tight_layout()

# Legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10)

# Show plot
plt.show()