import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = [1990, 2000, 2010, 2020]

# Energy production data (in terawatt-hours, TWh)
coal = [1200, 1100, 950, 800]  # Gradual decline
natural_gas = [300, 500, 600, 750]  # Increased utilization
nuclear = [450, 500, 550, 600]  # Steady growth
hydroelectric = [150, 200, 250, 300]  # Consistent but slow growth
renewables = [20, 60, 200, 550]  # Significant increase over time

# Stack the data
energy_sources = np.vstack([coal, natural_gas, nuclear, hydroelectric, renewables])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each area with a distinctive color
ax.stackplot(years, energy_sources, labels=['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Renewables'],
             colors=['#8B0000', '#FFA500', '#4682B4', '#32CD32', '#FFD700'], alpha=0.8)

# Title and labels
ax.set_title('Energy Transition Over Time\nElectricity Production Sources (1990-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Electricity Production (TWh)', fontsize=12)

# Add a legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Enhance grid and layout
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years, rotation=45)
plt.tight_layout()

# Show the plot
plt.show()