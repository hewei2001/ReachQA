import matplotlib.pyplot as plt
import numpy as np

# Define decades and celestial bodies
decades = ['2050s', '2060s', '2070s', '2080s']
bodies = ['Earth', 'Mars', 'Titan', 'Europa']

# IPCD deployment data (in arbitrary units)
# Each sublist contains data for Earth, Mars, Titan, Europa in order
device_data = np.array([
    [120, 100, 60, 30],  # Quantum Communicators
    [110, 90, 50, 25],   # Neutrino Transmitters
    [95, 80, 45, 20],    # Gravitational Signal Relays
    [85, 70, 35, 15],    # Hyper-Pulse Beacons
])

# Calculate the positions for each group of bars
x_positions = np.arange(len(decades))
bar_width = 0.15
depths = np.arange(len(bodies)) * 0.25

# Color map for each device type
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

# Setup the figure and 3D subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Cumulative heights for stacked bars
cumulative_heights = np.zeros((len(decades), len(bodies)))

# Iterate over each device type and plot stacked bars
for i, (device_type, color) in enumerate(zip(['Quantum Communicators', 'Neutrino Transmitters', 'Gravitational Relays', 'Hyper-Pulse Beacons'], colors)):
    for j, body in enumerate(bodies):
        ax.bar3d(
            x_positions,
            depths[j],
            cumulative_heights[:, j],
            bar_width,
            bar_width,
            device_data[i, j],
            color=color,
            alpha=0.8,
            label=device_type if j == 0 else ""
        )
        cumulative_heights[:, j] += device_data[i, j]

# Customize the plot
ax.set_xlabel('Decade')
ax.set_ylabel('Celestial Bodies')
ax.set_zlabel('Device Deployment Count')
ax.set_xticks(x_positions)
ax.set_xticklabels(decades)
ax.set_yticks(depths)
ax.set_yticklabels(bodies)
ax.set_title('Galactic Tech Deployment:\nIPCDs Distribution (2050-2090)', pad=20)
ax.view_init(elev=30, azim=135)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:len(colors)], labels[:len(colors)], loc='upper left', bbox_to_anchor=(1, 0.5), title="Device Types")

# Automatically adjust layout for better fit and visibility
plt.tight_layout()

# Display the plot
plt.show()