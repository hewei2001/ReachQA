import numpy as np
import matplotlib.pyplot as plt

# Define months
months = np.arange(1, 13)

# Artificial data for renewable energy production (in GWh)
solar_energy = [10, 20, 30, 40, 60, 80, 85, 80, 70, 50, 20, 10]
wind_energy = [40, 50, 45, 60, 70, 65, 75, 80, 70, 60, 55, 50]
hydro_energy = [80, 70, 65, 60, 50, 40, 30, 30, 40, 60, 70, 80]
biomass_energy = [30, 30, 35, 40, 45, 50, 55, 60, 55, 50, 45, 40]

# Stack data for plotting
data = np.array([solar_energy, wind_energy, hydro_energy, biomass_energy])

# Colors for each energy source
colors = ['#FFD700', '#87CEEB', '#4682B4', '#228B22']

# Calculate total energy production
total_energy = np.sum(data, axis=0)

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 8))

# Stackplot for renewable energy sources
ax1.stackplot(months, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Add line plot for total energy production
ax1.plot(months, total_energy, label='Total Energy Production', color='black', linestyle='--', marker='o', linewidth=2)

# Title and labels
ax1.set_title('Renewable Energy Production Trends\nin a Hypothetical Region', fontsize=16, fontweight='bold', loc='center')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Energy Production (GWh)', fontsize=12)
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='right')

# Create a secondary Y-axis for cumulative energy production
ax2 = ax1.twinx()
cumulative_energy = np.cumsum(total_energy)
ax2.plot(months, cumulative_energy, label='Cumulative Energy', color='magenta', linestyle='-', marker='^', linewidth=2)
ax2.set_ylabel('Cumulative Energy (GWh)', fontsize=12)

# Customize legends and grid
ax1.legend(loc='upper left', title='Energy Sources', fontsize=10, title_fontsize=12)
ax2.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

# Annotate significant points
max_solar_month = np.argmax(solar_energy) + 1
max_solar_value = max(solar_energy)
ax1.annotate(f'Max Solar\n{max_solar_value} GWh', 
             xy=(max_solar_month, max_solar_value), 
             xytext=(max_solar_month + 0.5, max_solar_value + 20),
             arrowprops=dict(facecolor='darkred', arrowstyle='->'),
             fontsize=10, color='darkred', fontweight='bold')

max_total_month = np.argmax(total_energy) + 1
max_total_value = max(total_energy)
ax1.annotate(f'Peak Total\n{max_total_value} GWh',
             xy=(max_total_month, max_total_value),
             xytext=(max_total_month, max_total_value + 30),
             arrowprops=dict(facecolor='blue', arrowstyle='->'),
             fontsize=10, color='blue', fontweight='bold')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()