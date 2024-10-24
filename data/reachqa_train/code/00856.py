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

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#4682B4', '#228B22']

# Plot setup
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting area chart with stackplot
ax.stackplot(months, data, labels=['Solar', 'Wind', 'Hydro', 'Biomass'], colors=colors, alpha=0.8)

# Title and labels
ax.set_title('Annual Renewable Energy Production Trends\nin a Hypothetical Region', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, ha='right')

# Add legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=10, title_fontsize=12)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate a significant point in the data
max_solar_month = np.argmax(solar_energy) + 1
max_solar_value = max(solar_energy)
ax.annotate(f'Max Solar Output\n{max_solar_value} GWh', 
            xy=(max_solar_month, max_solar_value), 
            xytext=(max_solar_month + 0.5, max_solar_value + 10),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='darkred', fontweight='bold')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()