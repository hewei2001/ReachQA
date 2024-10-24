import matplotlib.pyplot as plt
import numpy as np

# Data: Elements and their proportions in the atmosphere of the fictional Planet Zogron
elements = ['Argonium', 'Zenite', 'Heliox', 'Vaporium', 'Etherion']
proportions = [30, 25, 20, 15, 10]

# Brief descriptions for each element
descriptions = {
    'Argonium': 'A mysterious inert gas with a greenish glow.',
    'Zenite': 'Radiates a beautiful purple hue.',
    'Heliox': 'Light and buoyant, blends blue light.',
    'Vaporium': 'Contributes to the thick, dense clouds.',
    'Etherion': 'A rare, shimmering silver gas.'
}

# Distinct colors for each sector with gradient-like appearance
colors = ['#76c7c0', '#ab47bc', '#42a5f5', '#7e57c2', '#bdbdbd']

# Explode Heliox to highlight it
explode = (0, 0, 0.1, 0, 0)

# Create the figure and a 2D subplot
fig, ax = plt.subplots(figsize=(12, 7))

# Create a pie chart
wedges, texts, autotexts = ax.pie(proportions, labels=elements, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, textprops=dict(color="w", weight='bold'), pctdistance=0.85)

# Customizing the title for a thematic effect
ax.set_title('Atmospheric Composition of\nPlanet Zogron', fontsize=18, fontweight='bold', pad=25, color='#4a4a4a')

# Customize label and percentage text
for text in texts + autotexts:
    text.set_fontsize(12)
    text.set_weight('bold')

# Create a legend with element descriptions
legend_labels = [f'{elements[i]}: {descriptions[elements[i]]}' for i in range(len(elements))]
plt.legend(wedges, legend_labels, title="Element Descriptions", loc="upper left", bbox_to_anchor=(1, 0.85), fontsize=10)

# Add shadow effect
for wedge in wedges:
    wedge.set_edgecolor('w')
    wedge.set_linewidth(1.2)
    wedge.set_alpha(0.8)

# Set a background that reflects the theme of space
fig.patch.set_facecolor('#f0f0f5')

# Automatically adjust the plot layout
plt.tight_layout()

# Display the plot
plt.show()