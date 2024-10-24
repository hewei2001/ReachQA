import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Libraries and centuries
libraries = ['Arcane Archives', 'Celestial Codices', 'Enchanted Encyclopedias']
centuries = ['15th', '17th', '19th']

# Number of magical manuscripts discovered
manuscripts = np.array([
    [120, 230, 340],  # Arcane Archives
    [150, 190, 260],  # Celestial Codices
    [180, 160, 300]   # Enchanted Encyclopedias
])

# Plotting the 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Defining positions
_x = np.arange(len(libraries))
_y = np.arange(len(centuries))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Bar heights and positions
z = np.zeros_like(x)
dx = dy = 0.4
dz = manuscripts.T.ravel()

# Colors for bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create bars
ax.bar3d(x, y, z, dx, dy, dz, color=np.repeat(colors, len(libraries)), alpha=0.8)

# Title and labels
ax.set_title('Mystical Manuscript Discoveries\nin Mystical Libraries Across Centuries', pad=20, fontsize=16, fontweight='bold')
ax.set_xlabel('Library', fontsize=12)
ax.set_ylabel('Century', fontsize=12)
ax.set_zlabel('Number of Manuscripts', fontsize=12)

# Custom ticks
ax.set_xticks(np.arange(len(libraries)))
ax.set_xticklabels(libraries, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(centuries)))
ax.set_yticklabels(centuries, fontsize=10)

# Adjusting viewing angle for better visibility
ax.view_init(elev=20, azim=135)

# Custom legend
handles = [plt.Rectangle((0,0),1,1, color=color, alpha=0.8) for color in colors]
ax.legend(handles, centuries, loc='upper left', title='Century', fontsize=10, title_fontsize=12)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()