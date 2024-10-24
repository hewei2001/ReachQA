import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data representing species diversity in the fictional rainforest
species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects', 'Plants']
percentages = [25, 20, 15, 10, 20, 10]
colors = ['#FF6347', '#4682B4', '#3CB371', '#FFA500', '#DA70D6', '#8A2BE2']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plotting the donut chart
wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=species_categories,
    autopct='%1.1f%%',
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='white'),
    shadow=True,
    explode=(0.05,) * len(species_categories)
)

# Adding a circle in the middle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(centre_circle)

# Title and axis properties
ax.axis('equal')
plt.title('Species Diversity in the Enchanted Rainforest\nContribution to Ecosystem Biodiversity', fontsize=16, fontweight='bold', color='darkgreen', pad=40)

# Customizing autotext labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_size(10)

# Building a custom legend
legend_elements = [mpatches.Patch(color=colors[i], label=species_categories[i]) for i in range(len(species_categories))]
plt.legend(handles=legend_elements, title='Species Categories', loc='center left', bbox_to_anchor=(1, 0.5))

# Automatically adjust the layout to prevent clipping of text
plt.tight_layout()

# Display the chart
plt.show()