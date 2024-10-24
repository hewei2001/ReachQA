import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Define the fashion styles and regions
styles = ['Vintage', 'Bohemian', 'Minimalist', 'Avant-Garde', 'Streetwear']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Artificial data: rows for styles, columns for regions
prominence_data = np.array([
    [8, 5, 6, 4, 3],   # Vintage
    [3, 7, 5, 6, 4],   # Bohemian
    [4, 3, 9, 5, 6],   # Minimalist
    [6, 8, 2, 4, 7],   # Avant-Garde
    [5, 6, 8, 7, 9]    # Streetwear
])

# Set up the figure with grid layout for subplot
fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])

# Main heatmap plot
ax0 = plt.subplot(gs[0])
cax = ax0.imshow(prominence_data, cmap='viridis', aspect='auto', interpolation='nearest')

# Set ticks and labels
ax0.set_xticks(np.arange(len(regions)))
ax0.set_yticks(np.arange(len(styles)))
ax0.set_xticklabels(regions, fontsize=10, fontstyle='italic', rotation=45, ha='right')
ax0.set_yticklabels(styles, fontsize=10, fontweight='bold')

# Add grid lines for clarity
ax0.grid(which='minor', color='white', linestyle='-', linewidth=2)
ax0.set_xticks(np.arange(-.5, len(regions), 1), minor=True)
ax0.set_yticks(np.arange(-.5, len(styles), 1), minor=True)

# Add color bar with detailed ticks
cbar = ax0.figure.colorbar(cax, ax=ax0, orientation='vertical')
cbar.set_label('Prominence Scale', rotation=270, labelpad=15, fontsize=12)
cbar.set_ticks([2, 4, 6, 8, 10])

# Annotate heatmap values
for i in range(len(styles)):
    for j in range(len(regions)):
        ax0.text(j, i, f'{prominence_data[i, j]}', ha='center', va='center', color='black', fontsize=9)

# Additional plot: Histogram to show prominence distribution
ax1 = plt.subplot(gs[1])
ax1.barh(styles, np.sum(prominence_data, axis=1), color='slateblue', alpha=0.7)
ax1.set_title('Total Style Prominence', fontsize=12, fontweight='bold')
ax1.set_xlabel('Total Score', fontsize=10)
ax1.set_xlim(0, max(np.sum(prominence_data, axis=1)) + 5)

# Main title for the chart
fig.suptitle('The Evolution of Global Fashion Styles\nFrom the 1950s to the 2020s', fontsize=14, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()