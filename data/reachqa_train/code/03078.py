import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Define pizza types and their respective market shares
pizza_types = [
    'Galactic Cheese',
    'Mars Margherita',
    'Neptune Veggie',
    'Saturn Salami',
    'Pluto Pepperoni',
    'Jupiter Jalapeño'
]
market_shares = [28, 22, 18, 15, 10, 7]

# Define a color palette with gradient effect
colors = ['#FF9999', '#FF6666', '#66B3FF', '#3399FF', '#99FF99', '#66FF66']

# Set explode for enhanced effect
explode = (0.1, 0.05, 0.05, 0, 0, 0)

# Create a donut pie chart with gradient colors
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    market_shares,
    labels=pizza_types,
    autopct=lambda pct: f'{pct:.1f}%\n({int(pct/100.*sum(market_shares))})',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=1.5)
)

# Draw a circle in the center to create a donut shape, with a text for visual enhancement
centre_circle = Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)
ax.text(0, 0, 'Total\n100%', horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold', color='gray')

# Adjust texts for readability
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=11, weight="bold", color="darkblue")

# Equal aspect ratio ensures the pie is drawn as a circle
ax.axis('equal')

# Set the title and legend, with a thematic font and color adjustment
plt.title("Galactic Pizza Market Share:\nStellar Slices of 2200", fontsize=16, fontweight='bold', color='navy', pad=20)
ax.legend(wedges, pizza_types, title="Pizza Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Background color and layout adjustments for aesthetics
fig.patch.set_facecolor('#F0F0F5')
plt.tight_layout()

# Display the plot
plt.show()