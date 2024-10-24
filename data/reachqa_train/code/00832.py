import matplotlib.pyplot as plt
import numpy as np

# Define the data for each fruit
fruits = ['Apples', 'Bananas', 'Oranges', 'Strawberries', 'Blueberries']
nutrients = ['Vitamins', 'Fiber', 'Sugars', 'Minerals', 'Water']

# Nutrient composition for each fruit (percentages)
nutrient_data = np.array([
    [12, 5, 15, 3, 65],  # Apples
    [9, 4, 23, 2, 62],   # Bananas
    [14, 3, 11, 3, 69],  # Oranges
    [11, 4, 9, 3, 73],   # Strawberries
    [12, 5, 10, 3, 70]   # Blueberries
])

# Colors for nutrients
colors = ['#FF9999', '#FFCC99', '#99FF99', '#66B3FF', '#C2C2F0']

# Create a figure for the donut pies
fig, axes = plt.subplots(1, len(fruits), figsize=(18, 10), subplot_kw=dict(aspect="equal"))

# Plot each fruit's composition as a donut pie chart
for ax, fruit, nutrient_composition in zip(axes, fruits, nutrient_data):
    wedges, texts, autotexts = ax.pie(nutrient_composition, 
                                      labels=nutrients, 
                                      colors=colors, 
                                      startangle=140, 
                                      wedgeprops=dict(width=0.3, edgecolor='w'),
                                      autopct='%1.1f%%', 
                                      pctdistance=0.85)
    
    # Customize autotexts
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
    
    # Draw a circle in the middle to make it a donut chart
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(center_circle)
    
    # Title for each subplot
    ax.set_title(fruit, fontsize=12, pad=15)

# Overall plot title
plt.suptitle("Nutritional Composition of Common Fruits\nA Donut Pie Overview", 
             fontsize=16, fontweight='bold', y=0.95)

# Add a legend at the side
fig.legend(wedges, nutrients, title="Nutrients", loc='center right', bbox_to_anchor=(1.15, 0.5), fontsize=10)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout(rect=[0, 0, 0.9, 1])

# Display the plot
plt.show()