import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Fantasy literature categories
categories = ['World-Building', 'Character Development', 'Plot Complexity', 'Thematic Depth', 'Originality']

# Scores for each subgenre
epic_fantasy = [9, 8, 7, 8, 6]
urban_fantasy = [7, 7, 6, 7, 8]
dark_fantasy = [6, 8, 8, 9, 7]
historical_fantasy = [8, 6, 7, 7, 8]

# Group the data
data = [epic_fantasy, urban_fantasy, dark_fantasy, historical_fantasy]
genres = ['Epic Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Historical Fantasy']

# Number of variables
num_vars = len(categories)

# Compute angle for each category axis
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop by adding the start point

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable with label
plt.xticks(angles[:-1], categories, color='grey', size=10)

# Draw y labels
ax.set_rscale('linear')
ax.set_ylim(0, 10)
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color="grey", size=7)

# Plot data and fill areas for each genre
colors = ['#FF5733', '#33C4FF', '#DA33FF', '#33FF8B']
for i, (genre_data, color) in enumerate(zip(data, colors)):
    values = genre_data + genre_data[:1]
    ax.plot(angles, values, color=color, linewidth=1, linestyle='solid', label=genres[i])
    ax.fill(angles, values, color=color, alpha=0.25)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Add a title with line breaks for readability
plt.title('Quest for Knowledge:\nEvaluating Fantasy Genres in Modern Literature', size=15, y=1.1, color='navy', weight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()