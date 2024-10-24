import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Define the categories and corresponding data
categories = [
    'Fish', 
    'Coral Reefs', 
    'Marine Mammals', 
    'Sea Turtles', 
    'Crustaceans', 
    'Mollusks', 
    'Other Marine Life'
]

percentages = [40, 15, 10, 5, 12, 8, 10]

# Define colors with a colormap for gradient effect
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
cmap = LinearSegmentedColormap.from_list("marine_gradient", colors)

# Create a 3D effect pie chart with a gradient
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))

# Explode slices based on percentage
explode = [0.1 if pct > 10 else 0 for pct in percentages]

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=[cmap(i/len(percentages)) for i in range(len(percentages))],
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='w', linewidth=2),
    explode=explode,
    shadow=True
)

# Adjust text sizes and style for better readability
for text in texts:
    text.set_fontsize(11)
    text.set_ha('left')
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_weight('bold')
    
# Draw a central circle to make the pie chart look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Set title with appropriate font size and style
ax.set_title('Marine Biodiversity Composition\nin the Oceans of Oceania', 
             fontsize=15, 
             color='navy', 
             fontweight='bold', 
             pad=20)

# Add a legend outside the chart
plt.legend(wedges, categories, title="Species Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Enhance layout to avoid overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()