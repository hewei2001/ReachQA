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

# Additional hypothetical data for economic impact in billion USD
ai_economic_impact = [1, 2, 4, 6, 10, 15, 20, 28, 35, 45, 55, 65, 75, 85, 95, 105, 120, 135, 150, 170, 190, 210, 225, 235, 245, 260, 270, 280, 290, 300, 310]
renewable_energy_economic_impact = [2, 3, 5, 8, 11, 16, 22, 30, 40, 50, 60, 72, 85, 95, 105, 120, 135, 150, 165, 180, 195, 210, 220, 230, 245, 260, 275, 290, 305, 320, 335]
quantum_computing_economic_impact = [0.5, 1, 1.5, 2, 3, 5, 8, 12, 18, 25, 32, 40, 50, 60, 75, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390]
biotechnology_economic_impact = [1, 1.5, 2.5, 4, 6, 9, 13, 19, 28, 36, 45, 56, 68, 80, 92, 105, 120, 135, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390]

# Plot setup with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plot 1: Technological Growth Over Time
ax1.plot(years, ai_growth, label='Artificial Intelligence', marker='o', color='tab:blue', linestyle='-')
ax1.plot(years, renewable_energy_growth, label='Renewable Energy', marker='s', color='tab:green', linestyle='--')
ax1.plot(years, quantum_computing_growth, label='Quantum Computing', marker='^', color='tab:red', linestyle='-.')
ax1.plot(years, biotechnology_growth, label='Biotechnology', marker='d', color='tab:orange', linestyle=':')

# Title and axis labels
ax1.set_title('Technological Maturity Index\n2000-2030', fontsize=16, pad=10)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Adoption and Maturity Index', fontsize=12)

# Configure x and y ticks
ax1.set_xticks(np.arange(2000, 2031, 2))
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_xlim(2000, 2030)
ax1.set_ylim(0, 100)

# Add gridlines
ax1.grid(True, linestyle='--', alpha=0.7)

# Legend
ax1.legend(title='Technologies', loc='upper left', fontsize=10)

# Plot 2: Economic Impact Over Time
ax2.bar(years - 0.3, ai_economic_impact, width=0.2, label='AI Impact', color='tab:blue')
ax2.bar(years - 0.1, renewable_energy_economic_impact, width=0.2, label='Renewable Impact', color='tab:green')
ax2.bar(years + 0.1, quantum_computing_economic_impact, width=0.2, label='Quantum Impact', color='tab:red')
ax2.bar(years + 0.3, biotechnology_economic_impact, width=0.2, label='BioTech Impact', color='tab:orange')

# Title and axis labels
ax2.set_title('Economic Impact of Technologies\nin Billions USD (2000-2030)', fontsize=16, pad=10)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Economic Impact (Billion USD)', fontsize=12)

# Configure x and y ticks
ax2.set_xticks(np.arange(2000, 2031, 2))
ax2.set_xlim(2000, 2030)

# Add gridlines
ax2.grid(True, linestyle='--', alpha=0.7)

# Legend
ax2.legend(title='Technologies', loc='upper left', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()