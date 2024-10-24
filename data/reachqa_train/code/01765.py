import matplotlib.pyplot as plt
import numpy as np

# Data representing neighborhood well-being scores in different categories
community_engagement = [78, 82, 69, 85, 71]
access_to_amenities = [90, 87, 76, 88, 75]
environmental_quality = [65, 70, 60, 78, 65]
safety = [80, 85, 75, 82, 70]

# Combine the data into a single list for plotting
data = [community_engagement, access_to_amenities, environmental_quality, safety]

# Categories
categories = ['Community Engagement', 'Access to Amenities', 'Environmental Quality', 'Safety']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal box plot with different colors for each category
box_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
box = ax.boxplot(data, vert=False, patch_artist=True,
                 boxprops=dict(color='blue'),
                 whiskerprops=dict(color='blue'),
                 capprops=dict(color='blue'),
                 flierprops=dict(markerfacecolor='red', marker='o', color='blue'),
                 medianprops=dict(color='darkblue'))

# Setting individual colors for each box
for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

# Set y-tick labels
ax.set_yticklabels(categories)

# Title and labels
ax.set_title("Community Well-Being in Urban Neighborhoods:\nA Horizontal Box Plot Analysis",
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Scores', fontsize=12)
ax.set_ylabel('Categories', fontsize=12)

# Add grid for easier analysis
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()