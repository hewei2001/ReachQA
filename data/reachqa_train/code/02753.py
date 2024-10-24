import matplotlib.pyplot as plt
import numpy as np

# Data: Distances from the star (AU) and Habitability Index scores
# Planets' names correspond to different star systems
star_systems = ['Proxima b', 'Kepler-442b', 'Trappist-1e', 'Kepler-452b', 'Gliese 581g',
                'Tau Ceti e', 'Luyten b', 'HD 40307g', 'K2-18b', 'Wolf 1061c']

distances = np.array([0.0485, 1.120, 0.029, 1.046, 0.146, 0.552, 0.091, 0.600, 0.142, 0.084])
habitability_index = np.array([0.8, 0.9, 0.85, 0.88, 0.82, 0.77, 0.79, 0.74, 0.80, 0.81])
sizes = np.array([150, 200, 180, 220, 170, 140, 130, 160, 175, 165])  # Bubble sizes for aesthetic

# Create the scatter plot
plt.figure(figsize=(14, 8))
scatter = plt.scatter(distances, habitability_index, s=sizes, c=habitability_index, cmap='viridis', alpha=0.8, edgecolors='w')

# Annotate each point with planet's name
for i, txt in enumerate(star_systems):
    plt.annotate(txt, (distances[i], habitability_index[i]), fontsize=9, ha='right', weight='bold')

# Adding a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Habitability Index Score', rotation=270, labelpad=15, fontsize=12, weight='bold')

# Titles and labels
plt.title('Exploring Habitability of Exoplanets\nRelation Between Distance from Star and Habitability Index', 
          fontsize=16, weight='bold', pad=20)
plt.xlabel('Distance from Star (AU)', fontsize=14, weight='bold')
plt.ylabel('Habitability Index Score', fontsize=14, weight='bold')

# Enhancing plot style
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()