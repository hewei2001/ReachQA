import numpy as np
import matplotlib.pyplot as plt

# Categories of superhero abilities
categories = ['Strength', 'Speed', 'Intelligence', 'Durability', 'Power', 'Combat Skills']
N = len(categories)

# Superhero ability scores
captain_marvelous = [95, 70, 50, 90, 80, 85]
speedster = [60, 100, 55, 75, 95, 65]
brainiac = [45, 65, 100, 60, 70, 55]

# Append the first value to the end to close the radar charts
captain_marvelous += captain_marvelous[:1]
speedster += speedster[:1]
brainiac += brainiac[:1]

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Setup the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw each superhero's abilities on the radar chart
ax.fill(angles, captain_marvelous, color='skyblue', alpha=0.3)
ax.plot(angles, captain_marvelous, linewidth=2, label='Captain Marvelous', color='skyblue')

ax.fill(angles, speedster, color='orange', alpha=0.3)
ax.plot(angles, speedster, linewidth=2, label='Speedster', color='orange')

ax.fill(angles, brainiac, color='green', alpha=0.3)
ax.plot(angles, brainiac, linewidth=2, label='Brainiac', color='green')

# Customize the chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
ax.spines['polar'].set_visible(False)

# Add a title and legend
plt.title('Superhero Abilities Index:\nComparative Analysis of Power Profiles', size=15, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()