import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each season
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for i, (season, values) in enumerate(data.items()):
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=season)
    ax.plot(angles, values, color=colors[i], linewidth=2)

# Add labels for each coffee type
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(coffee_types, fontsize=11)

# Title and legend
plt.title("Seasonal Coffee Preferences\nin Brewville", size=16, fontweight='bold', va='bottom', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Seasons', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()