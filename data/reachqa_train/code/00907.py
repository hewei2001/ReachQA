import matplotlib.pyplot as plt
import numpy as np

# Define plant categories and their cultivation frequency
plant_categories = ['Trees', 'Shrubs', 'Grasses', 'Flowers', 'Vines']
cultivation_frequency = [40, 25, 15, 30, 10]

# Define a color palette for the plant categories
colors = ['#2E8B57', '#D2691E', '#BDB76B', '#FF1493', '#6A5ACD']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(plant_categories, cultivation_frequency, color=colors, edgecolor='black', height=0.6)

# Set labels and title
ax.set_xlabel('Cultivation Frequency (units)', fontsize=12)
ax.set_ylabel('Plant Categories', fontsize=12)
ax.set_title('Urban Flora Expansion:\nKey Plant Types Cultivated in Green Cities (2023)', fontsize=14, fontweight='bold')

# Add data labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', fontsize=10)

# Add vertical grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Customize y-axis: invert and align ticks with bar centers
ax.invert_yaxis()
ax.set_yticks(np.arange(len(plant_categories)))
ax.set_yticklabels(plant_categories)

# Create annotations for plant categories
annotations = [
    'Trees: Provide shade, produce oxygen',
    'Shrubs: Enhance aesthetics, support biodiversity',
    'Grasses: Prevent erosion, cover ground',
    'Flowers: Attract pollinators, add color',
    'Vines: Efficient use of vertical space'
]

# Add a legend explaining significance
plt.legend(bars, annotations, title="Significance", loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()