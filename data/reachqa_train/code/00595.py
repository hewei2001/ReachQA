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
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f7f9f9')

# Grid customization
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Add fill for each character class with gradient effect
ax.fill(angles, knight_skills, color='tab:red', alpha=0.1)
ax.plot(angles, knight_skills, color='tab:red', linewidth=2, linestyle='dashed', label='Knight')

ax.fill(angles, archer_skills, color='tab:green', alpha=0.1)
ax.plot(angles, archer_skills, color='tab:green', linewidth=2, linestyle='dashed', label='Archer')

ax.fill(angles, mage_skills, color='tab:blue', alpha=0.1)
ax.plot(angles, mage_skills, color='tab:blue', linewidth=2, linestyle='dashed', label='Mage')

# Add labels for each axis
ax.set_yticklabels(['Low', '', '', 'Medium', '', '', 'High'], fontsize=10, color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='black')

# Annotations for special skills
ax.annotate('Top Magic', xy=(angles[2], mage_skills[2]), xytext=(angles[2], mage_skills[2] + 2),
            arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='darkblue')

# Title and legend adjustments
ax.set_title('Character Skill Distribution\nin "Lands of Mythoria"',
             fontsize=16, fontweight='bold', color='darkgreen', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), frameon=False, fontsize=11)

# Tight layout adjustment
plt.tight_layout()

# Display the radar chart
plt.show()