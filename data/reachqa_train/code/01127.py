import matplotlib.pyplot as plt
import numpy as np

# Times of the day (in hours)
hours = np.array([4, 8, 12, 16, 20, 24])

# Energy outputs in megawatts for each source at these times
solar_output = np.array([15, 60, 95, 65, 35, 10])
wind_output = np.array([35, 55, 75, 55, 70, 55])
hydro_output = np.array([25, 25, 25, 25, 25, 25])

# Additional data for energy demand at these times
energy_demand = np.array([50, 80, 120, 90, 60, 40])

# Convert hours to radians for the rose plot
theta = np.radians((hours / 24) * 360)

# Create the figure and a polar subplot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 8))

# Calculate angle for each sector
sector_angle = np.radians(360 / len(hours))

# Plot each energy source using stacked bars
ax.bar(theta, solar_output, width=sector_angle, color='yellow', alpha=0.7, label='Solar')
ax.bar(theta, wind_output, width=sector_angle, color='blue', alpha=0.7, label='Wind', bottom=solar_output)
ax.bar(theta, hydro_output, width=sector_angle, color='green', alpha=0.7, label='Hydro', bottom=solar_output + wind_output)

# Overlay a line plot for energy demand
ax.plot(theta, energy_demand, color='red', marker='o', linestyle='--', linewidth=2, label='Energy Demand')

# Set the title and labels
ax.set_title('Renewable Energy Output and Demand\nThroughout the Day', fontsize=16, fontweight='bold', va='bottom')
ax.set_xticks(theta)
ax.set_xticklabels(['4 AM', '8 AM', '12 PM', '4 PM', '8 PM', '12 AM'], fontsize=12, weight='bold', rotation=45)
ax.set_yticks(range(0, 201, 50))
ax.set_yticklabels(['0 MW', '50 MW', '100 MW', '150 MW', '200 MW'], fontsize=10)

# Add a legend and adjust its position to prevent overlap
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Legend')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()