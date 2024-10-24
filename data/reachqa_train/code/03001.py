import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the data for various instruments
instruments = ['Violin', 'Cello', 'Flute', 'Trumpet', 'Clarinet', 'Oboe', 'Timpani', 'Harp']
resonance = np.array([8.0, 9.5, 5.0, 6.0, 7.5, 7.0, 3.0, 8.5])
pitch_range = np.array([5, 4, 3, 3, 3, 4, 2, 4])
volume = np.array([4, 5, 3, 6, 4, 4, 8, 4])
cultural_significance = np.array([200, 180, 120, 160, 140, 150, 100, 190])  # Adjusted for better visualization

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with varying sizes and colors
scatter = ax.scatter(resonance, pitch_range, volume, s=cultural_significance,
                     c=np.linspace(0, 1, len(instruments)), cmap='viridis', alpha=0.7, edgecolors='w')

# Add labels to each point
for i, instrument in enumerate(instruments):
    ax.text(resonance[i], pitch_range[i], volume[i], instrument, fontsize=10, ha='right')

# Set axes labels and title
ax.set_xlabel('Resonance Level', fontsize=12, labelpad=10)
ax.set_ylabel('Pitch Range', fontsize=12, labelpad=10)
ax.set_zlabel('Volume Level', fontsize=12, labelpad=10)
ax.set_title('The Cosmos of Classical Music:\n3D Visualization of Instrument Characteristics',
             fontsize=15, fontweight='bold', pad=20)

# Set axes limits for better clarity
ax.set_xlim(0, 10)
ax.set_ylim(1, 5)
ax.set_zlim(1, 10)

# Add a color bar to show the cultural significance scale
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Cultural Significance', rotation=270, labelpad=15)

# Adjust the viewing angle for better visualization
ax.view_init(elev=30, azim=120)

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()