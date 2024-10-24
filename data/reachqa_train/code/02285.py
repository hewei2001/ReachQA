import matplotlib.pyplot as plt
import numpy as np

# Define the years of observation
years = np.arange(2015, 2026)

# Qubit counts for each company
quantum_leap = np.array([5, 8, 15, 18, 22, 30, 40, 55, 70, 85, 100])
entangled_technologies = np.array([7, 10, 14, 20, 25, 28, 35, 48, 60, 78, 95])
qubit_pioneers = np.array([6, 9, 13, 17, 24, 29, 33, 50, 68, 80, 98])

# Standard deviation for error bars
quantum_leap_std = np.array([0.5, 0.7, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
entangled_technologies_std = np.array([0.6, 0.8, 1.1, 1.3, 1.6, 2.1, 2.4, 3.2, 3.6, 4.1, 4.6])
qubit_pioneers_std = np.array([0.4, 0.9, 1.2, 1.4, 1.7, 1.8, 2.3, 2.9, 3.8, 4.2, 4.4])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each company's data with error bars
ax.errorbar(years, quantum_leap, yerr=quantum_leap_std, fmt='-o', capsize=5,
            label='QuantumLeap Innovations', color='blue', alpha=0.7)
ax.errorbar(years, entangled_technologies, yerr=entangled_technologies_std, fmt='-s', capsize=5,
            label='Entangled Technologies', color='green', alpha=0.7)
ax.errorbar(years, qubit_pioneers, yerr=qubit_pioneers_std, fmt='-^', capsize=5,
            label='QubitPioneers', color='red', alpha=0.7)

# Title and labels
ax.set_title('Advancements in Quantum Computing\nQubit Count by Leading Companies (2015-2025)', 
             fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Qubit Count', fontsize=14)

# Grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Companies', fontsize=12, title_fontsize='13', loc='upper left')

# Set x and y limits
ax.set_xlim([2015, 2025])
ax.set_ylim([0, 110])

# Rotate x-axis labels for better readability
ax.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()