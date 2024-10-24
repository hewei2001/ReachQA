import matplotlib.pyplot as plt
import numpy as np

# Define the skills and genres
skills = ['Creativity', 'Critical Thinking', 'Empathy', 'Vocabulary', 'Cultural Awareness']
genres = ['Fiction', 'Non-Fiction', 'Poetry', 'Drama']

# Data: Skill development scores for each genre
data = {
    'Fiction': [8, 7, 9, 6, 5],
    'Non-Fiction': [5, 9, 5, 7, 8],
    'Poetry': [9, 6, 8, 5, 7],
    'Drama': [6, 8, 7, 5, 9],
}

# Number of variables
N = len(skills)

# Calculate angles for each skill
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# Append first skill score to close the chart
for genre in data:
    data[genre].append(data[genre][0])

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each genre
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']
for i, (genre, values) in enumerate(data.items()):
    ax.fill(angles, values, color=colors[i], alpha=0.25, label=genre)
    ax.plot(angles, values, color=colors[i], linewidth=2)

# Add labels for each skill
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=11)

# Title and legend
plt.title("Exploring Literary Skills:\nHow Different Genres Foster Diverse Abilities", size=16, fontweight='bold', va='bottom', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), title='Literary Genres', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()