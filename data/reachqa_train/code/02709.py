import matplotlib.pyplot as plt
import numpy as np

# Define the fruit categories and their consumption proportions
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs', 'Grapes']
consumption = np.array([25, 30, 10, 15, 5, 8, 7])

# Define distinct colors for each fruit segment
colors = ['#FF6347', '#FFD700', '#FF69B4', '#8B4513', '#4B0082', '#D2B48C', '#8A2BE2']

# Plotting the ring chart
fig, ax = plt.subplots(figsize=(10, 8))

# Create a ring chart by adjusting the wedge width
ax.pie(consumption, labels=fruits, colors=colors, startangle=90, 
       pctdistance=0.85, wedgeprops=dict(width=0.4, edgecolor='w', alpha=0.8))

# Draw a central circle to convert the pie chart into a ring chart
centre_circle = plt.Circle((0, 0), 0.6, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure that the chart is a circle
ax.axis('equal')

# Add title inside the center of the ring
plt.text(0, 0, "Fruit\nConsumption", horizontalalignment='center', 
         verticalalignment='center', fontsize=14, fontweight='bold', color='grey')

# Title for the chart
plt.title("Community Garden Fruit Consumption\nAnnual Harvest Festival 2023", fontsize=16, fontweight='bold', pad=20)

# Add a legend with adjusted placement to prevent occlusion
plt.legend(fruits, title="Fruits", loc="upper left", bbox_to_anchor=(1, 0.5), frameon=False)

# Automatically adjust layout to ensure optimal spacing
plt.tight_layout()

# Display the plot
plt.show()