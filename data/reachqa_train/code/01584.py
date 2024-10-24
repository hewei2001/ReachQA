import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Data preparation
genres = [
    'Fiction', 
    'Non-Fiction', 
    'Mystery/Thriller', 
    'Science Fiction/Fantasy', 
    'Romance', 
    'Historical', 
    'Young Adult'
]

popularity = [25, 20, 15, 15, 10, 8, 7]

# Enhanced color scheme using a gradient colormap
colors = cm.viridis(np.linspace(0, 1, len(genres)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=[f'{genre}\n{pop}%' for genre, pop in zip(genres, popularity)], 
    colors=colors, 
    autopct=lambda p: f'{p:.1f}%', 
    startangle=140,
    pctdistance=0.8, 
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Draw circle for the donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Add additional information in the center
ax.text(0, 0, 'Book\nGenres\n2023', horizontalalignment='center',
        verticalalignment='center', fontsize=12, weight='bold', color='gray')

# Set title with styling
ax.set_title('Global Book Genre Popularity in 2023\nInsightful Statistics', fontsize=14, weight='bold', pad=20)

# Adjust the legend
ax.legend(
    wedges, 
    genres, 
    title="Genres", 
    title_fontsize='13', 
    fontsize='11', 
    loc='center left', 
    bbox_to_anchor=(1, 0.5),
    frameon=False
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()