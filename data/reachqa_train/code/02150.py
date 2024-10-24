import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the stages and number of writers
stages = ['Idea Generation', 'Manuscript Drafting', 'Editing & Revisions', 
          'Submission to Publishers', 'Publication', 'Bestseller Status']
writers = [1000, 800, 500, 250, 120, 50]

# Colors for the funnel segments
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Calculate the width ratio for each stage based on the number of writers
widths = [w / max(writers) for w in writers]

# Calculate positions for each polygon to create a funnel effect
polygon_points = []
height = 0.8
for i, width in enumerate(widths):
    bottom_width = width if i == len(widths) - 1 else widths[i + 1]
    top_left = ((1 - width) / 2, i)
    top_right = ((1 + width) / 2, i)
    bottom_left = ((1 - bottom_width) / 2, i + 1)
    bottom_right = ((1 + bottom_width) / 2, i + 1)
    polygon_points.append([top_left, top_right, bottom_right, bottom_left])

# Plotting the funnel chart
fig, ax = plt.subplots(figsize=(10, 7))

for i, (points, color) in enumerate(zip(polygon_points, colors)):
    funnel_polygon = Polygon(points, closed=True, facecolor=color, edgecolor='gray', alpha=0.8)
    ax.add_patch(funnel_polygon)
    # Adding the number of writers at each stage
    ax.text(0.5, i + 0.5, f'{writers[i]} Writers', va='center', ha='center', fontsize=10, color='black', fontweight='bold')

# Adding labels for stages
ax.set_yticks([i + 0.5 for i in range(len(stages))])
ax.set_yticklabels(stages, fontsize=12, fontweight='bold')
ax.invert_yaxis()  # Invert y axis to have the first stage at the top

# Titles and labels
plt.title("The Writer's Journey:\nFrom Concept to Bestseller", fontsize=16, fontweight='bold')
plt.xlabel('Proportion of Writers', fontsize=12)

# Removing the x-axis ticks and labels for cleanliness
ax.set_xticks([])
ax.set_xlim(0, 1)  # Set limits from 0 to 1 for the funnel width

# Optimize layout
plt.tight_layout()

# Display the funnel chart
plt.show()