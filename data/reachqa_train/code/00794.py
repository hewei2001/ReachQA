import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Define art movements and their corresponding color usage percentages
art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [20, 25, 18, 22, 15]  # Sum up to 100

# Colors with gradients
colors = ['#003366', '#8B0000', '#FFD700', '#FFE4B5', '#4682B4']
patterns = ['//', '\\\\', '..', 'oo', '++']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    color_usage, 
    labels=art_movements, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linestyle='--', hatch=patterns, linewidth=1.5),
    shadow=True, 
    explode=(0.05,) * len(art_movements)
)

# Customize autotexts and wedge labels
plt.setp(autotexts, size=9, weight='bold', color='white')
plt.setp(texts, size=11, style='italic')

# Title with artistic flair
plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold', family='serif')

# Draw a circle at the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.7, fc='white', edgecolor='black', lw=1.5)
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Legend with contextual info and matching pattern
legend_labels = [f'{movement}: {color}' for movement, color in zip(art_movements, ['Rich', 'Deep', 'Vibrant', 'Pastel', 'Bold'])]
ax.legend(
    wedges, legend_labels, 
    title="Art Movements", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=9
)

# Adding annotations for each segment
annotations = [
    "Era of rebirth and classical influence",
    "Excessive ornamentation and grandeur",
    "Emphasis on emotion and individualism",
    "Light and color nuances with rapid brushwork",
    "Modern innovations and diverse expressions"
]
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = 1.1 * np.cos(np.radians(angle))
    y = 1.1 * np.sin(np.radians(angle))
    ax.annotate(
        annotations[i], xy=(x, y), xytext=(x*1.25, y*1.25),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"), fontsize=9, family='serif'
    )

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()