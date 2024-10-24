import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the skills to evaluate
categories = ['Combat', 'Magic', 'Stealth', 'Leadership', 'Intelligence']
num_vars = len(categories)

# Skill levels for each character (on a scale from 1 to 10)
arin_skills = [9, 3, 5, 7, 6]
lira_skills = [4, 10, 6, 5, 8]
thorn_skills = [7, 4, 10, 4, 7]

# Create a 2D array for the skills of all characters
skills_data = [arin_skills, lira_skills, thorn_skills]

# Names of characters
characters = ["Arin the Brave", "Lira the Enchantress", "Thorn the Shadow"]

# Compute angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop by adding the first angle at the end

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one line per character
for i, character_skills in enumerate(skills_data):
    data = character_skills + character_skills[:1]  # Complete the loop by adding the first value at the end
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=characters[i])
    ax.fill(angles, data, alpha=0.2)  # Fill the area beneath each line

# Add labels for each category
plt.xticks(angles[:-1], categories)

# Adjust the range for y-axis
ax.set_rscale('linear')
ax.set_ylim(0, 10)

# Add a title
plt.title("Skill Assessment of Eldorian Heroes\nComparative Analysis of Legendary Figures", fontsize=14, pad=20)

# Add a legend with improved position to avoid overlap
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Optimize layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()