import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and skill values for the radar chart
categories = ['Market Analysis', 'Risk Management', 'Innovation', 'Customer Service', 'Financial Stability']
values = [8, 7, 9, 6, 8]  # Skill scores

# Repeat the first value to close the radar chart loop
values += values[:1]

# Calculate angle for each axis (divide the circle into equal parts)
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# Set up the figure and polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Draw one axis per variable and add labels
plt.xticks(angles[:-1], categories, color='darkblue', size=8)

# Draw y-labels (0-10 scale)
ax.set_rscale('linear')  # Linear scale
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color="grey", size=7)
plt.ylim(0, 10)

# Plot the data
ax.plot(angles, values, linewidth=1.5, linestyle='solid', label="FinTech Innovations")
ax.fill(angles, values, 'cyan', alpha=0.3)

# Add a title and legend
plt.title("FinTech Innovations:\nStrategic Skills Assessment", size=14, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

# Ensure layout fits well and adjust for readability
plt.tight_layout()

# Show the plot
plt.show()