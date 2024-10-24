import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Data for the radar chart
parks = ['Central Green', 'Heritage Grove', 'Sunset Park', 'Riverside', 'Botanic Bliss']
attributes = ['Biodiversity Index', 'Tree Canopy Coverage', 'Floral Diversity', 'Water Body Coverage', 'Pollinator Activity Index']

# Create artificial data for each park
data = np.array([
    [78, 65, 50, 40, 80],  # Central Green
    [85, 55, 60, 30, 90],  # Heritage Grove
    [60, 70, 40, 70, 60],  # Sunset Park
    [90, 60, 70, 60, 85],  # Riverside
    [95, 80, 90, 50, 95]   # Botanic Bliss
])

# Number of attributes
num_vars = len(attributes)

# Compute angle for each attribute
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close the circle

# Start plotting
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each park
for idx, park_data in enumerate(data):
    values = park_data.tolist()
    values += values[:1]  # repeat first value to close the circle
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=parks[idx])
    ax.fill(angles, values, alpha=0.25)

# Add attribute labels
plt.xticks(angles[:-1], attributes, color='grey', size=10)

# Add values grid
ax.set_rscale('linear')
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Add a title
plt.title('Botanical Attributes of Urban Parks in Greenfield', size=14, color='green', weight='bold', position=(0.5, 1.1))

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title='Parks')

# Enhance layout and display the chart
plt.tight_layout()
plt.show()