import matplotlib.pyplot as plt
import squarify
import matplotlib.colors as mcolors

# Define the data for continents and their resource usage
data = {
    'Energy Consumption': {
        'North America': 25,
        'Europe': 20,
        'Asia': 30,
        'Africa': 10,
        'South America': 8,
        'Australia': 7
    },
    'Water Usage': {
        'North America': 20,
        'Europe': 15,
        'Asia': 35,
        'Africa': 12,
        'South America': 10,
        'Australia': 8
    },
    'Waste Generation': {
        'North America': 30,
        'Europe': 25,
        'Asia': 28,
        'Africa': 5,
        'South America': 7,
        'Australia': 5
    }
}

# Define a color list for 'Energy Consumption' using a subset of Tableau colors
energy_colors = list(mcolors.TABLEAU_COLORS.values())

# Plot a tree map for each category
fig, axes = plt.subplots(1, 3, figsize=(20, 10))

for ax, (category, values) in zip(axes, data.items()):
    labels = [f'{continent}\n{values[continent]}%' for continent in values]
    sizes = list(values.values())
    
    # Generate a color list based on the category
    if category == 'Energy Consumption':
        color_list = energy_colors[:len(values)]
    elif category == 'Water Usage':
        cmap = plt.cm.Blues
        color_list = [cmap(i / float(len(values) - 1)) for i in range(len(values))]
    elif category == 'Waste Generation':
        cmap = plt.cm.Greens
        color_list = [cmap(i / float(len(values) - 1)) for i in range(len(values))]

    # Create the treemap
    squarify.plot(ax=ax, sizes=sizes, label=labels, color=color_list, alpha=0.8, text_kwargs={'fontsize':10})
    
    # Add a thin border around each segment for visual separation
    ax.set_title(f'{category}', fontsize=14, fontweight='bold')
    ax.axis('off')

# Main title for the plot
plt.suptitle('Global Environmental Footprint:\nResource Usage by Continent', fontsize=18, fontweight='bold', y=0.97)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()