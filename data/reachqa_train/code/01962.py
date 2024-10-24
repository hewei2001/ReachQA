import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2025, 2035)

# Define projected annual launches to each destination
launches_to_moon = np.array([5, 7, 8, 9, 10, 12, 13, 15, 18, 20])
launches_to_mars = np.array([3, 4, 5, 6, 8, 10, 11, 13, 15, 18])
launches_to_jupiter_moons = np.array([0, 0, 1, 1, 2, 3, 4, 5, 7, 10])

# Calculate total launches per year for the line plot
total_launches_per_year = launches_to_moon + launches_to_mars + launches_to_jupiter_moons

# Initialize figure and axes
fig = plt.figure(figsize=(14, 8))

# Subplot 1: 3D Bar Chart
ax1 = fig.add_subplot(121, projection='3d')
xpos = np.repeat(years, 3)
ypos = np.tile([1, 2, 3], len(years))
zpos = np.zeros_like(xpos)
dx = np.ones_like(xpos) * 0.7
dy = np.ones_like(ypos) * 0.7
dz = np.concatenate([launches_to_moon, launches_to_mars, launches_to_jupiter_moons])
colors = ['#ff9999', '#66b3ff', '#99ff99'] * len(years)

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8, zsort='average')
ax1.set_xlabel('Year', fontsize=10, labelpad=8)
ax1.set_ylabel('Destination', fontsize=10, labelpad=10)
ax1.set_zlabel('Projected Launches', fontsize=10, labelpad=8)
ax1.set_yticks([1, 2, 3])
ax1.set_yticklabels(['Moon', 'Mars', "Jupiter's Moons"], fontsize=9)
ax1.set_title('Projected Launches to Various\nGalactic Destinations (2025-2034)', fontsize=14, fontweight='bold', pad=20)
ax1.view_init(elev=20, azim=45)
ax1.grid(True, linestyle='--', alpha=0.5)

# Subplot 2: Line Plot
ax2 = fig.add_subplot(122)
ax2.plot(years, total_launches_per_year, marker='o', color='b', label='Total Launches')
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Total Launches', fontsize=10)
ax2.set_title('Total Projected Launches Per Year\n(2025-2034)', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()