import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Infrastructure', 'Technology', 'Sustainability', 'Population Growth', 'Economic Output']

# Data representing each colony's progress in 2075
lunar_base = [8, 9, 7, 6, 8]
mars_outpost = [7, 8, 9, 5, 7]
europa_station = [6, 7, 6, 7, 6]
titan_habitat = [7, 5, 8, 8, 7]
enceladus_complex = [5, 6, 5, 6, 5]

# Define related data for a bar chart showing resource allocation
resource_allocation = [
    [85, 90, 75, 60, 80],   # Lunar Base One
    [75, 80, 95, 55, 70],   # Mars Outpost
    [60, 70, 65, 75, 60],   # Europa Station
    [70, 55, 85, 85, 70],   # Titan Habitat
    [50, 65, 55, 60, 55]    # Enceladus Complex
]

# Combine the data into a list for ease of iteration
colony_data = [lunar_base, mars_outpost, europa_station, titan_habitat, enceladus_complex]
colony_labels = ['Lunar Base One', 'Mars Outpost', 'Europa Station', 'Titan Habitat', 'Enceladus Complex']

# Number of variables we're plotting
num_vars = len(categories)

# Compute the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Extend each data list to "close the loop" on the radar chart
for data in colony_data:
    data += data[:1]

# Define a color palette for the chart
colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'violet']

# Create a figure with 1 row and 2 columns for subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7), subplot_kw=dict(polar=True))

# Radar plot (original data)
ax = axes[0]
for data, label, color in zip(colony_data, colony_labels, colors):
    ax.fill(angles, data, color=color, alpha=0.25, label=label)
    ax.plot(angles, data, color=color, linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, weight='bold')

# Add a title
ax.set_title("Progress of Interplanetary Colonies in 2075:\nA Comprehensive Development Analysis", size=13, weight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Bar plot (related data)
ax2 = fig.add_subplot(122)
width = 0.15  # width of each bar
x = np.arange(len(categories))

# Bar plotting for each colony
for i, (allocation, label, color) in enumerate(zip(resource_allocation, colony_labels, colors)):
    ax2.bar(x + i * width, allocation, width=width, label=label, color=color, alpha=0.7)

# Add categories as x-ticks
ax2.set_xticks(x + width * 2)
ax2.set_xticklabels(categories, rotation=30, ha='right')
ax2.set_title("Resource Allocation of Colonies:\nPriorities in Development", size=13, weight='bold')
ax2.set_ylabel("Allocation Percentage")
ax2.legend(loc='upper right')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Show the plot
plt.show()