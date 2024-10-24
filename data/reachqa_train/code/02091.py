import matplotlib.pyplot as plt
import numpy as np

# Data for Renewable Energy Adoption in EcoVille
years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])
wind_capacity = np.array([70, 80, 90, 110, 130, 150, 180, 220, 260, 300, 350])

# Calculate additional data for the second subplot
total_capacity = solar_capacity + wind_capacity
solar_percentage = (solar_capacity / total_capacity) * 100
wind_percentage = (wind_capacity / total_capacity) * 100

# Set up subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# First subplot: Line plot for Solar and Wind Energy
ax1.plot(years, solar_capacity, marker='o', linestyle='-', color='orange', label='Solar Energy', linewidth=2)
ax1.plot(years, wind_capacity, marker='s', linestyle='--', color='blue', label='Wind Energy', linewidth=2)

for i, (x, y) in enumerate(zip(years, solar_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='orange')

for i, (x, y) in enumerate(zip(years, wind_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(10,-15), ha='center', fontsize=8, color='blue')

ax1.set_title('Renewable Energy Adoption in EcoVille\n(2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Installed Capacity (MW)', fontsize=10)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
ax1.text(2015, max(max(solar_capacity), max(wind_capacity)) + 20, 'Paris Agreement', ha='center', color='gray')

# Second subplot: Stacked area plot for percentage of Solar and Wind Energy
ax2.stackplot(years, solar_percentage, wind_percentage, labels=['Solar %', 'Wind %'], colors=['orange', 'blue'], alpha=0.6)
ax2.set_title('Percentage of Renewable Energy Contribution\n(2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Percentage of Total Capacity (%)', fontsize=10)
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()