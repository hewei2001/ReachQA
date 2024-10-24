import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define coffee types and seasons
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Cold Brew', 'Mocha']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Data: Preference scores for each coffee type across the seasons
data = {
    'Spring': [7, 6, 8, 5, 6],
    'Summer': [5, 7, 6, 9, 4],
    'Autumn': [8, 7, 6, 4, 9],
    'Winter': [9, 8, 7, 3, 8],
}

# Number of variables
N = len(coffee_types)

# Calculate angles for each coffee type
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Append first coffee type score to close the chart
for season in data:
    data[season].append(data[season][0])

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each season
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
markers = ['o', 's', 'D', '^']
for i, (season, values) in enumerate(data.items()):
    ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.plot(angles, values, color=colors[i], linewidth=2, marker=markers[i], label=season, markerfacecolor='white')

# Add grid and customize
ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.6)
ax.spines['polar'].set_visible(False)

# Add labels for each coffee type
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(coffee_types, fontsize=12, fontweight='bold')

# Add radial grid labels
ax.set_rlabel_position(0)
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color="grey", size=10)
plt.ylim(0, 10)

# Add average preference line
average_values = [np.mean([data[season][i] for season in data]) for i in range(N)]
average_values += average_values[:1]
ax.plot(angles, average_values, color='black', linewidth=2, linestyle='--', label='Average')

# Title and legend
plt.title("Seasonal Coffee Preferences\nin Brewville: A Comparative Radar View", size=18, fontweight='bold', va='bottom', pad=30)
legend_labels = [Patch(facecolor=colors[i], edgecolor='black', label=season) for i, season in enumerate(seasons)]
plt.legend(handles=legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Seasons', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()