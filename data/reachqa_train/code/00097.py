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

# Create the line plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the data
ax.plot(days, wind_speed, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Recorded Wind Speed')

# Title and labels
ax.set_title('The Journey of Sailing Expeditions:\nWind Speed vs. Time', fontsize=16, fontweight='bold')
ax.set_xlabel('Day of Expedition', fontsize=12)
ax.set_ylabel('Wind Speed (knots)', fontsize=12)

# Customize grid and background
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f7fbfc')

# Highlight optimal wind speed
ax.axhline(y=15, color='gray', linestyle='--', linewidth=1, label='Optimal Wind Speed')

# Annotations for contextual insights
ax.text(1, 16, "Steady Winds", fontsize=10, color='green', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))
ax.text(25, 6, "Light Breezes", fontsize=10, color='red', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.5))

# Configure legend
ax.legend(loc='upper left', fontsize=10, framealpha=1)

# Adjust layout to ensure everything is visible
plt.tight_layout()

# Show the plot
plt.show()