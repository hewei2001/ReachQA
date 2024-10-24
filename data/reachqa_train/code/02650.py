import matplotlib.pyplot as plt
import numpy as np

# Define the labels for each spoke (attribute)
labels = np.array(['Strength', 'Intelligence', 'Speed', 'Endurance', 'Agility'])
num_vars = len(labels)

# Scores for each superhero
scores = np.array([
    [8, 5, 9, 6, 7],  # Thunderbolt
    [4, 9, 5, 7, 6],  # Brainwave
    [6, 7, 10, 5, 8], # Flashwing
    [9, 6, 4, 9, 5]   # Stoneheart
])

# Names of the superheroes
superheroes = ['Thunderbolt', 'Brainwave', 'Flashwing', 'Stoneheart']

# Create the angle for each axis in the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
scores = np.concatenate((scores, scores[:, [0]]), axis=1)  # Close the plot
angles += angles[:1]  # Ensure the radar chart is a closed loop

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Plot each superhero
for idx, score in enumerate(scores):
    ax.fill(angles, score, color=colors[idx], alpha=0.25, label=superheroes[idx])
    ax.plot(angles, score, color=colors[idx], linewidth=2)

# Set the labels for each angle
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, size=10, weight='bold')

# Title and legend configuration
plt.title("Comparative Skill Sets of Superheroes", size=15, weight='bold', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()