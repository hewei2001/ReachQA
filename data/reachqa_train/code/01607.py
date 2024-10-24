import numpy as np
import matplotlib.pyplot as plt

# Skill areas for the radar chart
skills = [
    "Classic Cooking", 
    "Fusion Cooking", 
    "Baking & Pastry", 
    "Presentation",
    "Molecular Gastronomy", 
    "Sustainability"
]

# Define the proficiency scores for each chef persona
traditionalist_skills = [9, 4, 8, 6, 3, 7]
fusion_expert_skills = [5, 9, 6, 8, 7, 6]
tech_gourmet_skills = [3, 5, 7, 8, 9, 5]

# Number of skills
num_skills = len(skills)

# Create an angle for each skill and ensure the chart closes by repeating the start
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Data preparation for closing the radar chart
traditionalist_skills += traditionalist_skills[:1]
fusion_expert_skills += fusion_expert_skills[:1]
tech_gourmet_skills += tech_gourmet_skills[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plotting each persona's data with different colors and transparency
ax.fill(angles, traditionalist_skills, color='b', alpha=0.25, label='Traditionalist')
ax.fill(angles, fusion_expert_skills, color='r', alpha=0.25, label='Fusion Expert')
ax.fill(angles, tech_gourmet_skills, color='g', alpha=0.25, label='Tech Gourmet')

# Add lines and markers for better readability
ax.plot(angles, traditionalist_skills, color='b', linewidth=1.5)
ax.plot(angles, fusion_expert_skills, color='r', linewidth=1.5)
ax.plot(angles, tech_gourmet_skills, color='g', linewidth=1.5)

# Adding skill areas as tick labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='gray')

# Add labels and a title, breaking the title into two lines for better clarity
plt.title('Innovative Cuisine: Culinary Skill Set Radar\nfor Emerging Chefs in 2023',
          size=15, color='darkslategray', ha='center', va='bottom', pad=20)

# Add a legend outside the radar chart
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust the layout to ensure no overlap of elements
plt.tight_layout()

# Display the radar chart
plt.show()