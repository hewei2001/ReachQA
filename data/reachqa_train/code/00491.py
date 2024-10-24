import matplotlib.pyplot as plt
import numpy as np

# Planets and their elemental compositions (in percentages)
planets = ['Mercury', 'Venus', 'Earth', 'Mars']
elements = ['Iron', 'Silicon', 'Oxygen', 'Magnesium', 'Sulfur', 'Other']

# Fictional percentage data for elemental composition
composition_data = {
    'Mercury': [70, 10, 7, 7, 3, 3],
    'Venus': [32, 15, 48, 3, 1, 1],
    'Earth': [35, 15, 46, 2, 1, 1],
    'Mars': [22, 16, 53, 5, 2, 2]
}

# Colors for each element
colors = ['#D32F2F', '#FF9800', '#4CAF50', '#2196F3', '#9C27B0', '#FFC107']

# Create a donut pie chart for each planet
fig, axs = plt.subplots(2, 2, figsize=(14, 14))
axs = axs.flatten()

for ax, planet in zip(axs, planets):
    wedges, texts, autotexts = ax.pie(composition_data[planet], labels=elements, autopct='%1.1f%%',
                                      startangle=140, colors=colors, pctdistance=0.85,
                                      wedgeprops=dict(width=0.3), shadow=True)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')  
    
    ax.set_title(f'{planet}', fontsize=14, fontweight='bold', pad=20)
    
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)

# Add a title to the figure
fig.suptitle('Elemental Composition of Rocky Planets:\nA Cross-Planetary Analysis', 
             fontsize=18, fontweight='bold')

# Create a legend
plt.legend(wedges, elements, title="Elements", loc="center left", bbox_to_anchor=(1.05, 0.5))

# Adjust layout to make room for the legend and avoid overlap
plt.tight_layout()

# Show the plot
plt.show()