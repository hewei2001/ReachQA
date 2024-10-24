import matplotlib.pyplot as plt
import numpy as np

# Define skill categories for the radar chart
skills = ['Creativity', 'Technical Skill', 'Collaboration', 
          'Communication', 'Adaptability', 'Cultural Awareness', 
          'Critical Thinking']

# Scores for two profiles in "The Artistry Collective"
artist_a = [8, 7, 6, 7, 5, 6, 8]  # Scores out of 10 for Artist A
artist_b = [6, 8, 7, 5, 8, 7, 6]  # Scores out of 10 for Artist B

# Number of skills
num_skills = len(skills)

# Calculate the angle for each skill on the plot
angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

# Complete the loop by appending the start point to the end
artist_a += artist_a[:1]
artist_b += artist_b[:1]
angles += angles[:1]

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each artist
ax.fill(angles, artist_a, color='skyblue', alpha=0.4, linewidth=2, linestyle='solid', label='Artist A')
ax.fill(angles, artist_b, color='orange', alpha=0.4, linewidth=2, linestyle='solid', label='Artist B')

# Draw skill category labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=10, weight='bold')

# Add a title and customize
plt.title("Skill Profiles in The Artistry Collective", 
          size=15, color='navy', weight='bold', pad=20)

# Add a legend with specific title
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), 
           title="Profiles", fontsize='small', title_fontsize='12')

# Customize grid and spine
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_linewidth(1)
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()