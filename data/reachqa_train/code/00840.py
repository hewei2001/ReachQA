import numpy as np
import matplotlib.pyplot as plt

# Define transportation metrics
metrics = ['Speed', 'Cost-Effectiveness', 'Accessibility', 'Environmental Impact', 'Comfort']
num_vars = len(metrics)

# Create radar chart data for each transportation mode
buses = [3, 4, 5, 3, 3]
bicycles = [2, 5, 4, 5, 4]
subways = [5, 3, 5, 4, 4]
scooters = [4, 3, 3, 4, 3]
walking = [1, 5, 5, 5, 5]

data = [buses, bicycles, subways, scooters, walking]
modes = ['Buses', 'Bicycles', 'Subways', 'Scooters', 'Walking']

# Compute angle for each metric
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop
for i in range(len(data)):
    data[i] += data[i][:1]
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each transportation mode and fill area
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, (d, color) in enumerate(zip(data, colors)):
    ax.fill(angles, d, color=color, alpha=0.25)
    ax.plot(angles, d, linewidth=2, color=color, label=modes[idx])

# Add a title
ax.set_title('Urban Mobility Efficiency:\nTransportation Modes in Metroville', size=16, weight='bold', va='bottom')

# Draw one axe per variable and add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(metrics, fontsize=12)

# Set the range for each axis
ax.set_ylim(0, 6)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Transport Modes", fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()