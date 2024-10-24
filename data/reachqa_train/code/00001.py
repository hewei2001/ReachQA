import matplotlib.pyplot as plt
import numpy as np

# Decades of exploration
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Intensity of the ocean currents (artificially created for demonstration)
gulf_stream = np.array([5, 12, 20, 25, 35, 45, 60, 75])
kuroshio_current = np.array([3, 10, 15, 22, 30, 40, 55, 70])
antarctic_circumpolar = np.array([4, 9, 17, 22, 32, 42, 58, 68])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each ocean current
ax.plot(decades, gulf_stream, marker='o', linestyle='-', color='b', linewidth=2, label='Gulf Stream')
ax.plot(decades, kuroshio_current, marker='s', linestyle='--', color='g', linewidth=2, label='Kuroshio Current')
ax.plot(decades, antarctic_circumpolar, marker='^', linestyle=':', color='r', linewidth=2, label='Antarctic Circumpolar')

# Title and labels
ax.set_title('Exploration of the Depths: Mapping Ocean Currents Over Time', fontsize=14, pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Current Intensity (arbitrary units)', fontsize=12)

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Legend placement to avoid overlap
ax.legend(loc='upper left', fontsize=10, frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()