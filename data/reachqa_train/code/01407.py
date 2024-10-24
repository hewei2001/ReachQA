import matplotlib.pyplot as plt

# Material composition data for each structure
structures = ['Pyramids of Giza', 'Parthenon', 'Great Wall of China', 'Colosseum', 'Machu Picchu']
stone = [85, 70, 50, 60, 80]
wood = [5, 10, 30, 20, 10]
metal = [5, 15, 10, 15, 5]
others = [5, 5, 10, 5, 5]

# Colors for each section
colors = ['#8C7853', '#C19A6B', '#B0C4DE', '#DDA0DD']

# Define subplots for each structure
fig, axs = plt.subplots(1, 5, figsize=(20, 6), subplot_kw=dict(aspect="equal"))

# Titles for each subplot
structure_titles = [
    'Pyramids of Giza\n85% Stone, 5% Wood, 5% Metal, 5% Others',
    'Parthenon\n70% Stone, 10% Wood, 15% Metal, 5% Others',
    'Great Wall of China\n50% Stone, 30% Wood, 10% Metal, 10% Others',
    'Colosseum\n60% Stone, 20% Wood, 15% Metal, 5% Others',
    'Machu Picchu\n80% Stone, 10% Wood, 5% Metal, 5% Others'
]

# Plotting each donut pie chart
for ax, structure, title, s, w, m, o in zip(axs, structures, structure_titles, stone, wood, metal, others):
    sizes = [s, w, m, o]
    wedges, texts, _ = ax.pie(
        sizes, colors=colors, startangle=140, 
        wedgeprops=dict(width=0.3, edgecolor='w'), 
        labels=['Stone', 'Wood', 'Metal', 'Others'], 
        labeldistance=1.1, pctdistance=0.8, autopct='%1.1f%%')
    
    # Customizing text properties
    for text in texts:
        text.set_color('black')
        text.set_fontsize(8)
    
    ax.set_title(title, fontsize=10, pad=10)
    
    # Adding a circle at the center for the donut shape
    centre_circle = plt.Circle((0,0),0.70,fc='white', edgecolor='white')
    fig.gca().add_artist(centre_circle)

# Add a global legend
fig.legend(wedges, ['Stone', 'Wood', 'Metal', 'Others'], loc='upper center', ncol=4, frameon=False, fontsize=10)

# Add the main title
plt.suptitle('Material Composition of Iconic Ancient Structures', fontsize=16, fontweight='bold', y=1.05)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()