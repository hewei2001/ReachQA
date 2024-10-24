import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Shadow

# Define the dietary components and their corresponding proportions
dietary_components = [
    "Plant-based\nProteins", "Whole Grains", "Vegetables",
    "Fruits", "Dairy\nAlternatives", "Healthy Fats", "Sugars"
]
proportions = [20, 25, 20, 15, 10, 7, 3]  # in percentage

# Assign colors with a gradient effect to each dietary component
colors = ['#8dd3c7', '#fb8072', '#ffffb3', '#bebada', '#80b1d3', '#fdb462', '#b3de69']
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Explode the "Plant-based Proteins" slice

# Create the ring chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions,
    explode=explode,
    labels=dietary_components,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add shadows to create a 3D effect
for w in wedges:
    shadow = Shadow(w, -0.02, -0.02, color='gray')
    ax.add_patch(shadow)

# Draw a gradient circle at the center to enhance the ring effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='grey', linewidth=1.5, linestyle='--')
fig.gca().add_artist(centre_circle)

# Title and styling
plt.title('Revolutionizing Nutrition:\nShare of Dietary Components\nin the Future Food Pyramid', 
          fontsize=14, fontweight='bold', pad=20, color='#333333')
plt.setp(autotexts, size=9, weight="bold", color="black")

# Adjust layout to prevent overlap
plt.tight_layout()

# Create a custom legend outside the plot
plt.legend(wedges, dietary_components, title="Components", loc="center left", bbox_to_anchor=(1.1, 0.5))

# Add text inside the ring for additional context
plt.text(0, 0, '2050 Diet\nModel', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# Show the ring chart
plt.show()