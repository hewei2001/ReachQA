import matplotlib.pyplot as plt
import numpy as np

# Define the years and technologies
years = np.arange(2000, 2031)
technologies = ['Artificial Intelligence', 'Renewable Energy', 'Quantum Computing', 'Biotechnology']

# Constructing hypothetical data for each technology over the years
ai_growth = [5, 8, 12, 18, 25, 30, 38, 45, 55, 60, 65, 70, 75, 80, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100, 100, 100, 100, 100, 100]
renewable_energy_growth = [10, 15, 20, 25, 30, 35, 40, 48, 55, 60, 65, 68, 72, 76, 79, 82, 85, 87, 89, 92, 94, 96, 97, 98, 99, 100, 100, 100, 100, 100, 100]
quantum_computing_growth = [1, 2, 3, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100, 100, 100]
biotechnology_growth = [7, 10, 15, 20, 25, 30, 35, 42, 50, 55, 60, 65, 70, 75, 78, 82, 85, 88, 90, 92, 94, 95, 96, 97, 98, 99, 100, 100, 100, 100, 100]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each technology with distinct styles
ax.plot(years, ai_growth, label='Artificial Intelligence', marker='o', color='tab:blue', linestyle='-')
ax.plot(years, renewable_energy_growth, label='Renewable Energy', marker='s', color='tab:green', linestyle='--')
ax.plot(years, quantum_computing_growth, label='Quantum Computing', marker='^', color='tab:red', linestyle='-.')
ax.plot(years, biotechnology_growth, label='Biotechnology', marker='d', color='tab:orange', linestyle=':')

# Title and axis labels
ax.set_title('The Dawn of Technological Advancement: 2000-2030', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Adoption and Maturity Index', fontsize=12)

# Configure x and y ticks
ax.set_xticks(np.arange(2000, 2031, 2))
ax.set_yticks(np.arange(0, 101, 10))
ax.set_xlim(2000, 2030)
ax.set_ylim(0, 100)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(title='Technologies', loc='upper left', fontsize=10)

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()