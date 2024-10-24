import matplotlib.pyplot as plt
import numpy as np

# Data: Types of cuisines and their popularity among surveyed food enthusiasts
cuisines = ["Italian", "Chinese", "Indian", "Mexican", "Japanese", "French", "Mediterranean", "Thai"]
popularity = [25, 18, 15, 12, 10, 8, 7, 5]

# Set colors for each section using a colormap
colors = plt.cm.tab20c(np.linspace(0, 1, len(cuisines)))

# Create the donut pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    popularity,
    labels=cuisines,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w'),
    explode=[0.1, 0, 0, 0, 0, 0, 0, 0],  # Explode the first slice for emphasis
    shadow=True  # Add a shadow for depth
)

# Enhance text properties for better readability
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(9)

# Place a title inside the donut for thematic emphasis
plt.text(0, 0, 'Global Culinary\nPreferences', 
         horizontalalignment='center', verticalalignment='center',
         fontsize=14, fontweight='bold')

# Draw the circle for the ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add the title and arrange layout
plt.title('Culinary Preferences of Food Enthusiasts:\nA Gastronomic Journey', fontsize=15, pad=50)
plt.legend(wedges, cuisines, title="Cuisines", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()