import matplotlib.pyplot as plt
import numpy as np

# Futuristic foods and their projected popularity index
foods = [
    "Insect Protein Bars",
    "Lab-Grown Steak",
    "Algae Smoothies",
    "3D-Printed Pizza",
    "Fermented Plant-Based Yogurt"
]
demand_index = [85, 75, 65, 70, 80]

# Assign distinct colors for each bar to represent different innovation categories
colors = ['#A569BD', '#48C9B0', '#F4D03F', '#F1948A', '#85C1E9']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(foods, demand_index, color=colors, edgecolor='black', height=0.6)

# Set title and axis labels
ax.set_title("Projected Popularity of Innovative Foods\nat the 2045 Global Culinary Innovation Expo", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Popularity Index', fontsize=12, labelpad=10)
ax.set_ylabel('Futuristic Foods', fontsize=12, labelpad=10)

# Adding data labels to each bar
for bar in bars:
    width = bar.get_width()
    label_x_position = width + 1  # Slightly offset the label to the right of the bar
    ax.text(label_x_position, bar.get_y() + bar.get_height()/2, f'{width}', va='center', fontsize=10)

# Adjust y-ticks for better label visibility
ax.set_yticks(np.arange(len(foods)))
ax.set_yticklabels(foods, fontsize=11)
ax.invert_yaxis()  # Highest values on top

# Add a vertical grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()