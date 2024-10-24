import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the countries and sustainable energy production data (GWh)
countries = ['Country A', 'Country B', 'Country C']
solar = [80, 50, 100]  # Solar energy in GWh
wind = [60, 90, 70]    # Wind energy in GWh
hydro = [40, 60, 80]   # Hydro energy in GWh

# Compute positions for the bars
x = np.arange(len(countries))

# Create a figure with a 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the width of each bar
bar_width = 0.4

# Plot each energy source as a stacked 3D bar
ax.bar(x, solar, zs=0, zdir='y', label='Solar', color='#ffc857', alpha=0.9, hatch='//', width=bar_width)
ax.bar(x, wind, zs=0, zdir='y', bottom=solar, label='Wind', color='#4b8bbe', alpha=0.9, hatch='\\', width=bar_width)
ax.bar(x, hydro, zs=0, zdir='y', bottom=np.array(solar) + np.array(wind), label='Hydro', color='#5fbb72', alpha=0.9, hatch='--', width=bar_width)

# Customize the axes
ax.set_xlabel('Countries', fontsize=12, labelpad=10)
ax.set_ylabel('Energy Types', fontsize=12, labelpad=10)
ax.set_zlabel('Energy Production (GWh)', fontsize=12, labelpad=10)
ax.set_xticks(x)
ax.set_xticklabels(countries, fontsize=10)
ax.set_yticks([])  # Hide the y-axis labels for energy types

# Add a customized legend
ax.legend(loc='upper left', fontsize=10, title='Energy Sources', title_fontsize='13')

# Add detailed annotations
total_energy = np.array(solar) + np.array(wind) + np.array(hydro)
for i in range(len(countries)):
    ax.text(x[i], 0, total_energy[i] + 5, f"{total_energy[i]} GWh", ha='center', fontsize=10, fontweight='bold')

# Title with line breaks for better readability
ax.set_title('Innovations in Sustainable Energy\nProduction by Country (2023)', fontsize=14, fontweight='bold', pad=20)

# Adjust the layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()