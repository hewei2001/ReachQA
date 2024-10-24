import matplotlib.pyplot as plt
import squarify

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

# Plot a tree map for each category
plt.figure(figsize=(18, 10))

for idx, (category, values) in enumerate(data.items(), 1):
    plt.subplot(1, 3, idx)
    labels = [f'{continent}\n{values[continent]}%' for continent in values]
    sizes = list(values.values())
    
    # Define colors for the continents
    colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

    # Create the treemap
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={'fontsize':10})
    
    plt.title(f'{category}', fontsize=14, fontweight='bold')
    plt.axis('off')

# Main title for the plot
plt.suptitle('Global Environmental Footprint: \nResource Usage by Continent', fontsize=18, fontweight='bold', y=0.98)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # rect helps to fit the suptitle without overlapping

# Display the plot
plt.show()