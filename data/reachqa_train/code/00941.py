import matplotlib.pyplot as plt
import numpy as np

# Define plant categories and their cultivation frequency
plant_categories = ['Trees', 'Shrubs', 'Grasses', 'Flowers', 'Vines']
cultivation_frequency = [40, 25, 15, 30, 10]

# Define a color palette for the plant categories with gradient-like effect
cmap = plt.get_cmap('Greens')
colors = [cmap(0.8), cmap(0.6), cmap(0.4), cmap(0.3), cmap(0.2)]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.barh(plant_categories, cultivation_frequency, color=colors, edgecolor='black', height=0.6)

# Set labels and a multi-line title for readability
ax.set_xlabel('Cultivation Frequency (units)', fontsize=12, fontweight='bold')
ax.set_ylabel('Plant Categories', fontsize=12, fontweight='bold')
ax.set_title('Urban Flora Expansion:\nKey Plant Types Cultivated in Green Cities (2023)', fontsize=16, fontweight='bold', loc='left', pad=20)

# Add data labels to each bar with enhanced styling
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}', va='center', ha='left', fontsize=11, fontweight='bold', color='darkgreen')

# Add vertical grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

# Customize y-axis: invert and align ticks with bar centers
ax.invert_yaxis()

# Create annotations for plant categories with icons
annotations = [
    '🌳 Trees: Provide shade, produce oxygen',
    '🌿 Shrubs: Enhance aesthetics, support biodiversity',
    '🌾 Grasses: Prevent erosion, cover ground',
    '🌺 Flowers: Attract pollinators, add color',
    '🍇 Vines: Efficient use of vertical space'
]

# Add a legend explaining significance with formatted annotations
legend = plt.legend(bars, annotations, title="Significance", loc='upper right',
                    bbox_to_anchor=(1.2, 1), fontsize=10, title_fontsize='11', frameon=False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()