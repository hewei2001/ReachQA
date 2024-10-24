import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the metrics for the radar chart
metrics = ['Speed', 'Strength', 'Agility', 'Endurance', 'Strategy', 'Teamwork']
n_metrics = len(metrics)

# Performance data for each team
dragonfire = [9, 8, 7, 8, 6, 7]
elvenarchers = [7, 6, 9, 7, 8, 8]
griffinriders = [8, 9, 6, 9, 7, 8]

# Calculate Overall Performance Score as average
dragonfire_score = np.mean(dragonfire)
elvenarchers_score = np.mean(elvenarchers)
griffinriders_score = np.mean(griffinriders)
scores = [dragonfire_score, elvenarchers_score, griffinriders_score]
teams = ['Dragonfire', 'Elvenarchers', 'Griffinriders']

# Close the loop by repeating the first value
dragonfire += dragonfire[:1]
elvenarchers += elvenarchers[:1]
griffinriders += griffinriders[:1]

# Create angles for the radar chart
angles = np.linspace(0, 2 * pi, n_metrics, endpoint=False).tolist()
angles += angles[:1]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'polar': True}, gridspec_kw={'width_ratios': [2, 1]})

# Plot Radar Chart
ax1.set_title('Team Dynamics in Mythical Sports Championship\nPerformance Radar', fontsize=14, fontweight='bold', pad=20)
ax1.fill(angles, dragonfire, color='#FF6347', alpha=0.25)
ax1.plot(angles, dragonfire, color='#FF6347', linewidth=2, linestyle='solid')
ax1.fill(angles, elvenarchers, color='#8A2BE2', alpha=0.25)
ax1.plot(angles, elvenarchers, color='#8A2BE2', linewidth=2, linestyle='solid')
ax1.fill(angles, griffinriders, color='#3CB371', alpha=0.25)
ax1.plot(angles, griffinriders, color='#3CB371', linewidth=2, linestyle='solid')
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(metrics, fontsize=12, fontweight='bold')
ax1.set_yticklabels([])
ax1.set_ylim(0, 10)
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax1.spines['polar'].set_visible(False)
ax1.legend(labels=teams, loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Bar Chart for Overall Performance Scores
ax2 = plt.subplot(122)
ax2.bar(teams, scores, color=['#FF6347', '#8A2BE2', '#3CB371'], alpha=0.7)
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score', fontsize=12, fontweight='bold')
ax2.set_title('Overall Performance Scores', fontsize=14, fontweight='bold', pad=20)
for i, score in enumerate(scores):
    ax2.text(i, score + 0.1, f'{score:.2f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()