import matplotlib.pyplot as plt
import numpy as np

# Data setup
libraries = ['Ancient Archives', 'Renaissance Repository', 'Modern Manuscript']
genres = ['Fiction', 'Non-Fiction', 'Poetry', 'Drama']
percentage_data = np.array([
    [30, 40, 20, 10],  # Ancient Archives
    [25, 35, 30, 10],  # Renaissance Repository
    [40, 20, 20, 20],  # Modern Manuscript Collection
])

# Create figure and 3D axes
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

# Define bar positions
num_libraries = len(libraries)
num_genres = len(genres)
xpos, ypos = np.meshgrid(np.arange(num_genres), np.arange(num_libraries))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

# Define bar sizes and gradients
dx = dy = 0.8
dz = percentage_data.flatten()
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Plot bars with gradients
for i in range(len(xpos)):
    bar = ax.bar3d(xpos[i], ypos[i], zpos[i], dx, dy, dz[i], 
                   color=colors[i % len(colors)], zsort='average', alpha=0.9, edgecolor='k')
    # Add data labels
    ax.text(xpos[i] + dx/2, ypos[i] + dy/2, dz[i] + 2, f'{dz[i]}%', 
            ha='center', va='bottom', fontsize=9, color='black')

# Customize the axes
ax.set_xticks(np.arange(num_genres))
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(num_libraries))
ax.set_yticklabels(libraries, fontsize=10)
ax.set_zlim(0, 50)
ax.set_zlabel('Percentage (%)', fontsize=12)

# Improve aesthetics
ax.grid(False)  # Turn off grid for cleaner aesthetics
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

# Title and legend
ax.set_title(
    'Literary Genre Distribution\nAcross the Libraries of Time',
    fontsize=16, fontweight='bold', pad=30
)
ax.view_init(elev=30, azim=120)

# Add legend with genre colors
proxy_rects = [plt.Rectangle((0,0),1,1,fc=color) for color in colors]
ax.legend(proxy_rects, genres, title='Genre', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()