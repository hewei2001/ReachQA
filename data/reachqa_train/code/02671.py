import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Energy output data for different sources (in Gigawatt-hours, GWh)
solar_energy = np.array([30, 35, 50, 70, 90, 110, 120, 115, 85, 60, 45, 35])
wind_energy = np.array([40, 45, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50])
hydro_energy = np.array([50, 50, 55, 60, 65, 70, 70, 65, 60, 55, 50, 50])
geothermal_energy = np.array([20, 22, 25, 28, 30, 33, 35, 34, 31, 29, 25, 23])

# Set up the figure
plt.figure(figsize=(12, 7))

# Plot the stacked area chart
plt.stackplot(months, solar_energy, wind_energy, hydro_energy, geothermal_energy, 
              labels=['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Geothermal Energy'],
              colors=['#FFD700', '#00BFFF', '#32CD32', '#8B4513'], alpha=0.8)

# Adding title and labels
plt.title("Renewable Energy Output Breakdown\nThroughout the Year", fontsize=14, weight='bold', pad=20)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Energy Output (GWh)", fontsize=12)

# Adjust x-ticks to improve readability
plt.xticks(rotation=45)

# Gridlines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Use tight layout to handle label and legend spacing
plt.tight_layout()

# Show the plot
plt.show()