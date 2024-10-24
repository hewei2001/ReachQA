import matplotlib.pyplot as plt
import numpy as np

# Define the time points (decades)
years = np.array([2050, 2060, 2070, 2080, 2090, 2100])

# Define fleet sizes for each corporation at each time point
nebula_transports = np.array([25, 45, 70, 110, 150, 200])
stellar_pathways = np.array([30, 55, 85, 100, 140, 185])
quantum_courier = np.array([20, 50, 80, 115, 160, 210])
astro_express = np.array([15, 40, 65, 105, 135, 190])

# Calculate cumulative fleet sizes
cumulative_fleet_sizes = nebula_transports + stellar_pathways + quantum_courier + astro_express

# Create a figure with two subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# First subplot - line plot for fleet growth
axs[0].plot(years, nebula_transports, label='Nebula Transports', marker='o', linestyle='-', linewidth=2, color='navy')
axs[0].plot(years, stellar_pathways, label='Stellar Pathways', marker='s', linestyle='--', linewidth=2, color='darkorange')
axs[0].plot(years, quantum_courier, label='Quantum Courier', marker='^', linestyle='-.', linewidth=2, color='forestgreen')
axs[0].plot(years, astro_express, label='Astro Express', marker='d', linestyle=':', linewidth=2, color='crimson')

# Title and labels for the first subplot
axs[0].set_title('Growth of Galactic Transport Fleets\nin the Noveria Galaxy (2050-2100)', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Number of Fleet Ships', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(title='Corporations', title_fontsize=12, fontsize=10, loc='upper left')

# Second subplot - stacked area plot for cumulative fleet size
axs[1].stackplot(years, nebula_transports, stellar_pathways, quantum_courier, astro_express,
                 labels=['Nebula Transports', 'Stellar Pathways', 'Quantum Courier', 'Astro Express'],
                 colors=['navy', 'darkorange', 'forestgreen', 'crimson'], alpha=0.8)

# Title and labels for the second subplot
axs[1].set_title('Cumulative Fleet Size of\nAll Corporations (2050-2100)', fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Fleet Size', fontsize=12)
axs[1].legend(loc='upper left', title='Corporations', title_fontsize=12, fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Optimize layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()