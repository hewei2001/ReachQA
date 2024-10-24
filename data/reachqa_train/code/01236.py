import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the x-axis
decades = ['1980s', '1990s', '2000s', '2010s']

# Forest composition data in millions of square kilometers
tropical_forests = np.array([18, 17, 16, 15])
boreal_forests = np.array([14, 14, 14, 13])
temperate_forests = np.array([8, 8, 9, 10])
subtropical_forests = np.array([10, 11, 12, 12])

# Create the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the stacked bars with distinct colors for each forest type
ax.bar(decades, tropical_forests, label='Tropical', color='#1f78b4', alpha=0.85)
ax.bar(decades, boreal_forests, bottom=tropical_forests, label='Boreal', color='#33a02c', alpha=0.85)
ax.bar(decades, temperate_forests, bottom=tropical_forests + boreal_forests, label='Temperate', color='#e31a1c', alpha=0.85)
ax.bar(decades, subtropical_forests, bottom=tropical_forests + boreal_forests + temperate_forests, label='Subtropical', color='#ff7f00', alpha=0.85)

# Titles and labels
ax.set_title("Shifting Landscapes:\nChanges in Earth's Forest Composition (1980s-2010s)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Decades", fontsize=12)
ax.set_ylabel("Forest Area (Million sq. km)", fontsize=12)

# Improve readability with gridlines
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Rotate x-ticks for better visibility
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Add a legend to differentiate forest types
ax.legend(loc='upper right', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()