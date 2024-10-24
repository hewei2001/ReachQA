import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2030, 2040)

# Define the energy utilization in gigawatt-hours for each type of renewable energy
solar_power = [300, 350, 410, 480, 560, 640, 730, 830, 940, 1060]
wind_energy = [50, 60, 75, 90, 110, 135, 160, 190, 225, 265]
biofuels = [40, 42, 45, 48, 52, 56, 60, 65, 70, 75]

# Stack the data
data = np.vstack([solar_power, wind_energy, biofuels])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Creating the stacked area plot
ax.stackplot(years, data, labels=['Solar Power', 'Wind Energy', 'Biofuels'],
             colors=['#FFD700', '#B0E0E6', '#90EE90'], alpha=0.8)

# Customize the plot with a backstory
ax.set_title('Renewable Energy Utilization in Martian Colonies\n2030 to 2039', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Utilization (GWh)', fontsize=12)

# Add legend with title, positioned outside the main plot area
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, bbox_to_anchor=(1, 1))

# Customize grid lines to improve readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Avoid overlapping x-axis labels by adjusting rotation
plt.xticks(years, rotation=45)

# Automatically adjust layout to ensure nothing is clipped
plt.tight_layout()

# Display the plot
plt.show()