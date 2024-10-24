import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2025
years = np.arange(2010, 2026)

# Data for renewable energy production in MWh with realistic growth trends
solar_energy = [
    120, 150, 190, 240, 290, 350, 420, 500, 590, 690,
    800, 920, 1050, 1190, 1350, 1520
]

wind_energy = [
    90, 110, 130, 160, 190, 230, 270, 320, 370, 430,
    500, 580, 670, 770, 880, 1000
]

hydro_energy = [
    200, 210, 220, 240, 260, 280, 300, 320, 340, 360,
    380, 400, 420, 440, 460, 480
]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each energy source
ax.plot(years, solar_energy, label='Solar Energy', marker='o', linestyle='-', linewidth=2.5, color='orange')
ax.plot(years, wind_energy, label='Wind Energy', marker='s', linestyle='-', linewidth=2.5, color='blue')
ax.plot(years, hydro_energy, label='Hydro Energy', marker='^', linestyle='-', linewidth=2.5, color='green')

# Set labels and title with multiple lines for better readability
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (MWh)', fontsize=12)
ax.set_title('Renewable Energy Production Trends\nin Green City (2010-2025)', fontsize=16, fontweight='bold')

# Customize ticks for better spacing and readability
ax.set_xticks(years[::2])  # Every other year
ax.set_yticks(np.arange(0, 1800, 200))

# Add grid for visual clarity
ax.grid(True, linestyle='--', alpha=0.6)

# Remove unnecessary plot spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a legend to help identify the data series
ax.legend(loc='upper left', fontsize=11)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()