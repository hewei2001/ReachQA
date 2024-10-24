import matplotlib.pyplot as plt
import numpy as np

# Define the time points (decades)
years = np.array([2050, 2060, 2070, 2080, 2090, 2100])

# Define fleet sizes for each corporation at each time point
nebula_transports = np.array([25, 45, 70, 110, 150, 200])
stellar_pathways = np.array([30, 55, 85, 100, 140, 185])
quantum_courier = np.array([20, 50, 80, 115, 160, 210])
astro_express = np.array([15, 40, 65, 105, 135, 190])

# Create the plot
plt.figure(figsize=(12, 8))

plt.plot(years, nebula_transports, label='Nebula Transports', marker='o', linestyle='-', linewidth=2, color='navy')
plt.plot(years, stellar_pathways, label='Stellar Pathways', marker='s', linestyle='--', linewidth=2, color='darkorange')
plt.plot(years, quantum_courier, label='Quantum Courier', marker='^', linestyle='-.', linewidth=2, color='forestgreen')
plt.plot(years, astro_express, label='Astro Express', marker='d', linestyle=':', linewidth=2, color='crimson')

# Set title and labels
plt.title('Growth of Galactic Transport Fleets\nin the Noveria Galaxy (2050-2100)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Fleet Ships', fontsize=12)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend to describe each corporation
plt.legend(title='Corporations', title_fontsize=12, fontsize=10, loc='upper left')

# Optimize layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()