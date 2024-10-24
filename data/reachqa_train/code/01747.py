import matplotlib.pyplot as plt
import numpy as np

# Data preparation: Player performance scores for five fantasy teams
team_scores = {
    'Team Alpha': [65, 78, 82, 55, 67, 72, 59, 88, 90, 62, 81, 85, 54, 76, 80],
    'Team Bravo': [59, 73, 65, 60, 75, 70, 85, 68, 74, 66, 69, 77, 71, 82, 79],
    'Team Charlie': [78, 83, 69, 76, 85, 91, 75, 80, 87, 74, 88, 90, 69, 81, 83],
    'Team Delta': [62, 58, 61, 69, 70, 66, 72, 64, 63, 67, 65, 74, 71, 68, 59],
    'Team Echo': [80, 90, 85, 87, 92, 84, 95, 88, 86, 89, 91, 93, 83, 85, 94]
}

# List of teams for labeling
teams = list(team_scores.keys())
data = [team_scores[team] for team in teams]

# Creating the vertical box chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting with enhanced styling
boxprops = dict(facecolor='lightblue', color='blue')
medianprops = dict(linewidth=2, color='darkred')
whiskerprops = dict(linestyle='--', linewidth=1.5, color='grey')
capprops = dict(color='grey', linewidth=1.5)

ax.boxplot(data, patch_artist=True, boxprops=boxprops, medianprops=medianprops,
           whiskerprops=whiskerprops, capprops=capprops, notch=True, vert=True, labels=teams)

# Enhancing the chart
ax.set_title("Fantasy League Soccer:\nPlayer Performance Score Distribution by Team", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Fantasy Teams", fontsize=12)
ax.set_ylabel("Performance Score", fontsize=12)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend for the median line
median_legend = plt.Line2D([0], [0], color='darkred', label='Median Performance', linestyle='-', linewidth=2)
ax.legend(handles=[median_legend], loc='upper right', fontsize=10)

# Adjust the layout to prevent overlaps
plt.tight_layout()

# Display the plot
plt.show()