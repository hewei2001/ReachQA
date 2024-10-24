import matplotlib.pyplot as plt
import numpy as np

# Days of the expedition
days = np.arange(1, 31)

# Hypothetical wind speed data (in knots)
wind_speed = [
    12, 15, 14, 10, 8, 7, 13, 17, 14, 16, 
    11, 15, 18, 19, 12, 10, 14, 16, 15, 20, 
    18, 17, 13, 11, 9, 7, 8, 12, 15, 18
]

# Hypothetical precipitation data (in mm)
precipitation = [
    5, 3, 4, 1, 0, 0, 2, 6, 3, 1,
    0, 4, 7, 6, 1, 0, 3, 5, 2, 8,
    7, 6, 1, 0, 0, 0, 1, 3, 4, 6
]

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot the wind speed line plot
ax1.plot(days, wind_speed, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Recorded Wind Speed')
ax1.axhline(y=15, color='gray', linestyle='--', linewidth=1, label='Optimal Wind Speed')

# Title and labels for primary axis
ax1.set_title('The Journey of Sailing Expeditions:\nWind Speed and Precipitation vs. Time', fontsize=16, fontweight='bold')
ax1.set_xlabel('Day of Expedition', fontsize=12)
ax1.set_ylabel('Wind Speed (knots)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('#f7fbfc')

# Highlight zones with annotations
ax1.text(1, 16, "Steady Winds", fontsize=10, color='green', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))
ax1.text(25, 6, "Light Breezes", fontsize=10, color='red', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))

# Legend for the wind speed
ax1.legend(loc='upper left', fontsize=10, framealpha=1)

# Create a secondary y-axis for the bar plot
ax2 = ax1.twinx()

# Plot the precipitation bar plot
bars = ax2.bar(days, precipitation, color='cyan', alpha=0.5, label='Precipitation (mm)')

# Labels and customization for secondary axis
ax2.set_ylabel('Precipitation (mm)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, framealpha=1)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()