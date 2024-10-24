import matplotlib.pyplot as plt
import numpy as np

# Energy consumption data in petajoules (PJ) for different sectors
sectors = ['Transportation', 'Industry', 'Residential', 'Commercial', 'Agriculture']
energy_consumption = [1500, 1200, 900, 700, 400]

# Generate a numerical range for the x-axis positions
x_positions = np.arange(len(sectors))

# Colors for the bars
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars with labels and colors
bars = ax.bar(x_positions, energy_consumption, color=colors, edgecolor='black', width=0.6)

# Add data value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval} PJ', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Title and labels
ax.set_title('Energy Consumption by Sector in the 2030s:\nAn Emphasis on Sustainability', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Economic Sectors', fontsize=12)
ax.set_ylabel('Energy Consumption (Petajoules)', fontsize=12)

# Set x-axis ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(sectors, rotation=30, ha='right', fontsize=10)

# Add a grid for y-axis for easier readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()