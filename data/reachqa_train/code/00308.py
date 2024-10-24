import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.colors as mcolors

# Exoplanet data
exoplanets = ['Xeno 1', 'Nexus 2', 'Terra Nova', 'Zypher', 'Cosmo Prime',
              'Artemis', 'Elysium', 'Solaria', 'Arcadia', 'Veridian']

# Distances from Earth (in light-years)
distances = np.array([4.2, 8.6, 15.3, 20.7, 22.5, 28.4, 30.1, 35.0, 38.7, 40.0])

# Estimated sizes (in Earth Masses)
sizes = np.array([0.9, 1.1, 1.3, 2.0, 1.8, 1.0, 2.5, 0.8, 1.6, 1.4])

# Habitability scores (on a scale of 0 to 1)
habitability_scores = np.array([0.8, 0.6, 0.9, 0.4, 0.5, 0.7, 0.3, 0.2, 0.6, 0.1])

# Bubble sizes (scaling factor for better visualization)
bubble_sizes = sizes * 150

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d', facecolor='lightblue')

# Plotting the data
scatter = ax.scatter(distances, sizes, habitability_scores, s=bubble_sizes, c=habitability_scores,
                     cmap='plasma', alpha=0.85, edgecolors='w', linewidth=0.5)

# Setting labels and title
ax.set_title('Exoplanet Exploration:\nEvaluating Promising Targets in the Universe', fontsize=16, pad=30)
ax.set_xlabel('Distance from Earth\n(light-years)', fontsize=12, labelpad=10)
ax.set_ylabel('Estimated Size\n(Earth Masses)', fontsize=12, labelpad=10)
ax.set_zlabel('Habitability Score', fontsize=12, labelpad=10)

# Adding color bar for habitability score
color_bar = fig.colorbar(scatter, ax=ax, pad=0.1)
color_bar.set_label('Habitability Score', fontsize=12)

# Annotating each exoplanet with its name
for i, planet in enumerate(exoplanets):
    ax.text(distances[i], sizes[i], habitability_scores[i] + 0.03, planet, fontsize=9, color='navy', ha='center')

# Adjust the view angle for better perspective
ax.view_init(elev=30, azim=60)

# Enhanced grid and background
ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.set_facecolor('aliceblue')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()