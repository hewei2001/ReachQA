import matplotlib.pyplot as plt
import numpy as np

# Define years and energy production data
years = np.arange(2013, 2023)
solar_energy = [12, 20, 35, 50, 70, 100, 130, 160, 190, 220]
wind_energy = [40, 55, 75, 95, 120, 150, 180, 210, 245, 280]
hydro_energy = [100, 102, 105, 110, 115, 120, 125, 130, 135, 140]

# Stack the data to show cumulative energy production
production_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plot the area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, production_data, labels=['Solar Energy', 'Wind Energy', 'Hydroelectric Energy'],
             colors=['#ffdd57', '#57a0ff', '#57ff86'], alpha=0.8)

# Add titles and labels
plt.title('Renewable Energy Production Trends\nOver the Last Decade (2013-2022)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (TWh)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Customize ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 701, 100))

# Add a grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate notable trends
ax.annotate('Rapid Solar Growth', xy=(2018, 70), xytext=(2015, 140),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkorange')

ax.annotate('Steady Wind Expansion', xy=(2020, 215), xytext=(2016, 320),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='blue')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()