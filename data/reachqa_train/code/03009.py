import matplotlib.pyplot as plt
import numpy as np

# Years of exploration
years = np.arange(2010, 2020)

# New species discoveries by each research vessel over the years
discoveries = {
    'Abyss Explorer': np.array([5, 10, 15, 10, 20, 25, 30, 28, 35, 40]),
    'Ocean Voyager': np.array([3, 6, 9, 12, 15, 18, 22, 25, 30, 35]),
    'Deep Blue': np.array([2, 5, 8, 10, 12, 15, 20, 25, 27, 30]),
    'Seafloor Surveyor': np.array([1, 3, 5, 7, 10, 13, 15, 18, 20, 25]),
}

# Colors for each research vessel
colors = ['#7fc97f', '#beaed4', '#fdc086', '#386cb0']

# Create a stacked area plot
plt.figure(figsize=(12, 8))
plt.stackplot(years, discoveries.values(), labels=discoveries.keys(), colors=colors, alpha=0.7)

# Add title and labels
plt.title('Expeditions and Discoveries of Deep Ocean Species\nOver Time', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of New Species Discovered', fontsize=14)

# Rotate x-axis labels to prevent overlap
plt.xticks(years, rotation=45)

# Add legend
plt.legend(title='Research Vessels', title_fontsize=12, fontsize=10, loc='upper left')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Make layout tight to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()