import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import squarify

# Define species categories and their percentages in the park
categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects', 'Fishes']
percentages = [25, 35, 10, 5, 20, 5]

# Define colors for each category for the tree map
colors = ['#8b4513', '#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0']

# Plotting the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=percentages, label=[f"{cat}\n{perc}%" for cat, perc in zip(categories, percentages)], 
              color=colors, alpha=0.7, pad=True, text_kwargs={'fontsize': 12})

# Add title and styling
plt.title('Biodiversity Distribution\nin Evergreen Wilderness Park', fontsize=16, fontweight='bold', ha='center')
plt.axis('off')  # Hide the axes

# Create a custom legend
legend_labels = [Patch(color=colors[i], label=f'{categories[i]}: {percentages[i]}%') for i in range(len(categories))]
plt.legend(handles=legend_labels, loc='upper left', fontsize=12, title='Species Categories')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()