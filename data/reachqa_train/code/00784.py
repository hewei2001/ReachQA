import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the flavor attributes
attributes = ['Aroma', 'Acidity', 'Body', 'Sweetness', 'Aftertaste']
num_attributes = len(attributes)

# Define data for three coffee blends
# Adjust values as necessary to ensure a clear visual representation
morning_brew = [7, 5, 6, 8, 7]
evening_delight = [6, 4, 8, 5, 9]
tropical_twist = [8, 7, 5, 9, 6]

# Consolidate data into an array and prepare for plotting
data = np.array([morning_brew, evening_delight, tropical_twist])

# Extend data to close the radar chart
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate angle for each axis
angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define labels for the different coffee blends
labels = ["Morning Brew", "Evening Delight", "Tropical Twist"]

# Define colors for each blend
colors = ['#FF7F0E', '#1F77B4', '#2CA02C']

# Plot each coffee blend
for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.25, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

# Add attribute labels to the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(attributes, fontsize=12, fontweight='bold')

# Set title and legend
ax.set_title('Flavor Profiles of Coffee Blends\nA Journey Through Taste', fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the radar chart
plt.show()