import matplotlib.pyplot as plt
import numpy as np

# Define art movements and their corresponding color usage percentages
art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [20, 25, 18, 22, 15]  # Sum up to 100

# Colors associated with each art movement
colors = ['#003366', '#8B0000', '#FFD700', '#FFE4B5', '#4682B4']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), shadow=True, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

# Customize autotexts
plt.setp(autotexts, size=9, weight='bold', color='white')

# Title with artistic flair
plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold')

# Draw a circle at the center to create a donut effect
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Legend with more contextual info
ax.legend(wedges, [f'{movement}: {color} tones' for movement, color in zip(art_movements, ['Rich', 'Deep', 'Vibrant', 'Pastel', 'Bold'])],
          title="Art Movements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()