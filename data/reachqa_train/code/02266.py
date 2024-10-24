import matplotlib.pyplot as plt
import numpy as np

# Fantasy genre labels and their respective popularity percentage
genres = ['High Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Epic Fantasy', 'Fairy Tales']
votes_percentage = [30, 20, 15, 25, 10]

# Define colors for each segment
colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9370DB']

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot donut pie chart
wedges, texts, autotexts = ax.pie(
    votes_percentage,
    labels=genres,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=[0.1, 0, 0, 0.1, 0]
)

# Draw a circle in the center to enhance the donut appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set equal aspect ratio for a perfect circle
ax.axis('equal')

# Customize text appearance
plt.setp(autotexts, size=10, weight='bold', color='navy')
plt.setp(texts, size=11, weight='bold')

# Add title with line break for readability
plt.title(
    "Popularity of Fantasy Book Genres:\n"
    "A Literary Exploration",
    fontsize=15, weight='bold', color='teal', pad=20
)

# Create a legend positioned to avoid chart overlap
ax.legend(
    wedges, genres,
    title="Genres",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Automatically adjust subplot parameters for a cleaner layout
plt.tight_layout()

# Display the chart
plt.show()