import matplotlib.pyplot as plt
import numpy as np

# Data for space missions
countries = ['USA', 'Russia', 'China', 'India', 'Japan']
missions_by_decade = {
    '1960s': [40, 55, 2, 0, 0],
    '1970s': [60, 70, 5, 0, 2],
    '1980s': [50, 60, 10, 2, 5],
    '1990s': [75, 65, 15, 5, 8],
    '2000s': [85, 55, 20, 10, 12],
    '2010s': [110, 70, 35, 25, 30]
}
decades = list(missions_by_decade.keys())
total_missions = [sum(missions_by_decade[decade]) for decade in decades]

width = 0.15
ind = np.arange(len(decades))

fig, ax = plt.subplots(figsize=(12, 8))

colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))
for i, (country, color) in enumerate(zip(countries, colors)):
    missions = [missions_by_decade[decade][i] for decade in decades]
    bars = ax.bar(ind + i * width, missions, width, label=country, color=color)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 3, int(yval), ha='center', va='bottom', fontsize=9)

# Overlay line plot for total missions per decade
ax2 = ax.twinx()
ax2.plot(ind + width * 2, total_missions, color='red', marker='o', linestyle='--', linewidth=2, label='Total Missions')
ax2.set_ylabel('Total Missions per Decade', fontsize=14, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Title and labels
ax.set_title('Space Exploration Missions by Country\nand Total Missions by Decade', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Number of Missions', fontsize=14)
ax.set_xticks(ind + width * 2)
ax.set_xticklabels(decades, fontsize=12)

# Grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Legend
ax.legend(title="Countries", fontsize=10)
ax2.legend(loc='upper left', fontsize=10)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()