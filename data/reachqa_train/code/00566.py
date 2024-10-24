import matplotlib.pyplot as plt
import numpy as np

# Futuristic work environment categories
workspaces = ['Co-working Pods', 'VR Offices', 'Nature-Integrated', 'AI-Assisted', 'Floating Hubs']

# Break durations (in minutes) for each workspace
break_durations = [
    [15, 20, 22, 19, 30, 45, 50, 20, 18, 25],  # Co-working Pods
    [30, 25, 32, 35, 40, 60, 55, 45, 42, 48],  # VR Offices
    [60, 55, 58, 62, 65, 80, 85, 70, 68, 72],  # Nature-Integrated
    [10, 12, 15, 18, 20, 22, 25, 18, 19, 23],  # AI-Assisted
    [45, 50, 52, 48, 55, 65, 70, 58, 60, 63],  # Floating Hubs
]

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot(break_durations, vert=True, patch_artist=True, labels=workspaces, notch=True)

# Customizing colors for different workspaces
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Title and labels
plt.title('Futuristic Work Environments:\nDaily Break Durations in 2050', fontsize=14, fontweight='bold', color='darkslategray')
plt.xlabel('Workspaces', fontsize=12, fontweight='bold')
plt.ylabel('Break Duration (minutes)', fontsize=12, fontweight='bold')

# Adding annotations to highlight observations
annotations = ["Short breaks", "Immersive breaks", 
               "Long nature breaks", "Micro-breaks", 
               "Balanced breaks"]
for i, annotation in enumerate(annotations):
    ax.text(i + 1, max(break_durations[i]) + 3, annotation, ha='center', va='bottom', fontsize=10, color='navy')

# Customize median line and other properties
medianprops = dict(linestyle='-', linewidth=2.5, color='darkred')
ax.boxplot(break_durations, vert=True, patch_artist=True, labels=workspaces, notch=True, medianprops=medianprops)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()