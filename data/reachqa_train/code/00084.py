import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.arange(1, 13)

# Energy consumption data in terawatt-hours (TWh) for each source
solar_energy = np.array([15, 18, 25, 28, 30, 35, 40, 38, 30, 25, 20, 18])
wind_energy = np.array([20, 18, 15, 10, 12, 10, 8, 12, 18, 20, 22, 25])
fusion_energy = np.array([10, 12, 10, 15, 18, 20, 22, 20, 22, 25, 28, 27])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each energy source with transparency to prevent occlusion
ax.fill_between(months, solar_energy, color='gold', alpha=0.6, label='Solar Energy')
ax.fill_between(months, solar_energy + wind_energy, solar_energy, color='skyblue', alpha=0.6, label='Wind Energy')
ax.fill_between(months, solar_energy + wind_energy + fusion_energy, solar_energy + wind_energy, color='lightgreen', alpha=0.6, label='Fusion Energy')

# Adding title and labels
ax.set_title('Energy Dynamics in Lumina:\nA Year of Sustainability', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12)

# Set month names for the x-ticks
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Place the legend
ax.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the plot
plt.show()