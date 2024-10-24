import matplotlib.pyplot as plt
import numpy as np

# Define city names and wildlife categories
cities = ['New York', 'London', 'Tokyo', 'Sydney']
wildlife_categories = ['Birds', 'Mammals', 'Reptiles', 'Insects']

# Define the percentage data for each city
percentage_data = np.array([
    [40, 25, 5, 30],  # New York
    [35, 30, 10, 25], # London
    [30, 20, 15, 35], # Tokyo
    [25, 35, 10, 30]  # Sydney
])

# Create a 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Parameters for bar dimensions
bar_width = 0.2
num_cities = len(cities)
num_categories = len(wildlife_categories)
x = np.arange(num_cities)
y = np.arange(num_categories)
_xx, _yy = np.meshgrid(x, y)
x, y = _xx.ravel(), _yy.ravel()

# Heights (percentage values)
top = percentage_data.T.flatten()
bottom = np.zeros_like(top)
width = depth = bar_width

# Create the bars with unique colors for each category
colors = ['cyan', 'magenta', 'green', 'orange']
bar_colors = np.array(colors * num_cities)

ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=bar_colors)

# Set the axes labels
ax.set_xlabel('City', labelpad=10)
ax.set_ylabel('Wildlife Category', labelpad=10)
ax.set_zlabel('Percentage (%)', labelpad=10)
ax.set_xticks(np.arange(num_cities))
ax.set_xticklabels(cities, rotation=20, ha='right')
ax.set_yticks(np.arange(num_categories))
ax.set_yticklabels(wildlife_categories)
ax.set_zlim(0, 100)

# Title for the chart
ax.set_title('Urban Wildlife Diversity Study\nPercentage Composition of Species in Urban Parks',
             fontsize=14, fontweight='bold', pad=20)

# Legend for the bars
for i, color in enumerate(colors):
    ax.bar3d(0, 0, 0, 0, 0, 0, color=color, label=wildlife_categories[i])
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Use tight_layout to minimize text overlap
plt.tight_layout()

# Display the chart
plt.show()