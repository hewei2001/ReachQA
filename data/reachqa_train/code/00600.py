import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories (cuisines) and the corresponding proficiency ratings
categories = ['French', 'Italian', 'Japanese', 'Mexican', 'Indian', 'Mediterranean']
ratings = [8, 7, 6, 9, 5, 8]

# Number of variables we're plotting
num_vars = len(categories)

# Compute the angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the plot

# Repeat the first value to close the plot
ratings += ratings[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one line per rating and fill the area
ax.fill(angles, ratings, color='turquoise', alpha=0.3)
ax.plot(angles, ratings, color='teal', linewidth=2)

# Add labels for each category
ax.set_yticklabels([])  # Hide y-tick labels to focus on categories
plt.xticks(angles[:-1], categories, size=12)

# Add a title
plt.title('Culinary Quest:\nChef\'s Mastery Across Cuisines', size=16, weight='bold', pad=20)

# Set the radial limits
ax.set_rscale('linear')
ax.set_rlabel_position(0)
plt.yticks(range(0, 11, 2), color="grey", size=10)
plt.ylim(0, 10)

# Annotate the peak proficiency
peak_index = np.argmax(ratings[:-1])
ax.annotate(f'Peak: {categories[peak_index]}', xy=(angles[peak_index], ratings[peak_index]), 
            xytext=(angles[peak_index] + 0.1, ratings[peak_index] + 1.5),
            arrowprops=dict(facecolor='darkred', shrink=0.05),
            fontsize=12, color='darkred')

# Add a legend to explain the rating scale
plt.legend(['Proficiency Level'], loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the radar chart
plt.show()