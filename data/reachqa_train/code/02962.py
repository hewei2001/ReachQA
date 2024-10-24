import matplotlib.pyplot as plt
import numpy as np

# Design Elements and corresponding Influence Scores
design_elements = ['Color', 'Texture', 'Form', 'Space', 'Balance', 'Movement']
influence_scores = [85, 60, 70, 55, 90, 65]

# Close the loop by adding the first element again
influence_scores += influence_scores[:1]
angles = np.linspace(0, 2 * np.pi, len(design_elements), endpoint=False).tolist()
angles += angles[:1]

# Create the figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one line per design element and fill area
ax.plot(angles, influence_scores, color='mediumslateblue', linewidth=2)
ax.fill(angles, influence_scores, color='mediumslateblue', alpha=0.4)

# Add labels for each axis
plt.xticks(angles[:-1], design_elements, color='darkslategray', size=12)

# Define y-ticks
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], color="grey", size=10)

# Set radial limit
ax.set_ylim(0, 100)

# Add a title with line breaks for readability
plt.title('The Creative Spectrum:\nDesign Elements in Modern Art', size=15, color='mediumslateblue', pad=20, weight='bold')

# Add a legend
ax.legend(['The Essence of Creativity'], loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Use tight layout to improve spacing
plt.tight_layout()

# Show the plot
plt.show()