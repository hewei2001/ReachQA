import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = [1990, 2000, 2010, 2020]

# Artifacts data: Number of artifacts acquired
celestial_sculptures = [30, 45, 60, 80]
astronomical_devices = [40, 50, 50, 55]
cosmic_paintings = [20, 25, 35, 50]

# X positions for each group
x_pos = np.arange(len(decades))

# Parameters for bar dimensions
width = 0.4   # Bar width
depth = 0.2   # Bar depth

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting each category of artifact using bar3d
# Celestial Sculptures
ax.bar3d(x_pos, np.zeros(len(x_pos)), np.zeros(len(x_pos)), width, depth, celestial_sculptures, color='purple', alpha=0.8, label='Celestial Sculptures')

# Astronomical Devices
ax.bar3d(x_pos + width, np.ones(len(x_pos)), np.zeros(len(x_pos)), width, depth, astronomical_devices, color='orange', alpha=0.8, label='Astronomical Devices')

# Cosmic Paintings
ax.bar3d(x_pos + 2 * width, np.ones(len(x_pos)) * 2, np.zeros(len(x_pos)), width, depth, cosmic_paintings, color='cyan', alpha=0.8, label='Cosmic Paintings')

# Customizing axes
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Artifact Type', fontsize=12)
ax.set_zlabel('Number of Artifacts', fontsize=12)

# Set title
ax.set_title('Interstellar Artifacts: 3D Visualization of Space Museum Exhibits', fontsize=14, fontweight='bold', pad=20)

# Custom y-axis tick labels for artifact types
ax.set_yticks([0.1, 1.1, 2.1])
ax.set_yticklabels(['Celestial Sculptures', 'Astronomical Devices', 'Cosmic Paintings'])

# Set x-axis tick positions and labels
ax.set_xticks(x_pos + width)
ax.set_xticklabels(decades)

# Adjust viewing angle
ax.view_init(elev=20, azim=120)

# Add legend
ax.legend(title='Artifacts', loc='upper right', bbox_to_anchor=(1.2, 0.9), fontsize=10)

# Enhance grid visibility
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()