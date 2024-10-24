import matplotlib.pyplot as plt
import numpy as np

# Define the skills and number of skills
skills = ['Swordsmanship', 'Archery', 'Magic', 'Stealth', 'Crafting', 'Charisma']
num_skills = len(skills)

# Define skill values for each character class
knight_skills = [9, 4, 3, 2, 5, 8]
archer_skills = [5, 9, 4, 8, 5, 6]
mage_skills = [2, 3, 10, 4, 7, 5]

# Create an array of angles for the radar chart
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

# Complete the loop for the radar chart by connecting the first and last points
knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
mage_skills += mage_skills[:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f7f9f9')  # Set subtle background color for the figure

# Plot each character class
ax.fill(angles, knight_skills, color='tab:red', alpha=0.25, label='Knight')
ax.plot(angles, knight_skills, color='tab:red', linewidth=1.5)

ax.fill(angles, archer_skills, color='tab:green', alpha=0.25, label='Archer')
ax.plot(angles, archer_skills, color='tab:green', linewidth=1.5)

ax.fill(angles, mage_skills, color='tab:blue', alpha=0.25, label='Mage')
ax.plot(angles, mage_skills, color='tab:blue', linewidth=1.5)

# Add labels for each axis
ax.set_yticklabels([])  # Hide radial labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12)

# Add a title and legend
ax.set_title('Character Skill Distribution\nin "Lands of Mythoria"', fontsize=15, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Adjust layout
plt.tight_layout()

# Show the radar chart
plt.show()