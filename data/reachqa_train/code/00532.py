import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Altitude data (meters) for each mountain range
himalayas_altitude = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000])
andes_altitude = np.array([1200, 1700, 2200, 2700, 3200, 3700, 4200, 4700, 5200])
rockies_altitude = np.array([800, 1300, 1800, 2300, 2800, 3300, 3800, 4300, 4800])

# Flora variety (number of species) corresponding to altitudes
himalayas_flora = np.array([50, 70, 90, 85, 95, 110, 105, 100, 115])
andes_flora = np.array([45, 65, 85, 80, 100, 105, 95, 110, 120])
rockies_flora = np.array([40, 60, 80, 75, 85, 95, 90, 105, 100])

# Temperature data (degrees Celsius) derived based on altitude for illustrative purposes
himalayas_temp = 30 - himalayas_altitude * 0.005
andes_temp = 28 - andes_altitude * 0.005
rockies_temp = 26 - rockies_altitude * 0.005

# Create the figure and axis objects for plotting
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot for flora variety
ax1.scatter(himalayas_altitude, himalayas_flora, s=100, color='darkblue', 
            marker='o', label='Himalayas Flora', alpha=0.7, edgecolor='black')
ax1.scatter(andes_altitude, andes_flora, s=100, color='darkgreen', 
            marker='^', label='Andes Flora', alpha=0.7, edgecolor='black')
ax1.scatter(rockies_altitude, rockies_flora, s=100, color='sienna', 
            marker='s', label='Rockies Flora', alpha=0.7, edgecolor='black')

# Line plot for temperature data on a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(himalayas_altitude, himalayas_temp, color='lightblue', linestyle='--', linewidth=2, label='Himalayas Temp')
ax2.plot(andes_altitude, andes_temp, color='lightgreen', linestyle='--', linewidth=2, label='Andes Temp')
ax2.plot(rockies_altitude, rockies_temp, color='lightsalmon', linestyle='--', linewidth=2, label='Rockies Temp')

# Calculate and plot trend lines (linear regression) for flora variety
for alt, flora, color in [(himalayas_altitude, himalayas_flora, 'blue'),
                          (andes_altitude, andes_flora, 'green'),
                          (rockies_altitude, rockies_flora, 'brown')]:
    slope, intercept, _, _, _ = stats.linregress(alt, flora)
    ax1.plot(alt, slope*alt + intercept, color=color, alpha=0.3, linewidth=2, linestyle='-')

# Axis labels and titles
ax1.set_title('Altitude vs. Flora Variety Across\nMajor Mountain Ranges with Temperature Overlay', fontsize=16, fontweight='bold', color='darkslategray')
ax1.set_xlabel('Altitude (meters)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Flora Variety (Number of Species)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Temperature (°C)', fontsize=12, fontweight='bold', color='gray')

# Adding grid lines and legends
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend(title='Flora Data', loc='upper left', fontsize=10)
ax2.legend(title='Temperature Data', loc='upper right', fontsize=10)

# Annotate peak diversity
ax1.annotate('Peak Diversity', xy=(5000, 115), xytext=(5100, 125),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='navy')

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plot
plt.show()