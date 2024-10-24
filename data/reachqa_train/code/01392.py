import matplotlib.pyplot as plt
import numpy as np

# Data for the line chart
decades = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
average_heights = np.array([80, 120, 150, 170, 180, 200, 300, 350, 400, 450, 500, 600, 650])

# Plot setup
plt.figure(figsize=(12, 7))
plt.plot(decades, average_heights, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8)

# Customize plot
plt.title('Evolution of Skyscraper Heights\nOver the 20th and 21st Centuries', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Average Height of Tallest Skyscraper (meters)', fontsize=12)
plt.xticks(decades, rotation=45)
plt.yticks(np.arange(0, 701, step=50))
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(['Average Height'], loc='upper left', fontsize=10)

# Annotate key milestones
milestones = {'1900s': 80, '1960s': 300, '2010s': 600}
for decade, height in milestones.items():
    plt.annotate(f'{decade}: {height}m', xy=(int(decade[:-1] + '0'), height), xytext=(-40, 10),
                 textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()