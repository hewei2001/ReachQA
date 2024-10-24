import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define celestial civilizations and their properties
civilizations = ['Andromeda', 'Cygnus', 'Orion', 'Cassiopeia', 'Draco',
                 'Pegasus', 'Phoenix', 'Hercules', 'Perseus', 'Lynx']
distances = np.array([2.5, 4.3, 5.6, 8.1, 7.2, 3.2, 5.5, 9.0, 6.0, 10.2])  # in light years
frequency_bands = np.array([1.2, 2.5, 3.8, 4.1, 2.9, 2.0, 3.0, 4.5, 3.6, 5.0])  # in GHz
signal_strengths = np.array([50, 80, 30, 100, 60, 45, 55, 90, 40, 85])  # arbitrary units
tech_levels = np.array([3, 5, 2, 6, 4, 3, 4, 6, 3, 5])  # Technological advancement level

# Create a 3D scatter plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with an additional variable influencing color
scatter = ax.scatter(distances, frequency_bands, signal_strengths, 
                     s=signal_strengths*10, c=tech_levels, 
                     cmap='viridis', alpha=0.8, edgecolors='k', linewidth=0.5)

# Annotate points with civilization names
for i, civilization in enumerate(civilizations):
    ax.text(distances[i], frequency_bands[i], signal_strengths[i], civilization, 
            fontsize=8, fontweight='bold', ha='right', va='bottom',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.2'))

# Set labels and title
ax.set_xlabel('Distance from Earth (light years)', fontsize=10)
ax.set_ylabel('Frequency Band (GHz)', fontsize=10)
ax.set_zlabel('Signal Strength', fontsize=10)
ax.set_title('Cosmic Communication Channels:\nStrength, Distance, and Technological Advancement', 
             fontsize=16, fontweight='bold', pad=30)

# Customize the view
ax.view_init(elev=30, azim=130)

# Add color bar to indicate technological level
color_bar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
color_bar.set_label('Technological Level', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()