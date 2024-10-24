import matplotlib.pyplot as plt
import numpy as np

# Data: Expanded list of art styles and regional variations
art_styles = [
    'Early Renaissance', 'High Renaissance', 'Mannerism', 'Baroque', 'Rococo',
    'Neoclassicism', 'Romanticism', 'Realism', 'Impressionism', 'Post-Impressionism',
    'Cubism', 'Expressionism', 'Futurism', 'Abstract', 'Modern', 'Contemporary'
]
regions = ['Europe', 'Asia', 'America']

# Number of paintings in thousands
paintings_count = np.array([
    [80, 50, 40],   # Early Renaissance
    [70, 60, 30],   # High Renaissance
    [60, 40, 20],   # Mannerism
    [95, 80, 45],   # Baroque
    [45, 30, 25],   # Rococo
    [55, 35, 40],   # Neoclassicism
    [100, 85, 60],  # Romanticism
    [75, 65, 50],   # Realism
    [110, 90, 70],  # Impressionism
    [90, 70, 65],   # Post-Impressionism
    [85, 60, 50],   # Cubism
    [95, 75, 60],   # Expressionism
    [60, 40, 35],   # Futurism
    [75, 65, 55],   # Abstract
    [120, 110, 90], # Modern
    [130, 120, 110] # Contemporary
])

# Colors for the stacked bars
colors = ['#FF9999', '#66B3FF', '#99FF99']

# Create a figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot a stacked bar chart
for i, region in enumerate(regions):
    ax.bar(art_styles, paintings_count[:, i], color=colors[i], edgecolor='black', linewidth=0.5,
           label=region, bottom=np.sum(paintings_count[:, :i], axis=1))

# Add value labels on top of each stacked bar
for idx, (style, counts) in enumerate(zip(art_styles, paintings_count)):
    y_offset = 0
    for count in counts:
        y = y_offset + count / 2
        ax.text(idx, y, str(count), ha='center', va='center', fontsize=8)
        y_offset += count

# Title and labels
ax.set_title("Prevalence of Art Styles in Historical Paintings Across Regions", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Art Styles", fontsize=12)
ax.set_ylabel("Number of Paintings (in thousands)", fontsize=12)

# Adding a grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Add legend
ax.legend(title='Regions', loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust layout to accommodate labels and legend
plt.tight_layout()

# Display the plot
plt.show()