import matplotlib.pyplot as plt
import numpy as np

# Define the character classes and their respective attribute scores
labels = ['Strength', 'Intelligence', 'Agility', 'Endurance', 'Charisma']
num_vars = len(labels)

# Create the data for each class
warrior_stats = [9, 3, 6, 8, 4]
wizard_stats = [3, 9, 5, 5, 8]
rogue_stats = [5, 5, 9, 4, 7]

# Completing the loop for each class
warrior_stats += warrior_stats[:1]
wizard_stats += wizard_stats[:1]
rogue_stats += rogue_stats[:1]

# Calculate angles for each axis in the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Completing the loop

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot data and fill area for each character class
ax.fill(angles, warrior_stats, color='red', alpha=0.25, label='Warrior')
ax.fill(angles, wizard_stats, color='blue', alpha=0.25, label='Wizard')
ax.fill(angles, rogue_stats, color='green', alpha=0.25, label='Rogue')

ax.plot(angles, warrior_stats, color='red', linewidth=1.5)
ax.plot(angles, wizard_stats, color='blue', linewidth=1.5)
ax.plot(angles, rogue_stats, color='green', linewidth=1.5)

# Configure the chart with labels and title
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)

plt.title('Fantasy RPG Character Classes\nAttribute Distribution', fontsize=16, fontweight='bold', va='bottom')

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()