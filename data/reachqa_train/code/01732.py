import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define planets and decades
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
decades = [1970, 1980, 1990, 2000, 2010, 2020]

# Adjusted data for discoveries and significance
discoveries = np.array([
    [5, 7, 12, 15, 18, 21],   # Mercury
    [9, 13, 14, 20, 24, 30],  # Venus
    [22, 28, 30, 36, 42, 48], # Earth
    [10, 15, 25, 30, 38, 45], # Mars
    [19, 23, 26, 35, 40, 43], # Jupiter
    [12, 17, 20, 25, 28, 33], # Saturn
    [5, 8, 12, 14, 18, 20],   # Uranus
    [6, 7, 9, 10, 13, 16]     # Neptune
])

# Significance of discoveries
significance = np.array([
    [12, 18, 22, 28, 34, 40],  # Mercury
    [18, 24, 28, 35, 40, 45],  # Venus
    [28, 34, 40, 45, 50, 55],  # Earth
    [25, 30, 35, 40, 45, 50],  # Mars
    [32, 38, 44, 48, 54, 60],  # Jupiter
    [20, 26, 32, 38, 42, 48],  # Saturn
    [12, 16, 20, 22, 28, 32],  # Uranus
    [10, 12, 15, 18, 22, 26]   # Neptune
])

# Colors for each planet
colors = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039', '#900C3F', '#581845', '#1C2833', '#34495E']

# Set up the figure with two subplots: 3D scatter and line chart
fig = plt.figure(figsize=(18, 8))

# 3D scatter plot
ax1 = fig.add_subplot(121, projection='3d')
for i, planet in enumerate(planets):
    ax1.scatter([i] * len(decades), decades, discoveries[i], s=significance[i] * 10,
               c=[colors[i]] * len(decades), alpha=0.6, edgecolors='w', linewidths=0.5, label=planet)

# Configure 3D plot
ax1.set_xlabel('Planets', fontsize=12, labelpad=10)
ax1.set_xticks(np.arange(len(planets)))
ax1.set_xticklabels(planets)
ax1.set_ylabel('Decades', fontsize=12, labelpad=10)
ax1.set_yticks(decades)
ax1.set_zlabel('Discoveries', fontsize=12, labelpad=10)
ax1.set_title('Exploring the Solar System:\nPlanetary Discoveries Across Decades', fontsize=14, fontweight='bold', pad=20)
ax1.view_init(elev=20, azim=135)
ax1.legend(loc='upper right', title='Planets')

# Line chart subplot showing cumulative discoveries over decades
ax2 = fig.add_subplot(122)
cumulative_discoveries = np.cumsum(discoveries, axis=1)
for i, planet in enumerate(planets):
    ax2.plot(decades, cumulative_discoveries[i], marker='o', linestyle='-', color=colors[i], label=planet)

# Configure line chart
ax2.set_xlabel('Decades', fontsize=12)
ax2.set_ylabel('Cumulative Discoveries', fontsize=12)
ax2.set_title('Cumulative Discoveries Over Time', fontsize=14, fontweight='bold')
ax2.legend(loc='upper left', title='Planets')
ax2.grid(True)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()