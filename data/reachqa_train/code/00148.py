import matplotlib.pyplot as plt
import numpy as np

# Data: Water usage in million gallons
sectors = ['Residential', 'Agricultural', 'Industrial', 'Recreational', 'Commercial']
water_usage = np.array([120, 80, 50, 30, 70])

# Colors for each sector
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(9, 9))

# Plotting the donut pie chart
wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Customize the texts and autotexts for better readability
plt.setp(texts, size=12, weight='bold', va='center')
plt.setp(autotexts, size=12, color='white', weight='bold')

# Title
ax.set_title("Water Usage in AquaRidge Eco-City\nOptimizing Resources for Sustainability", 
             fontsize=16, fontweight='bold', loc='center')

# Create center circle for the donut effect
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(center_circle)

# Ensure the pie chart is a circle
ax.axis('equal')  

# Legend placed outside the chart
ax.legend(wedges, sectors, title="Sectors", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show plot
plt.show()