import matplotlib.pyplot as plt
import numpy as np

# Define the years of observation
years = np.arange(2015, 2026)

# Qubit counts for each company
quantum_leap = np.array([5, 8, 15, 18, 22, 30, 40, 55, 70, 85, 100])
entangled_technologies = np.array([7, 10, 14, 20, 25, 28, 35, 48, 60, 78, 95])
qubit_pioneers = np.array([6, 9, 13, 17, 24, 29, 33, 50, 68, 80, 98])

# Calculate percentage increase over the period for the second subplot
quantum_leap_growth = ((quantum_leap[-1] - quantum_leap[0]) / quantum_leap[0]) * 100
entangled_technologies_growth = ((entangled_technologies[-1] - entangled_technologies[0]) / entangled_technologies[0]) * 100
qubit_pioneers_growth = ((qubit_pioneers[-1] - qubit_pioneers[0]) / qubit_pioneers[0]) * 100

growth_data = [quantum_leap_growth, entangled_technologies_growth, qubit_pioneers_growth]
companies = ['QuantumLeap Innovations', 'Entangled Technologies', 'QubitPioneers']
colors = ['blue', 'green', 'red']

# Create a 1x2 subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Plot the original data with error bars
quantum_leap_std = np.array([0.5, 0.7, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
entangled_technologies_std = np.array([0.6, 0.8, 1.1, 1.3, 1.6, 2.1, 2.4, 3.2, 3.6, 4.1, 4.6])
qubit_pioneers_std = np.array([0.4, 0.9, 1.2, 1.4, 1.7, 1.8, 2.3, 2.9, 3.8, 4.2, 4.4])

ax1.errorbar(years, quantum_leap, yerr=quantum_leap_std, fmt='-o', capsize=5, label='QuantumLeap Innovations', color='blue', alpha=0.7)
ax1.errorbar(years, entangled_technologies, yerr=entangled_technologies_std, fmt='-s', capsize=5, label='Entangled Technologies', color='green', alpha=0.7)
ax1.errorbar(years, qubit_pioneers, yerr=qubit_pioneers_std, fmt='-^', capsize=5, label='QubitPioneers', color='red', alpha=0.7)

# Title and labels for the first subplot
ax1.set_title('Advancements in Quantum Computing\nQubit Count by Leading Companies (2015-2025)', fontsize=16, fontweight='bold', loc='center')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Qubit Count', fontsize=14)

# Grid and legend for the first subplot
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Companies', fontsize=12, title_fontsize='13', loc='upper left')
ax1.set_xlim([2015, 2025])
ax1.set_ylim([0, 110])
ax1.tick_params(axis='x', rotation=45)

# Second subplot: Bar Chart for Percentage Growth
ax2.bar(companies, growth_data, color=colors, alpha=0.7)
ax2.set_title('Percentage Growth of Qubit Count\n(2015-2025)', fontsize=16, fontweight='bold', loc='center')
ax2.set_xlabel('Companies', fontsize=14)
ax2.set_ylabel('Growth (%)', fontsize=14)
ax2.set_ylim(0, max(growth_data) + 10)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()