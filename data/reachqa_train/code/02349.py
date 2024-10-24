import matplotlib.pyplot as plt
import numpy as np

# Define the years for the study
years = np.arange(2010, 2021)

# Artificial data for green space area increase each year (hectares)
green_space_area = np.array([5, 7, 10, 14, 18, 22, 26, 31, 37, 43, 50])

# Corresponding environmental well-being index improvements
environmental_index = np.array([50, 52, 55, 58, 62, 65, 69, 74, 78, 83, 88])

plt.figure(figsize=(14, 7))

# Plot green space area with markers
plt.plot(years, green_space_area, '-o', color='forestgreen', label='Green Space Area (ha)',
         linewidth=2, markersize=7, markerfacecolor='darkgreen')

# Plot environmental well-being index with square markers
plt.plot(years, environmental_index, '-s', color='royalblue', label='Environmental Well-being Index',
         linewidth=2, markersize=7, markerfacecolor='navy')

# Title and labels
plt.title('Urban Green Spaces and Environmental Well-being in EcoVille\n2010-2020',
          fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Measure', fontsize=12)

# Legend placement
plt.legend(loc='upper left', fontsize=10)

# Ticks and grid
plt.xticks(years)
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate a significant point in the data
plt.annotate('Notable Expansion in 2015', xy=(2015, 22), xytext=(2015, 35),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=11, color='crimson')

# Prevent overlap by adjusting layout
plt.tight_layout()

# Display the plot
plt.show()