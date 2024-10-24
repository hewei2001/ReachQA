import matplotlib.pyplot as plt
import numpy as np

# Define years and crop yields in tons per Martian acre
years = np.array([2050, 2051, 2052, 2053, 2054])
martian_potatoes = np.array([1.2, 1.5, 1.7, 2.0, 2.3])
red_wheat = np.array([0.9, 1.1, 1.4, 1.8, 2.0])
space_carrots = np.array([1.0, 1.2, 1.5, 1.7, 2.1])

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each crop type
plt.plot(years, martian_potatoes, marker='o', linestyle='-', linewidth=2, color='tab:orange', label='Martian Potatoes')
plt.plot(years, red_wheat, marker='s', linestyle='-', linewidth=2, color='tab:green', label='Red Wheat')
plt.plot(years, space_carrots, marker='^', linestyle='-', linewidth=2, color='tab:blue', label='Space Carrots')

# Title and labels
plt.title('Extraterrestrial Agriculture: \nCrop Yields on Mars (2050-2054)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Yield (tons per Martian acre)', fontsize=12)

# Ticks and grid
plt.xticks(years)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Legend
plt.legend(loc='upper left', fontsize=10)

# Annotations
plt.annotate('Experimentation begins', xy=(2050, 1.2), xytext=(2050, 1.5),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

plt.annotate('Optimal conditions achieved', xy=(2053, 2.0), xytext=(2052.7, 2.4),
             arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10, color='gray')

# Automatically adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()