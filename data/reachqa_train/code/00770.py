import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define habitats and crops
habitats = ['Dome Alpha', 'Crater Beta', 'Valley Gamma', 'Lava Tube Delta']
crops = ['Potatoes', 'Wheat', 'Barley', 'Soybeans']

# Percentage contribution of crop yields from each habitat
# Rows represent habitats, columns represent crops
crop_data = np.array([
    [30, 40, 20, 10],  # Dome Alpha
    [25, 20, 35, 20],  # Crater Beta
    [20, 25, 15, 40],  # Valley Gamma
    [25, 15, 30, 30],  # Lava Tube Delta
])

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define colors for different habitats
colors = ['#e63946', '#f4a261', '#2a9d8f', '#264653']

# Generate x positions for each crop and y positions for each habitat
xpos = np.arange(len(crops))
ypos = np.arange(len(habitats))
xposM, yposM = np.meshgrid(xpos, ypos, indexing="ij")

# Flatten xpos and ypos for the bar3d function
xposM = xposM.ravel()
yposM = yposM.ravel()

# The percentage height for each habitat-crop pair
zpos = np.zeros_like(xposM)
dz = crop_data.ravel()

# Plot bars for each habitat-crop pair
ax.bar3d(xposM, yposM, zpos, 0.5, 0.5, dz, color=np.repeat(colors, len(crops)), alpha=0.8, edgecolor='black')

# Customize axes
ax.set_xlabel('Crops', labelpad=10)
ax.set_ylabel('Habitats', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(xpos)
ax.set_xticklabels(crops, rotation=45, ha='right')
ax.set_yticks(ypos)
ax.set_yticklabels(habitats)
ax.set_zlim(0, 50)

# Set the viewing angle
ax.view_init(elev=25, azim=135)

# Add a descriptive title
ax.set_title('Martian Crop Yield Distribution\nAcross Various Habitats (2050)', fontsize=16, fontweight='bold')

# Create a custom legend
legend_handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(legend_handles, habitats, loc='upper right', title='Habitats', bbox_to_anchor=(1.15, 0.9))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()