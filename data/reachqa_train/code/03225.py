import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Art styles and years
art_styles = ['Holographic\nInstallations', 'VR Art Spaces', 'Bio-Art\nDisplays', 'Interactive\nAI Art', 'Digital\nSurrealism']
years = np.array([2046, 2047, 2048, 2049, 2050])

# Attendance data in thousands
attendance_data = np.array([
    [50, 70, 90, 110, 130],  # Holographic Installations
    [40, 65, 85, 120, 150],  # VR Art Spaces
    [20, 45, 75, 100, 125],  # Bio-Art Displays
    [30, 50, 70, 95, 135],   # Interactive AI Art
    [25, 55, 80, 110, 145]   # Digital Surrealism
])

# Define parameters for bar positioning and dimensions
x_pos = np.arange(len(art_styles))
y_pos = np.arange(len(years))
x_positions, y_positions = np.meshgrid(x_pos, y_pos)
x_positions = x_positions.flatten()
y_positions = y_positions.flatten()
z_positions = np.zeros_like(x_positions)
dx = dy = 0.4
dz = attendance_data.flatten()

# Create a 3D plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Define colors with variation for visual distinction
colors = ['#FF6347', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4']
colors = np.repeat(colors, len(years))

# Plot the 3D bars
ax.bar3d(x_positions, y_positions, z_positions, dx, dy, dz, color=colors, alpha=0.8)

# Set axis labels and title
ax.set_xlabel('Art Style', labelpad=15)
ax.set_ylabel('Year', labelpad=15)
ax.set_zlabel('Attendance (Thousands)', labelpad=15)
ax.set_title('Attendance Trends in Futuristic Art Exhibitions\n2046 to 2050', fontsize=16, fontweight='bold')

# Customize ticks
ax.set_xticks(np.arange(len(art_styles)) + dx / 2)
ax.set_xticklabels(art_styles, fontsize=10)
ax.set_yticks(np.arange(len(years)) + dy / 2)
ax.set_yticklabels(years, fontsize=10)
ax.set_zlim(0, 160)

# Set a viewing angle for better perspective
ax.view_init(elev=20, azim=130)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()

# Display the plot
plt.show()