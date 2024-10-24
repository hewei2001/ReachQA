import matplotlib.pyplot as plt
import numpy as np

# Define labels for the radar chart
radar_labels = np.array(['Strength', 'Intelligence', 'Speed', 'Endurance', 'Agility'])
num_vars = len(radar_labels)

# Radar chart data for superheroes
radar_scores = np.array([
    [8, 5, 9, 6, 7],  # Thunderbolt
    [4, 9, 5, 7, 6],  # Brainwave
    [6, 7, 10, 5, 8], # Flashwing
    [9, 6, 4, 9, 5]   # Stoneheart
])

# Superhero names
superheroes = ['Thunderbolt', 'Brainwave', 'Flashwing', 'Stoneheart']

# Create angles for radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
radar_scores = np.concatenate((radar_scores, radar_scores[:, [0]]), axis=1)
angles += angles[:1]

# Define labels and scores for the bar chart
bar_labels = ['Popularity', 'Teamwork', 'Strategy', 'Tech Skills', 'Stealth']
bar_scores = np.array([
    [75, 85, 65, 70, 60],  # Thunderbolt
    [60, 95, 80, 85, 90],  # Brainwave
    [80, 70, 90, 75, 85],  # Flashwing
    [90, 60, 75, 85, 95]   # Stoneheart
])

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'polar': [True, False]})
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Radar Chart
for idx, score in enumerate(radar_scores):
    ax1.fill(angles, score, color=colors[idx], alpha=0.25, label=superheroes[idx])
    ax1.plot(angles, score, color=colors[idx], linewidth=2)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(radar_labels, size=10, weight='bold')
ax1.set_yticklabels([])
ax1.set_title("Comparative Skill Sets of Superheroes", size=13, weight='bold', y=1.1)
ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=9)

# Bar Chart
bar_width = 0.15
x = np.arange(len(bar_labels))
for idx, score in enumerate(bar_scores):
    ax2.bar(x + idx * bar_width, score, bar_width, color=colors[idx], label=superheroes[idx])

ax2.set_xlabel('Attributes', fontsize=12, weight='bold')
ax2.set_ylabel('Scores', fontsize=12, weight='bold')
ax2.set_title("Additional Attributes Analysis", fontsize=13, weight='bold', y=1.05)
ax2.set_xticks(x + bar_width * 1.5)
ax2.set_xticklabels(bar_labels, fontsize=10, weight='bold')
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=9)

plt.tight_layout()
plt.show()