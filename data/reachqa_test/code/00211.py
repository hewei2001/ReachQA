import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Define magical creature categories and their population percentages
creature_categories = ['Fairies', 'Elves', 'Unicorns', 'Dragons', 'Mermaids', 'Griffins', 'Centaurs']
population_percentages = [30, 25, 15, 10, 8, 7, 5]

# Use a colormap for a cohesive color scheme
cmap = plt.get_cmap("Pastel1")
colors = cmap(np.linspace(0, 1, len(creature_categories)))

# Explode slices to subtly highlight smaller categories
explode = (0.1, 0.05, 0, 0.05, 0, 0, 0.1)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Add shadow and style
wedges, texts, autotexts = ax.pie(
    population_percentages, labels=creature_categories, autopct='%1.1f%%', 
    startangle=140, colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3, edgecolor='w'))

# Style text and labels
for text in texts:
    text.set_fontsize(12)
    text.set_color('#2A2A2A')
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_color('#4C4C4C')
    
# Add a gradient effect by adding a circle to mimic depth
centre_circle = Circle((0, 0), 0.75, color='white', lw=0)
fig.gca().add_artist(centre_circle)

# Set a title with line breaks for readability
plt.title("Population Distribution of\nMagical Creatures in the Enchanted Forest (2023)", 
          fontsize=16, fontweight='bold', ha='center')

# Add a legend with icons for better visual categorization
plt.legend(wedges, creature_categories, title="Magical Creatures", loc="center left", 
           bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()