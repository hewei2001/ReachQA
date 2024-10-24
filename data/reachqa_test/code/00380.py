import matplotlib.pyplot as plt
import numpy as np

# Skills and their respective scores for Fashion Designer and Software Engineer
skills = ['Creativity', 'Technical Skills', 'Communication', 'Business Acumen', 'Attention to Detail', 
          'Time Management', 'Problem Solving', 'Data Analysis', 'Teamwork', 'Leadership', 'Adaptability', 'Innovation']

# Adjusted scores for better contrast
fashion_designer_scores = [9, 6, 7, 5, 9, 8, 6, 4, 7, 5, 9, 8]
software_engineer_scores = [5, 9, 6, 7, 7, 6, 9, 9, 6, 8, 5, 6]

# Define angles for each skill
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()

# Close the loop
scores_fs = fashion_designer_scores + [fashion_designer_scores[0]]
scores_se = software_engineer_scores + [software_engineer_scores[0]]
angles += angles[:1]

# Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'polar': True})

# Plot for Fashion Designer
ax1.plot(angles, scores_fs, 'o-', linewidth=2, color='blue', label='Fashion Designer')
ax1.fill(angles, scores_fs, color='blue', alpha=0.25)
ax1.set_ylim(0, 10)
ax1.set_yticks(range(0, 11, 2))
ax1.set_title('Skills of a Successful\nFashion Designer', fontsize=14)
ax1.set_thetagrids(np.degrees(angles[:-1]), skills, fontsize=10)
ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

# Plot for Software Engineer
ax2.plot(angles, scores_se, 'o-', linewidth=2, color='red', label='Software Engineer')
ax2.fill(angles, scores_se, color='red', alpha=0.25)
ax2.set_ylim(0, 10)
ax2.set_yticks(range(0, 11, 2))
ax2.set_title('Skills of a Successful\nSoftware Engineer', fontsize=14)
ax2.set_thetagrids(np.degrees(angles[:-1]), skills, fontsize=10)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
