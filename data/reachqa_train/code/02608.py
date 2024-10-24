import matplotlib.pyplot as plt
import numpy as np

# Original data for renewable energy sources
decades = np.arange(1980, 2030, 10)
solar_power = [5, 10, 40, 100, 250]
wind_power = [10, 20, 50, 150, 400]
hydro_power = [100, 110, 120, 130, 140]
geothermal_power = [15, 18, 25, 35, 50]

# Hypothetical total energy production (TWh) for comparison
total_energy = [500, 550, 600, 700, 850]

# Calculate total renewable energy
total_renewable = np.sum([solar_power, wind_power, hydro_power, geothermal_power], axis=0)

# Calculate the percentage of renewable energy
renewable_percentage = (total_renewable / total_energy) * 100

# Stacked data for the area chart
renewable_data = np.vstack([solar_power, wind_power, hydro_power, geothermal_power])

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the stacked area chart
ax1.stackplot(decades, renewable_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'],
              colors=['#ffd700', '#1e90ff', '#32cd32', '#ff6347'], alpha=0.8)

# Add title and axis labels
ax1.set_title('The Rise of Renewable Energy:\nGrowth in Power Generation and Market Share', 
              fontsize=16, fontweight='bold', ha='center')
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Power Generation (TWh)', fontsize=12)

# Setup secondary y-axis for the overlay line plot
ax2 = ax1.twinx()
ax2.plot(decades, renewable_percentage, color='purple', linestyle='--', marker='o', label='Renewable Share (%)')
ax2.set_ylabel('Renewable Share (%)', fontsize=12)

# Legends and annotation
ax1.legend(loc='upper left', title='Renewable Sources', fontsize=10, title_fontsize='13')
ax2.legend(loc='upper center', fontsize=10)

# Annotate the renewable percentage line for key insights
for decade, percent in zip(decades, renewable_percentage):
    ax2.annotate(f'{percent:.1f}%', xy=(decade, percent), textcoords='offset points', xytext=(10, -10), ha='center', fontsize=9, color='purple')

# Grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.5)
plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()