import matplotlib.pyplot as plt
import numpy as np

# Define the fashion styles and regions
styles = ['Vintage', 'Bohemian', 'Minimalist', 'Avant-Garde', 'Streetwear']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Artificial data: rows for styles, columns for regions
# Values indicate the prominence of each style in each region
prominence_data = np.array([
    [8, 5, 6, 4, 3],   # Vintage
    [3, 7, 5, 6, 4],   # Bohemian
    [4, 3, 9, 5, 6],   # Minimalist
    [6, 8, 2, 4, 7],   # Avant-Garde
    [5, 6, 8, 7, 9]    # Streetwear
])

# Create a heat map
fig, ax = plt.subplots(figsize=(12, 7))
cax = ax.imshow(prominence_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Set the ticks and labels for the axes
ax.set_xticks(np.arange(len(regions)))
ax.set_yticks(np.arange(len(styles)))
ax.set_xticklabels(regions)
ax.set_yticklabels(styles)

# Rotate the tick labels for better readability and reduce font size
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Add color bar to indicate prominence scale
cbar = ax.figure.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Prominence Scale', rotation=270, labelpad=15)

# Loop over data dimensions and create text annotations
for i in range(len(styles)):
    for j in range(len(regions)):
        ax.text(j, i, f'{prominence_data[i, j]}', ha='center', va='center', color='black', fontsize=9)

# Title and layout adjustments
plt.title('The Evolution of Global Fashion Styles\nFrom the 1950s to the 2020s', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()

# Show the plot
plt.show()