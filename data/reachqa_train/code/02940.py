import matplotlib.pyplot as plt
import numpy as np

# Define the years and planets
years = np.arange(3050, 3055)
planets = ['Zerion', 'Yutopia', 'Cetheron', 'Luthar']

# Export data for each commodity (in thousands of tons)
tritanium_exports = np.array([50, 55, 52, 54, 53])       # Zerion
dilithium_exports = np.array([20, 22, 23, 25, 24])       # Yutopia
plasmoid_exports = np.array([30, 33, 35, 36, 38])        # Cetheron
quantum_flux_exports = np.array([10, 15, 18, 20, 22])    # Luthar

# Colors for the charts
colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

# Calculate cumulative totals for line chart
total_exports = tritanium_exports + dilithium_exports + plasmoid_exports + quantum_flux_exports

# Yearly growth rate calculation
growth_rates = np.diff(total_exports) / total_exports[:-1] * 100  # as percentage

# Create 1x2 subplot
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Stacked Bar Chart
axs[0].bar(years, tritanium_exports, label='Tritanium - Zerion', color=colors[0])
axs[0].bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Yutopia', color=colors[1])
axs[0].bar(years, plasmoid_exports, bottom=tritanium_exports + dilithium_exports, label='Plasmoid - Cetheron', color=colors[2])
axs[0].bar(years, quantum_flux_exports, bottom=tritanium_exports + dilithium_exports + plasmoid_exports, label='Quantum Flux - Luthar', color=colors[3])

# Titles and Labels
axs[0].set_title("Intergalactic Commodity Exports\nfrom Major Alien Planets (3050-3054)", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Year", fontsize=14)
axs[0].set_ylabel("Export Quantity (Thousands of Tons)", fontsize=14)
axs[0].legend(title='Commodities by Planet', loc='upper left', bbox_to_anchor=(1, 1))
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Second subplot: Line Chart for Growth Rates
axs[1].plot(years[1:], growth_rates, marker='o', linestyle='-', color=colors[0], label='Total Export Growth Rate')
axs[1].set_title("Annual Export Growth Rate (%)\nAcross All Planets (3050-3054)", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Year", fontsize=14)
axs[1].set_ylabel("Growth Rate (%)", fontsize=14)
axs[1].grid(True, linestyle='--', alpha=0.7)

# Annotate points in line chart
for i, txt in enumerate(growth_rates):
    axs[1].annotate(f'{txt:.1f}%', (years[i+1], growth_rates[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()