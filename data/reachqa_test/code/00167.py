import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Original Data
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010])
style_diversity = np.array([45, 55, 70, 60, 80, 90])
sustainability_index = np.array([10, 20, 30, 50, 70, 90])
color_palette_variety = np.array([5, 10, 15, 10, 20, 25]) * 10

# New data for additional plot: Calculating change rates (as percentage change)
change_style_diversity = np.diff(style_diversity) / style_diversity[:-1] * 100
change_sustainability_index = np.diff(sustainability_index) / sustainability_index[:-1] * 100
change_decades = decades[1:]  # For the change rates

# Create subplots
fig = plt.figure(figsize=(16, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# 3D Scatter Plot
sc = ax1.scatter(decades, style_diversity, sustainability_index, s=color_palette_variety,
                 c=style_diversity, cmap='plasma', alpha=0.7, edgecolors='w', linewidth=0.5)

ax1.set_title('Diversity of Global Fashion Trends\nOver the Decades', fontsize=14, pad=20)
ax1.set_xlabel('Decade', fontsize=12, labelpad=10)
ax1.set_ylabel('Style Diversity (0-100)', fontsize=12, labelpad=10)
ax1.set_zlabel('Sustainability Index (0-100)', fontsize=12, labelpad=10)

ax1.set_xticks(decades)
ax1.set_xticklabels([f'{dec}s' for dec in decades])
ax1.set_yticks(np.arange(0, 101, 20))
ax1.set_zticks(np.arange(0, 101, 20))

cbar = plt.colorbar(sc, ax=ax1, pad=0.1, fraction=0.03)
cbar.set_label('Style Diversity Intensity', fontsize=10)

ax1.view_init(elev=25, azim=120)

# 2D Line Plot for Change Rates
ax2.plot(change_decades, change_style_diversity, marker='o', linestyle='-', color='tab:blue', label='Style Diversity Change (%)')
ax2.plot(change_decades, change_sustainability_index, marker='s', linestyle='--', color='tab:green', label='Sustainability Index Change (%)')

ax2.set_title('Change Rate of Fashion Trends\nAcross Decades', fontsize=14)
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('Change Rate (%)', fontsize=12)

ax2.set_xticks(change_decades)
ax2.set_xticklabels([f'{dec}s' for dec in change_decades])
ax2.legend(loc='upper left', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Display the plots
plt.show()