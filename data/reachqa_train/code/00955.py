import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the data
years = [2015, 2020, 2025]
cities = ["Futureville", "Innovatown", "GreenCity"]
technologies = ["IoT", "AI", "Renewable Energy"]

# Percentage of tech adoption in each city over the years
data = {
    "Futureville": {
        "IoT": [40, 60, 80],
        "AI": [30, 50, 70],
        "Renewable Energy": [20, 40, 60]
    },
    "Innovatown": {
        "IoT": [30, 50, 70],
        "AI": [40, 60, 80],
        "Renewable Energy": [50, 70, 90]
    },
    "GreenCity": {
        "IoT": [20, 40, 60],
        "AI": [25, 45, 65],
        "Renewable Energy": [55, 75, 95]
    }
}

# Initialize 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define bar width and offsets
bar_width = 0.6
num_cities = len(cities)
num_techs = len(technologies)

# Plot stacked bars for each city
for i, city in enumerate(cities):
    x_pos = np.array(years) + i * 0.3  # Offset each city's bars
    y_pos = i * np.ones_like(years)    # Same y position for each city's bars
    bottom = np.zeros(len(years))      # Initialize the bottom for stacking
    
    for j, tech in enumerate(technologies):
        # Get data for current tech and city
        values = data[city][tech]
        ax.bar3d(x_pos, y_pos, bottom, bar_width, bar_width, values, 
                 color=plt.cm.viridis((j + i) / (num_techs + num_cities)),
                 label=f'{city} - {tech}' if i == 0 else "", alpha=0.8)
        
        # Update bottom for stacking
        bottom += values

# Adjust view angle for better visualization
ax.view_init(elev=20, azim=120)

# Label axes and title
ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('City', fontsize=10)
ax.set_zlabel('Tech Adoption (%)', fontsize=10)
ax.set_xticks(years)
ax.set_xticklabels(years)
ax.set_yticks(range(num_cities))
ax.set_yticklabels(cities)

# Set title
ax.set_title('Evolution of Tech Adoption in Smart Cities\n(2015-2025)', fontsize=14, fontweight='bold')

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:num_techs], labels[:num_techs], loc='upper left', title='Technology', bbox_to_anchor=(0.9, 1))

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()