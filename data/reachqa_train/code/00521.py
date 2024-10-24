import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy production data for each renewable energy source
years = np.arange(2010, 2021)

solar_energy = np.array([30, 40, 55, 70, 90, 120, 150, 180, 210, 250, 300])
wind_energy = np.array([50, 60, 65, 75, 85, 100, 110, 130, 140, 160, 180])
hydro_energy = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
bio_energy = np.array([20, 25, 30, 35, 40, 50, 55, 60, 65, 70, 75])

# Calculate total energy production for overlay
total_energy = solar_energy + wind_energy + hydro_energy + bio_energy

# Calculate year-on-year percentage growth
percentage_growth = np.append([0], np.diff(total_energy) / total_energy[:-1] * 100)

# Combine the data into a single array for stacked area plotting
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, bio_energy])

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax1.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
              colors=['#FFD700', '#87CEEB', '#8FBC8F', '#FF6347'])

# Adding primary title and labels
ax1.set_title('Annual Renewable Energy Production by Source\nand Percentage Growth in Emerald City (2010-2020)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (GWh)', fontsize=12)

# Add legend to the plot
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Add grid
ax1.grid(linestyle='--', linewidth=0.5, alpha=0.7)

# Create secondary y-axis for percentage growth overlay
ax2 = ax1.twinx()
ax2.plot(years, percentage_growth, 'k--', label='Percentage Growth', linewidth=2)
ax2.set_ylabel('Percentage Growth (%)', fontsize=12, color='black')

# Add annotations for notable percentage growth
for i, (year, growth) in enumerate(zip(years, percentage_growth)):
    if abs(growth) > 10:  # Annotate significant changes
        ax2.annotate(f'{growth:.1f}%', (year, growth),
                     textcoords="offset points", xytext=(-15,10), ha='center',
                     arrowprops=dict(arrowstyle='->', color='grey'), fontsize=9)

# Add legend for the line plot
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to fit all elements
fig.tight_layout()

# Display the plot
plt.show()