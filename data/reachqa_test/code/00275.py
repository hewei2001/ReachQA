import matplotlib.pyplot as plt
import numpy as np

# Define expanded dataset with more transport modes and larger sample sizes
hyperloops = [15, 12, 14, 16, 15, 11, 13, 15, 14, 12, 17, 13, 15, 16, 13, 14, 15, 12, 14, 13, 11, 16, 15, 17, 13]
autonomous_cars = [30, 28, 32, 31, 29, 27, 30, 34, 33, 31, 35, 29, 32, 30, 31, 32, 28, 29, 30, 33, 27, 31, 30, 29, 34]
drone_taxis = [8, 10, 7, 9, 11, 9, 10, 8, 7, 9, 10, 9, 8, 11, 7, 9, 10, 7, 8, 9, 9, 10, 8, 7, 11]
quantum_teleportation = [3, 4, 2, 3, 3, 2, 4, 2, 3, 3, 3, 2, 2, 4, 3, 3, 2, 2, 3, 4, 3, 3, 2, 2, 4]
maglev_trains = [20, 18, 22, 19, 21, 20, 19, 18, 21, 20, 22, 19, 20, 18, 21, 20, 22, 19, 20, 21, 20, 18, 22, 21, 19]
bicycle_sharing = [12, 11, 13, 14, 11, 12, 10, 13, 12, 11, 13, 14, 12, 11, 12, 13, 11, 12, 10, 13, 12, 13, 11, 14, 11]
personal_jetpacks = [25, 24, 26, 25, 23, 24, 25, 26, 24, 25, 26, 24, 25, 23, 25, 24, 23, 25, 26, 24, 25, 23, 24, 26, 25]

# Combine data into a list
data = [hyperloops, autonomous_cars, drone_taxis, quantum_teleportation, maglev_trains, bicycle_sharing, personal_jetpacks]

# Define transport mode labels
labels = ['Hyperloops', 'Autonomous Cars', 'Drone Taxis', 'Quantum Teleportation', 'Maglev Trains', 'Bicycle Sharing', 'Personal Jetpacks']

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(15, 8))

# Plot horizontal box plot with distinct colors for each transport mode
box = ax.boxplot(data, vert=False, patch_artist=True, labels=labels, notch=True, whis=1.5)

# Customize boxplot colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFB6C1', '#E0BBE4', '#957DAD']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels with appropriate formatting
ax.set_title("Urban Commute Innovations:\nAdvanced Study on Transport Efficiency by 2050", fontsize=16, fontweight='bold')
ax.set_xlabel("Commute Time (minutes)", fontsize=12)
ax.set_ylabel("Transport Modes", fontsize=12)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Annotate median values on each box for clarity
for i, median in enumerate(box['medians']):
    median_value = median.get_xdata()[1]
    ax.annotate(f'{median_value:.1f}', xy=(median_value, i + 1), xytext=(5, 0),
                textcoords='offset points', ha='left', va='center', fontsize=10, color='black',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

# Adjust layout to prevent any overlap and ensure clear visualization
plt.tight_layout()

# Display the box plot
plt.show()