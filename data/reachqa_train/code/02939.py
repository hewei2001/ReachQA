import matplotlib.pyplot as plt
import numpy as np

# Define the years and planet-specific exports
years = np.arange(3050, 3055)
planets = ['Zerion', 'Yutopia', 'Cetheron', 'Luthar']

# Export data for each commodity (in thousands of tons)
tritanium_exports = [50, 55, 52, 54, 53]       # Zerion
dilithium_exports = [20, 22, 23, 25, 24]       # Yutopia
plasmoid_exports = [30, 33, 35, 36, 38]        # Cetheron
quantum_flux_exports = [10, 15, 18, 20, 22]    # Luthar

# Colors for the stacked bars
colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each layer of the stack
ax.bar(years, tritanium_exports, label='Tritanium - Zerion', color=colors[0])
ax.bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Yutopia', color=colors[1])
ax.bar(years, plasmoid_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports), label='Plasmoid - Cetheron', color=colors[2])
ax.bar(years, quantum_flux_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports) + np.array(plasmoid_exports), label='Quantum Flux - Luthar', color=colors[3])

# Title and Axis Labels
ax.set_title("Intergalactic Commodity Exports\nfrom Major Alien Planets (3050-3054)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Export Quantity (Thousands of Tons)", fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Configure legend and position
ax.legend(title='Commodities by Planet', loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines for easier reading
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent clipping of labels and titles
plt.tight_layout()

# Display the plot
plt.show()