import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define data for hypothetical planets
planet_names = ['Planet A', 'Planet B', 'Planet C', 'Planet D', 'Planet E',
                'Planet F', 'Planet G', 'Planet H', 'Planet I', 'Planet J']
temperatures = np.array([15, -50, 30, 100, -10, 60, 20, 50, -30, 5])  # in °C
pressures = np.array([1, 0.5, 2, 5, 0.1, 3, 0.8, 1.5, 0.3, 1.2])      # in atm
water_reserves = np.array([1500, 200, 1000, 500, 50, 800, 600, 700, 100, 1200])  # in km³

# Construct additional data: habitability score (hypothetical index)
habitability_scores = 1 / (1 + np.exp(-0.05 * (temperatures - 15))) * water_reserves / 100

# Initialize the figure with subplots
fig = plt.figure(figsize=(16, 8))

# First subplot: 3D Scatter Plot
ax1 = fig.add_subplot(121, projection='3d')
colors = plt.cm.coolwarm((temperatures - temperatures.min()) / (temperatures.max() - temperatures.min()))
scatter = ax1.scatter(temperatures, pressures, water_reserves, s=water_reserves / 5, c=colors, alpha=0.7, edgecolor='k')
ax1.set_xlabel('Temperature (°C)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Pressure (atm)', fontsize=12, fontweight='bold')
ax1.set_zlabel('Water Reserves (km³)', fontsize=12, fontweight='bold')
ax1.set_title('Planetary Conditions\nfor Extraterrestrial Life Forms', fontsize=14, fontweight='bold', pad=20)

for i, txt in enumerate(planet_names):
    ax1.text(temperatures[i], pressures[i], water_reserves[i], txt, size=8, zorder=1, color='black')

# Add color bar for temperature
mappable = plt.cm.ScalarMappable(cmap='coolwarm')
mappable.set_array(temperatures)
cbar1 = plt.colorbar(mappable, ax=ax1, pad=0.1)
cbar1.set_label('Surface Temperature (°C)', fontsize=10)

ax1.view_init(elev=30, azim=140)

# Second subplot: 2D Bar Chart for Habitability Score
ax2 = fig.add_subplot(122)
bars = ax2.bar(planet_names, habitability_scores, color=plt.cm.viridis(habitability_scores / max(habitability_scores)))
ax2.set_xlabel('Planets', fontsize=12, fontweight='bold')
ax2.set_ylabel('Habitability Score', fontsize=12, fontweight='bold')
ax2.set_title('Habitability Score for Each Planet', fontsize=14, fontweight='bold', pad=10)
ax2.set_xticklabels(planet_names, rotation=45, ha='right')

# Adding value labels on the bars
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom', ha='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()