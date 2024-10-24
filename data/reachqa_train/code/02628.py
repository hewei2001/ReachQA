import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the cuisines to compare
cuisines = ['Italian', 'Japanese', 'Mexican']

# Define the culinary attributes to evaluate
attributes = ['Flavor', 'Presentation', 'Technique', 'Ingredients', 'Tradition']

# Data for each cuisine
data = [
    [85, 90, 80, 70, 75],  # Italian
    [90, 85, 95, 80, 80],  # Japanese
    [80, 75, 85, 85, 90]   # Mexican
]

# Convert data to a Numpy array for easier manipulation
data = np.array(data)

# Number of attributes
num_attributes = len(attributes)

# Calculate the angle for each attribute on the radar chart
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop to close the circle

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each cuisine
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot each cuisine's data
for i, cuisine_data in enumerate(data):
    values = cuisine_data.tolist()
    values += values[:1]  # Close the loop
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=cuisines[i], color=colors[i])
    ax.fill(angles, values, color=colors[i], alpha=0.25)

# Add labels for each attribute
plt.xticks(angles[:-1], attributes, color='grey', size=10)

# Set radial labels
ax.set_rlabel_position(30)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Add a title to the chart
plt.title('Global Culinary Competition:\nRadar Chart of Regional Cuisines', size=14, color='darkgreen', pad=20)

# Add a legend to the chart
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the radar chart
plt.show()