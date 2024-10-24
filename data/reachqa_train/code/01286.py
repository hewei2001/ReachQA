import matplotlib.pyplot as plt
import numpy as np

# Expanded dataset
genres = [
    'Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 
    'Mystery/Thriller', 'Romance', 'Historical', 'Biography',
    'Self-Help', 'Health & Wellness', 'Science', 'Adventure', 
    'Travel', 'Children', 'Poetry'
]
preferences = np.array([18, 14, 12, 11, 9, 8, 7, 5, 4, 3, 3, 2, 2, 1, 1])

# Define a broader range of colors
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
    '#c4e17f', '#ff6666', '#ffccff', '#ccccff', '#99cccc', '#99ccff',
    '#ffcc80', '#d9b3ff', '#ffb3b3'
]

# Create the donut pie chart with exploded wedges
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    preferences, 
    labels=genres, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w'), 
    explode=[0.05] * len(genres)
)

# Draw a white circle at the center to convert the pie into a donut
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Customize labels and percentage text for clarity
plt.setp(autotexts, size=8, weight='bold', color='black')
plt.setp(texts, size=10, weight='bold')

# Multi-line title
title = "An Intricate Study of Book Genres\nReader Preferences in the Digital Era"
ax.set_title(title, fontsize=14, fontweight='bold', loc='center', pad=20)

# Enhanced legend, placed outside the pie
ax.legend(wedges, genres, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()