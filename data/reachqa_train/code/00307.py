import matplotlib.pyplot as plt
import numpy as np

# Define the cities and times of day for the heat map
cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
times_of_day = ["Early Morning", "Morning", "Afternoon", "Evening", "Night", "Late Night"]

# Artificial data representing average noise levels in decibels for each city at different times of the day
noise_levels = np.array([
    [60, 68, 70, 65, 62, 55],  # New York
    [55, 63, 65, 60, 58, 52],  # London
    [58, 70, 75, 68, 65, 60],  # Tokyo
    [50, 58, 60, 55, 52, 48],  # Paris
    [53, 60, 68, 62, 57, 50]   # Sydney
])

# Create the heat map using imshow
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(noise_levels, cmap='viridis', aspect='auto', interpolation='nearest')

# Add city names and times of day as labels for the axes
ax.set_xticks(np.arange(len(times_of_day)))
ax.set_yticks(np.arange(len(cities)))
ax.set_xticklabels(times_of_day)
ax.set_yticklabels(cities)

# Rotate x-tick labels and align them to prevent overlapping
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add annotations to each cell to show the exact noise levels
for i in range(len(cities)):
    for j in range(len(times_of_day)):
        ax.text(j, i, f"{noise_levels[i, j]} dB",
                ha="center", va="center", color="white", fontsize=9)

# Include a color bar to provide a scale for the noise levels
cbar = fig.colorbar(cax, orientation='vertical', pad=0.02)
cbar.set_label('Noise Level (dB)', fontsize=10)

# Set a title and labels for clarity
ax.set_title("Urban Soundscape:\nNoise Levels Across Global Cities", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Time of Day', fontsize=12)
ax.set_ylabel('City', fontsize=12)

# Automatically adjust layout to prevent clipping of labels and titles
plt.tight_layout()

# Display the heat map
plt.show()