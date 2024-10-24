import matplotlib.pyplot as plt
import numpy as np

# Years over a decade
years = np.arange(2010, 2020)

# Production in GWh for each energy source
solar_energy = [20, 25, 30, 40, 50, 55, 60, 70, 80, 85]
wind_energy = [30, 35, 40, 45, 55, 60, 65, 75, 85, 90]
hydro_energy = [50, 52, 54, 53, 55, 56, 58, 60, 62, 64]

# Calculate total energy production
total_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy)

# Stack the data for plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Stacked area chart
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydroelectric'],
             colors=['#FDBF6F', '#1F78B4', '#33A02C'])

# Overlay line plot for total energy
ax.plot(years, total_energy, color='purple', linewidth=2.5, linestyle='--', marker='o', label='Total Production')

# Set title and labels
ax.set_title('Renewable Energy Production: Solar, Wind, and Hydroelectric\nwith Total Production Overlay (2010-2019)', fontsize=14, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (GWh)', fontsize=12)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend and position it outside the main plot area
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Energy Source')

# Highlight the year with maximum total energy production
max_year = years[np.argmax(total_energy)]
max_total = max(total_energy)
ax.annotate(f'Max Total: {max_total} GWh', xy=(max_year, max_total), 
            xytext=(max_year-2, max_total+50),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='darkred')

# Enhance plot aesthetics
plt.xticks(years, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()