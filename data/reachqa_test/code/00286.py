import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

# Define constellations and months
constellations = ['Orion', 'Ursa Major', 'Scorpius', 'Leo', 'Cassiopeia', 'Aquarius', 'Pegasus']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Visibility data
visibility_scores = np.array([
    [8, 9, 10, 7, 5, 3, 2, 1, 2, 4, 6, 7],  # Orion
    [6, 7, 8, 9, 10, 8, 5, 4, 5, 6, 7, 8],  # Ursa Major
    [1, 2, 3, 6, 8, 9, 10, 8, 6, 4, 3, 2],  # Scorpius
    [4, 5, 7, 8, 10, 9, 8, 6, 5, 4, 3, 2],  # Leo
    [7, 8, 7, 6, 5, 4, 3, 4, 6, 8, 9, 10],  # Cassiopeia
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7],  # Aquarius
    [3, 2, 4, 5, 6, 7, 8, 10, 9, 8, 7, 6]   # Pegasus
])

# Calculate average visibility per constellation
avg_visibility = visibility_scores.mean(axis=1)

# Create a figure with a grid layout
fig = plt.figure(figsize=(14, 10))
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])

# Plot the heatmap
ax0 = plt.subplot(gs[0])
im = ax0.imshow(visibility_scores, aspect='auto', cmap='coolwarm', interpolation='nearest')

# Enhanced titles and labels
ax0.set_title('Navigating the Stars:\nCelestial Observations in the Ancient Astrologers\' Guild', fontsize=18, fontweight='bold', pad=20)
ax0.set_xlabel('Months', fontsize=12, labelpad=10)
ax0.set_ylabel('Constellations', fontsize=12, labelpad=10)

# Set ticks with improved spacing
ax0.set_xticks(np.arange(len(months)))
ax0.set_yticks(np.arange(len(constellations)))
ax0.set_xticklabels(months, rotation=45, ha='right')
ax0.set_yticklabels(constellations)

# Annotate each cell with visibility score
for i in range(len(constellations)):
    for j in range(len(months)):
        color = 'white' if visibility_scores[i, j] < 6 else 'black'
        ax0.text(j, i, f'{visibility_scores[i, j]}', ha='center', va='center', color=color, fontsize=10)

# Add color bar with specific adjustments
cbar = plt.colorbar(im, ax=ax0, orientation='vertical')
cbar.set_label('Visibility Score', fontsize=12)

# Highlight maximum visibility for each constellation with gradient effect
for i in range(len(constellations)):
    max_score_index = np.argmax(visibility_scores[i])
    ax0.add_patch(patches.Rectangle((max_score_index-0.5, i-0.5), 1, 1, fill=False, edgecolor='yellow', linewidth=2, linestyle='--'))

# Sub-plot for average visibility bar chart
ax1 = plt.subplot(gs[1])
ax1.barh(constellations, avg_visibility, color='navy', alpha=0.6)
ax1.set_title('Average Annual Visibility', fontsize=14, fontweight='bold')
ax1.set_xlabel('Average Visibility Score', fontsize=12)
ax1.invert_yaxis()

# Ensure layout is optimal
plt.tight_layout()
plt.show()