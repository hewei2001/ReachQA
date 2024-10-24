import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data preparation: Player performance scores for five fantasy teams
team_scores = {
    'Team Alpha': [65, 78, 82, 55, 67, 72, 59, 88, 90, 62, 81, 85, 54, 76, 80],
    'Team Bravo': [59, 73, 65, 60, 75, 70, 85, 68, 74, 66, 69, 77, 71, 82, 79],
    'Team Charlie': [78, 83, 69, 76, 85, 91, 75, 80, 87, 74, 88, 90, 69, 81, 83],
    'Team Delta': [62, 58, 61, 69, 70, 66, 72, 64, 63, 67, 65, 74, 71, 68, 59],
    'Team Echo': [80, 90, 85, 87, 92, 84, 95, 88, 86, 89, 91, 93, 83, 85, 94]
}

teams = list(team_scores.keys())
data = [team_scores[team] for team in teams]

# Initialize figure with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Boxplot with colors from a colormap
cmap = plt.get_cmap("tab20")
colors = [cmap(i) for i in range(len(teams))]

bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, labels=teams,
                boxprops=dict(facecolor='white', color='blue'),
                medianprops=dict(color='darkred', linewidth=2),
                whiskerprops=dict(linestyle='--', color='grey'),
                capprops=dict(color='grey'))

# Setting colors for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Overlaying individual data points
for i, team_data in enumerate(data):
    y = team_data
    x = np.random.normal(i + 1, 0.04, size=len(y))  # adding some jitter
    ax.scatter(x, y, color=colors[i], alpha=0.6, edgecolor='k')

# Adding means and standard deviation annotations
means = [np.mean(scores) for scores in data]
std_devs = [np.std(scores) for scores in data]
for i, (mean, std_dev) in enumerate(zip(means, std_devs)):
    ax.text(i + 1, mean + 1, f"μ={mean:.1f}\nσ={std_dev:.1f}", 
            ha='center', va='bottom', fontsize=9, color='black')

# Title and labels
ax.set_title("Fantasy League Soccer:\nPlayer Performance Score Distribution by Team", fontsize=16, fontweight='bold')
ax.set_xlabel("Fantasy Teams", fontsize=13)
ax.set_ylabel("Performance Score", fontsize=13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Reference line for average performance score across all teams
overall_mean = np.mean([score for team in data for score in team])
ax.axhline(overall_mean, color='r', linestyle='--', linewidth=1.5, label='Overall Average Score')

# Legend for median and overall average line
ax.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()