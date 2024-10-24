import matplotlib.pyplot as plt
import numpy as np

# Define data for light intensity (in Lux) and average plant height (in cm)
light_intensity = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(light_intensity, plant_height, color='forestgreen', edgecolors='black', s=100, alpha=0.7)

# Add a trend line to show general growth pattern
z = np.polyfit(light_intensity, plant_height, 2)  # Fit a quadratic polynomial
p = np.poly1d(z)
plt.plot(light_intensity, p(light_intensity), "r--", label='Trend Line', linewidth=1.5)

# Customize the plot with titles and labels
plt.title('Impact of Light Intensity on Plant Growth\nAverage Plant Heights in Controlled Environment', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Light Intensity (Lux)', fontsize=12)
plt.ylabel('Average Plant Height (cm)', fontsize=12)

# Annotate some key points for emphasis
for i in range(len(light_intensity)):
    plt.text(light_intensity[i] + 10, plant_height[i] + 0.5, f'{plant_height[i]}cm', fontsize=9, ha='left')

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Growth Pattern', loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()