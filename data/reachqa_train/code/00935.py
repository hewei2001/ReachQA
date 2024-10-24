import matplotlib.pyplot as plt
import numpy as np

# Define magical ingredients and their usage percentages
ingredients = [
    "Dragon Scale Dust", 
    "Unicorn Horn Shavings", 
    "Mandrake Root Essence", 
    "Phoenix Feather Fragments", 
    "Moonflower Petals"
]

# Percentage usage in potion recipes
usage_percentages = [25, 20, 18, 22, 15]

# Colors for the ingredients
colors = ['#8B0000', '#FF69B4', '#6B8E23', '#FF4500', '#8A2BE2']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    usage_percentages, 
    labels=ingredients, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='white'),
    shadow=True
)

# Create a donut hole by setting the radius of a blank circle at the center
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set the title and adjust its formatting
plt.title(
    "Culinary Preferences of Elderglen:\n"
    "Top Magical Ingredients in Potion Recipes", 
    fontsize=14, fontweight='bold'
)

# Annotate text inside wedges with black color for better readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Draw a legend outside the plot
plt.legend(
    wedges, ingredients, title="Ingredients", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Adjust layout to make room for the legend
plt.tight_layout()

# Show the plot
plt.show()