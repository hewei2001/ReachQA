import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

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
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Parameters for bar dimensions
bar_width = 0.15
x = np.arange(len(cities))
y = np.arange(len(wildlife_categories))
_xx, _yy = np.meshgrid(x, y)
x, y = _xx.ravel(), _yy.ravel()

# Heights (percentage values)
top = percentage_data.T.flatten()
bottom = np.zeros_like(top)
width = depth = bar_width

# Enhanced color scheme using a colormap
colors = plt.cm.viridis(np.linspace(0, 1, len(wildlife_categories)))
colors = np.repeat(colors, len(cities), axis=0)

ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=colors)

# Add data labels on top of bars
for (xi, yi, zi) in zip(x, y, top):
    ax.text(xi, yi, zi, f'{zi}%', color='black', ha='center', va='bottom', fontsize=8)

# Set the axes labels
ax.set_xlabel('City', labelpad=20, fontweight='bold')
ax.set_ylabel('Wildlife Category', labelpad=20, fontweight='bold')
ax.set_zlabel('Percentage (%)', labelpad=20, fontweight='bold')
ax.set_xticks(np.arange(len(cities)) + bar_width/2)
ax.set_xticklabels(cities, rotation=20, ha='right')
ax.set_yticks(np.arange(len(wildlife_categories)) + bar_width/2)
ax.set_yticklabels(wildlife_categories)
ax.set_zlim(0, 100)
ax.zaxis.set_major_locator(MaxNLocator(integer=True))

# Title for the chart
ax.set_title('Urban Wildlife Diversity Study\n'
             'Percentage Composition of Species in Urban Parks',
             fontsize=16, fontweight='bold', pad=30)

# Legend for the bars
legend_handles = [plt.Rectangle((0, 0), 1, 1, color=plt.cm.viridis(i / len(wildlife_categories))) for i in range(len(wildlife_categories))]
ax.legend(legend_handles, wildlife_categories, loc='upper left', bbox_to_anchor=(0.1, 0.95))

# Apply a tight layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()