import matplotlib.pyplot as plt
import numpy as np

# Define the decades for the x-axis, expanded range
decades = ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', 
           '1980s', '1990s', '2000s', '2010s', '2020s', '2030s', '2040s']

# Forest composition data in millions of square kilometers
# Expanded data with realistic fluctuations and projections
tropical_forests = np.array([20, 19, 19, 18, 18, 18, 18, 17, 16, 15, 15, 14, 13])
boreal_forests = np.array([15, 15, 15, 14, 14, 14, 14, 14, 14, 13, 13, 12, 12])
temperate_forests = np.array([7, 7, 8, 8, 8, 8, 8, 8, 9, 10, 10, 11, 11])
subtropical_forests = np.array([9, 9, 10, 10, 10, 10, 10, 11, 12, 12, 12, 13, 14])
mangrove_forests = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# Create the figure and axis for the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the stacked bars with distinct colors for each forest type
ax.bar(decades, tropical_forests, label='Tropical', color='#1f78b4', alpha=0.85)
ax.bar(decades, boreal_forests, bottom=tropical_forests, label='Boreal', color='#33a02c', alpha=0.85)
ax.bar(decades, temperate_forests, bottom=tropical_forests + boreal_forests, label='Temperate', color='#e31a1c', alpha=0.85)
ax.bar(decades, subtropical_forests, bottom=tropical_forests + boreal_forests + temperate_forests, label='Subtropical', color='#ff7f00', alpha=0.85)
ax.bar(decades, mangrove_forests, bottom=tropical_forests + boreal_forests + temperate_forests + subtropical_forests, label='Mangrove', color='#6a3d9a', alpha=0.85)

# Titles and labels with multi-line title for clarity
ax.set_title("Shifting Landscapes Across a Century:\nChanges in Earth's Forest Composition (1920s-2040s)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Decades", fontsize=12)
ax.set_ylabel("Forest Area (Million sq. km)", fontsize=12)

# Add gridlines to improve readability
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Rotate x-ticks for better visibility
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Add a legend to differentiate forest types
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Adding a secondary y-axis for additional environmental factor, e.g., carbon sequestration (hypothetical data)
carbon_sequestration = np.array([400, 380, 360, 350, 345, 340, 335, 330, 320, 310, 300, 295, 290])
ax2 = ax.twinx()
ax2.plot(decades, carbon_sequestration, label='Carbon Sequestration', color='#a6cee3', linestyle='-', marker='o', linewidth=2)
ax2.set_ylabel('Carbon Sequestration (Million Tons)', fontsize=12)
ax2.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 0.9))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()