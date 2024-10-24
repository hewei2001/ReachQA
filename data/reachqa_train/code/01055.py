import matplotlib.pyplot as plt
import numpy as np

# Define the categories for sustainability assessment
categories = ['Renewable Energy', 'Waste Management', 'Public Transport', 'Green Spaces', 'Air Quality', 'Water Conservation']
num_vars = len(categories)

# Performance scores for each city
amsterdam_scores = [9, 8, 7, 8, 7, 9]
san_francisco_scores = [7, 9, 8, 7, 8, 6]
singapore_scores = [8, 7, 9, 6, 9, 8]
stockholm_scores = [9, 9, 7, 9, 9, 8]
sydney_scores = [8, 6, 8, 7, 8, 7]

# Add the first score to the end to close the circle
amsterdam_scores += amsterdam_scores[:1]
san_francisco_scores += san_francisco_scores[:1]
singapore_scores += singapore_scores[:1]
stockholm_scores += stockholm_scores[:1]
sydney_scores += sydney_scores[:1]

# Calculate angle for each category
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize Radar Chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw one axis per variable and add labels
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, color='grey', size=12, wrap=True)

# Draw y-labels
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Plot each city's data and fill the area
city_data = [
    (amsterdam_scores, 'Amsterdam', 'deepskyblue'),
    (san_francisco_scores, 'San Francisco', 'forestgreen'),
    (singapore_scores, 'Singapore', 'darkorange'),
    (stockholm_scores, 'Stockholm', 'mediumorchid'),
    (sydney_scores, 'Sydney', 'crimson')
]

for data, label, color in city_data:
    ax.plot(angles, data, linewidth=2, linestyle='solid', label=label, color=color)
    ax.fill(angles, data, color, alpha=0.1)

# Title with line break for clarity
plt.title("Urban Sustainability Performance 2023\nComparative Analysis of Major Cities", size=16, weight='bold', va='top')

# Add legend and adjust layout
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()