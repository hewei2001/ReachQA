import matplotlib.pyplot as plt

# Define Mars colony development sectors
sectors = ['Habitat\nConstruction', 'Sustainability\nMeasures', 'Transportation\nLogistics', 'Resource\nManagement']

# Expert scores for each sector
scores_data = [
    [6, 7, 8, 6, 5, 7, 8, 6, 7, 5],
    [7, 8, 6, 8, 7, 9, 8, 7, 6, 7],
    [5, 5, 6, 5, 4, 6, 5, 5, 6, 5],
    [6, 7, 7, 6, 5, 7, 6, 5, 7, 6]
]

# Create a horizontal box plot
fig, ax = plt.subplots(figsize=(10, 6))
boxprops = dict(linestyle='--', linewidth=2, color='darkblue')
flierprops = dict(marker='o', color='orange', alpha=0.6)

# Plot data with customizations
bplot = ax.boxplot(scores_data, vert=False, patch_artist=True, boxprops=boxprops, flierprops=flierprops,
                   medianprops=dict(color='red', linewidth=2), whiskerprops=dict(color='blue', linewidth=1.5),
                   capprops=dict(color='blue', linewidth=1.5), notch=True)

# Fill colors for each box
colors = ['#8ecae6', '#219ebc', '#023047', '#ffb703']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Set plot title and labels
ax.set_title('Mars Colony Development\nReadiness Assessment', fontsize=14, fontweight='bold', color='darkred')
ax.set_yticklabels(sectors, fontsize=10)
ax.set_xlabel('Readiness Score', fontsize=12)
ax.set_xlim(0, 10)

# Highlight and annotate median scores
for i, line in enumerate(bplot['medians']):
    median = line.get_xdata()[1]
    ax.text(median, i + 1, f'{median:.1f}', ha='center', va='bottom', fontsize=10, color='darkred', fontweight='bold')

# Add a grid
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()