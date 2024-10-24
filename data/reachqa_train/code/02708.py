import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the genres
genres = ['Mystery', 'Fantasy', 'Sci-Fi', 'Romance', 'Historical']

# Skills ratings for each author
alexander_skills = [9, 8, 6, 5, 7]
bianca_skills = [6, 5, 4, 9, 8]
christopher_skills = [8, 6, 9, 4, 5]

# Repeat the first value to close the circular graph
alexander_skills += alexander_skills[:1]
bianca_skills += bianca_skills[:1]
christopher_skills += christopher_skills[:1]

# Calculate angles for each axis
categories = len(genres)
angles = [n / float(categories) * 2 * pi for n in range(categories)]
angles += angles[:1]  # Repeat the first angle for closure

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each author's skills
for skills, name, color in zip(
        [alexander_skills, bianca_skills, christopher_skills],
        ['Alexander Storm', 'Bianca Frost', 'Christopher Gale'],
        ['#1f77b4', '#ff7f0e', '#2ca02c']):
    ax.plot(angles, skills, linewidth=2, linestyle='solid', label=name, color=color)
    ax.fill(angles, skills, color=color, alpha=0.25)

# Add labels and title
plt.xticks(angles[:-1], genres, color='black', size=10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='grey', size=8)
ax.set_title("Authorial Prowess:\nComparative Analysis of Fictional Authors Across Genres", size=16, pad=20)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()