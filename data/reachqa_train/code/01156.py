import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories (traits) and the number of variables (spokes)
categories = ['Imagination', 'Humor', 'Clarity', 'Emotional Depth', 'Narrative Innovation']
n_categories = len(categories)

# Create the data for each author
authors = {
    'Edith Prose': [9, 5, 8, 7, 6],
    'Mark Jest': [6, 9, 6, 5, 7],
    'Clara Sentence': [7, 6, 9, 6, 6],
    'Emo Noir': [5, 6, 7, 9, 5],
    'Nova Plot': [6, 7, 5, 6, 9]
}

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Calculate the angles for each axis
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Plot each author's traits
for author, scores in authors.items():
    scores += scores[:1]  # Complete the loop for the radar chart
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=author)
    ax.fill(angles, scores, alpha=0.1)

# Add labels for each category
plt.xticks(angles[:-1], categories, fontsize=11)

# Set up the range for each axis
ax.set_yticklabels([])  # Remove y-tick labels for a cleaner look
plt.yticks([2, 4, 6, 8, 10], ['2', '4', '6', '8', '10'], color="grey", size=8)
plt.ylim(0, 10)

# Add a legend and title
plt.title("Creative Traits of Renowned Authors\nA Comparative Analysis", size=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize='small')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()