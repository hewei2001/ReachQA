import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

# Data: Architectural Styles in Architectura Ville
architectural_styles = ['Modern', 'Gothic', 'Classical', 'Art Deco', 'Baroque', 'Futuristic']
percentages = [25, 15, 20, 10, 15, 15]
colors = ['#4CAF50', '#FFD700', '#FF5733', '#C70039', '#900C3F', '#581845']
explode = (0.15, 0, 0.05, 0, 0.1, 0.15)  # Enhance explosion for prominent styles

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=architectural_styles,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 11},
    shadow=True  # Adding shadow for 3D effect
)

# Adjust text properties for better readability
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Adding a gradient effect (Note: For static charts, this will simulate gradient via transparency)
for i, wedge in enumerate(wedges):
    wedge.set_alpha(0.8 - 0.05 * i)

# Title configuration with multi-line
ax.set_title('Architectura Ville:\nA Rich Tapestry of Architectural Styles', fontsize=14, fontweight='bold', pad=30)

# Customize and position the legend with thematic icons
legend_labels = [
    'Modern: Minimalist', 'Gothic: Ornate Arches', 'Classical: Ancient', 
    'Art Deco: Geometric', 'Baroque: Detailed', 'Futuristic: Avant-garde'
]

# Create custom legend icons (example patch usage)
legend_elements = [Patch(facecolor=colors[i], label=legend_labels[i]) for i in range(len(colors))]

ax.legend(
    handles=legend_elements,
    title="Architectural Styles",
    loc='center left',
    bbox_to_anchor=(1.05, 0.5),
    fontsize=10
)

# Subplot Configuration - Add background pattern for visual richness
fig.patch.set_facecolor('#f0f0f5')  # Light grey-blue background

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()