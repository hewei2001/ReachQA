import matplotlib.pyplot as plt
import numpy as np

# Define regions and corresponding renewable energy data (in terawatt-hours)
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
solar_energy = [150, 180, 210, 100, 80, 50]
wind_energy = [220, 300, 250, 130, 90, 60]
hydro_energy = [400, 350, 450, 500, 200, 100]
bioenergy = [120, 100, 150, 60, 40, 30]

# Calculate total energy for annotations
total_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy) + np.array(bioenergy)

# Set colors for different energy types
colors = ['#FFD700', '#7EC8E3', '#00FF00', '#FF5733']  # Solar, Wind, Hydro, Bioenergy

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the bar segments
ax.bar(regions, solar_energy, label='Solar Energy', color=colors[0], edgecolor='black')
ax.bar(regions, wind_energy, bottom=solar_energy, label='Wind Energy', color=colors[1], edgecolor='black')
ax.bar(regions, hydro_energy, bottom=np.array(solar_energy) + np.array(wind_energy), label='Hydro Energy', color=colors[2], edgecolor='black')
ax.bar(regions, bioenergy, bottom=np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy), label='Bioenergy', color=colors[3], edgecolor='black')

# Set title and labels with multi-line title for better visibility
ax.set_title('Renewable Energy Generation by Region\nin 2023', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Add a legend and customize its position
ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding annotations for total energy produced by each region
for i, total in enumerate(total_energy):
    ax.text(i, total + 20, f'{total} TWh', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()