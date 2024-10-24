import matplotlib.pyplot as plt

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

# Distinct colors for each sector
colors = ['#76c7c0', '#ab47bc', '#42a5f5', '#7e57c2', '#bdbdbd']

# Explode Heliox to highlight it
explode = (0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(proportions, labels=elements, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, textprops=dict(color="w", weight='bold'))

# Title with multiline to fit the space
ax.set_title('Atmospheric Composition of\nPlanet Zogron', fontsize=16, fontweight='bold', pad=20)

# Customize label and percentage text
plt.setp(texts, size=11, weight='bold')
plt.setp(autotexts, size=10)

# Create a legend with element descriptions
legend_labels = [f'{elements[i]}: {descriptions[elements[i]]}' for i in range(len(elements))]
ax.legend(wedges, legend_labels, title="Element Descriptions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust the plot layout
plt.tight_layout()

# Display the plot
plt.show()