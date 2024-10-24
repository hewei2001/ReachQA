import matplotlib.pyplot as plt
import numpy as np

# Original bar chart data: Energy consumption in petajoules (PJ) for different sectors
sectors = ['Transportation', 'Industry', 'Residential', 'Commercial', 'Agriculture']
energy_consumption = [1500, 1200, 900, 700, 400]

# Additional subplot data: Hypothetical trend of renewable energy adoption from 2020 to 2030 in the 'Industry' sector
years = np.arange(2020, 2031)
renewable_energy_adoption = [5, 10, 15, 20, 25, 30, 35, 42, 50, 60, 75]  # Percentages

# Setting up subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Energy Insights in the 2030s: Sector Usage and Renewable Trends', fontsize=16, fontweight='bold', y=0.95)

# Bar chart (Original plot)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
x_positions = np.arange(len(sectors))
bars = ax1.bar(x_positions, energy_consumption, color=colors, edgecolor='black', width=0.6)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval} PJ', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_title('Energy Consumption by Sector', fontsize=12, fontweight='bold')
ax1.set_xlabel('Economic Sectors', fontsize=10)
ax1.set_ylabel('Energy Consumption (Petajoules)', fontsize=10)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(sectors, rotation=30, ha='right', fontsize=9)
ax1.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)

# Line plot (New subplot)
ax2.plot(years, renewable_energy_adoption, marker='o', linestyle='-', color='#66b3ff', linewidth=2, markersize=5)
ax2.set_title('Trend of Renewable Energy Adoption\nin Industry Sector (2020-2030)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Renewable Energy Adoption (%)', fontsize=10)
ax2.set_xticks(years[::2])  # Show every other year for clarity
ax2.yaxis.grid(True, linestyle='--', color='grey', alpha=0.6)
ax2.set_ylim(0, 100)
ax2.fill_between(years, 0, renewable_energy_adoption, color='#c2c2f0', alpha=0.3)

plt.tight_layout(pad=3)
plt.show()