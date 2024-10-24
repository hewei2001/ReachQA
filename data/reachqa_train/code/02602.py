import matplotlib.pyplot as plt
import numpy as np

# Data for planetary exploration missions
celestial_bodies = ['Mars', 'Venus', 'Jupiter', 'Saturn', 'Mercury', 'Moon', 'Comets']
missions_count = [55, 40, 15, 12, 8, 65, 10]

# Example data for success rates (in percentage)
success_rates = [80, 70, 50, 60, 90, 85, 65]

# Define color palette for bars and line plot
bar_colors = ['#FF5733', '#FFBD33', '#75FF33', '#33FF57', '#33FFF5', '#335BFF', '#AF33FF']
line_color = '#1F77B4'

# Set up the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar chart
bars = ax1.bar(celestial_bodies, missions_count, color=bar_colors, edgecolor='black', width=0.6)

# Annotate each bar with the mission count
for bar, count in zip(bars, missions_count):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, str(count), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Line plot on secondary y-axis for success rates
ax2 = ax1.twinx()
ax2.plot(celestial_bodies, success_rates, color=line_color, marker='o', linestyle='-', linewidth=2, markersize=7, label='Success Rate (%)')

# Titles and labels
ax1.set_title('Exploratory Missions Across the Solar System\nFocus on Celestial Bodies as of 2023 with Success Rates', fontsize=16, fontweight='bold')
ax1.set_xlabel('Celestial Bodies', fontsize=12, labelpad=10)
ax1.set_ylabel('Number of Missions', fontsize=12, labelpad=10)
ax2.set_ylabel('Success Rate (%)', fontsize=12, labelpad=10)

# Customize x-axis labels
ax1.set_xticks(np.arange(len(celestial_bodies)))
ax1.set_xticklabels(celestial_bodies, rotation=45, ha='right')

# Set limits and grid
ax1.set_ylim(0, 70)
ax2.set_ylim(0, 100)
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Legend for the line plot
ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()