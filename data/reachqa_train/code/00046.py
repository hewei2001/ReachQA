import matplotlib.pyplot as plt

# Data for each planet
planets = ['Jupiter', 'Saturn', 'Earth', 'Mars']
composition_labels = ['Gas', 'Rock', 'Ice']

# Composition data in percentages
composition_data = {
    'Jupiter': [90, 8, 2],
    'Saturn': [88, 7, 5],
    'Earth': [1, 70, 29],
    'Mars': [2, 95, 3]
}

# Colors for each composition type
colors = ['#FFD700', '#D2691E', '#1E90FF']  # gold for gas, chocolate for rock, dodgerblue for ice

# Create a figure to hold all planet plots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Flatten the axes array for easy iteration
axs = axs.flatten()

# Plotting each planet's composition
for i, planet in enumerate(planets):
    wedges, texts, autotexts = axs[i].pie(composition_data[planet], labels=composition_labels,
                                          autopct='%1.1f%%', startangle=140, colors=colors, 
                                          explode=(0.05, 0.05, 0.05), shadow=True, wedgeprops=dict(width=0.3, edgecolor='w'))
    
    # Customize text properties
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_weight('bold')
        
    axs[i].set_title(f'{planet}', fontsize=14, weight='bold')

# Adding legend outside the main plot to avoid overlap
fig.legend(composition_labels, loc='upper center', ncol=3, fontsize=12)

# Set a main title for the entire plot
fig.suptitle('Composition of Planets in the Solar System', fontsize=16, weight='bold', y=0.95)

# Adjust layout to fit titles and legend without overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.9])

# Show plot
plt.show()