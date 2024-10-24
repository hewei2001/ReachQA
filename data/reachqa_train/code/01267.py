import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the thematic innovations for each
decades = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
innovations = np.array([5, 8, 12, 15, 20, 25, 28, 30, 32, 35, 38])
# Define standard deviations
std_devs = np.array([1.5, 2, 1, 3, 2, 2.5, 2, 2.2, 2.5, 3, 3.5])

# Initialize the plot
plt.figure(figsize=(12, 7))

# Plot the line chart with error bars
plt.errorbar(decades, innovations, yerr=std_devs, fmt='-o', color='darkblue',
             ecolor='skyblue', elinewidth=2, capsize=4, capthick=2, alpha=0.8,
             label='Thematic Innovations')

# Customize plot
plt.title("The Evolution of Science Fiction Literature\nThematic Innovations Over Decades", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Decades", fontsize=12)
plt.ylabel("Number of New Thematic Innovations", fontsize=12)
plt.xticks(decades, rotation=45)
plt.yticks(np.arange(0, 45, 5))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
plt.legend(loc='upper left')

# Automatically adjust the layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()