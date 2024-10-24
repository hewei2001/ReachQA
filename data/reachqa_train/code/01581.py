import matplotlib.pyplot as plt
import numpy as np

# Planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Average temperatures in degrees Celsius
temperatures = np.array([
    [430, 465, 440, 420, 430, 460, 430, 440],
    [462, 462, 462, 462, 462, 462, 462, 462],
    [15, 16, 14, 15, 14, 13, 15, 15],
    [-55, -60, -58, -56, -57, -59, -60, -58],
    [-108, -108, -110, -107, -108, -106, -108, -109],
    [-139, -140, -138, -137, -138, -139, -140, -138],
    [-195, -198, -197, -196, -195, -194, -195, -196],
    [-201, -202, -200, -199, -198, -199, -200, -201]
])

# Distances from the Sun in Astronomical Units (AU)
distances = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.22, 30.05]

# Transpose the temperature data
temperatures = np.transpose(temperatures)

# Create the figure and heatmap
fig, ax1 = plt.subplots(figsize=(14, 8))
heatmap = ax1.imshow(temperatures, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Color bar
cbar = plt.colorbar(heatmap, ax=ax1)
cbar.set_label('Average Temperature (°C)', rotation=270, labelpad=15)

# Set x and y ticks
ax1.set_xticks(np.arange(len(planets)))
ax1.set_xticklabels(planets, rotation=45, ha='right', fontsize=10)
ax1.set_yticks(np.arange(len(temperatures)))
ax1.set_yticklabels(planets, fontsize=10)

# Annotations for temperatures
for i in range(temperatures.shape[0]):
    for j in range(temperatures.shape[1]):
        ax1.text(j, i, f'{temperatures[i, j]}°C', ha='center', va='center', color='black', fontsize=9)

# Add a second y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(planets, distances, color='black', marker='o', linestyle='-', linewidth=2, label='Distance from Sun (AU)')
ax2.set_ylabel('Distance from Sun (AU)', fontsize=12)
ax2.set_ylim([0, 35])
ax2.yaxis.label.set_color('black')

# Title and layout adjustments
plt.title('Solar System Temperature Variations\nwith Distances from the Sun', fontsize=16, pad=30)
fig.tight_layout()

# Legend
ax2.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# Display the plot
plt.show()