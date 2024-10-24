import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define categories for the radar chart
categories = ["Knife Skills", "Baking", "Plating", "Sauce Preparation", "Creativity", "Hygiene Standards"]
num_vars = len(categories)

# Define scores for each chef
chef_aurora = [8, 7, 9, 8, 7, 9]
chef_blake = [7, 8, 8, 9, 9, 8]

# Compute angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Function to complete the data for the radar plot
def complete_data(data):
    return data + data[:1]

# Complete each chef's data
aurora_data = complete_data(chef_aurora)
blake_data = complete_data(chef_blake)

# Set up the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot settings for each category
plt.xticks(angles[:-1], categories, color='black', size=10)
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8)
plt.ylim(0, 10)

# Plot each chef's data
ax.plot(angles, aurora_data, linewidth=2, linestyle='solid', label='Chef Aurora', color='royalblue')
ax.fill(angles, aurora_data, color='royalblue', alpha=0.25)

ax.plot(angles, blake_data, linewidth=2, linestyle='dotted', label='Chef Blake', color='orange')
ax.fill(angles, blake_data, color='orange', alpha=0.25)

# Add a title with multiline for better readability
plt.title("Culinary Arts Mastery: A Chef's Skill Radar", size=15, color='black', weight='bold', pad=20)

# Add a legend for clarity
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Use tight layout for better spacing
plt.tight_layout()

# Display the radar chart
plt.show()