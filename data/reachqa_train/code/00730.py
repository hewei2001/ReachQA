import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Energy production data (TWh)
wind_energy = np.array([150, 170, 190, 210, 250, 275, 300, 330, 370, 390, 420])
solar_energy = np.array([20, 30, 50, 70, 95, 130, 180, 220, 260, 300, 360])

# Errors in energy production
wind_error = np.array([15, 10, 12, 10, 13, 10, 11, 12, 10, 15, 12])
solar_error = np.array([5, 8, 7, 10, 12, 11, 10, 15, 10, 12, 10])

# Create the plot
plt.figure(figsize=(12, 7))

# Plot with error bars
plt.errorbar(years, wind_energy, yerr=wind_error, fmt='-o', 
             color='#1f77b4', ecolor='#A0C8E5', elinewidth=2, capsize=4, 
             label='Wind Energy')
plt.errorbar(years, solar_energy, yerr=solar_error, fmt='-s', 
             color='#ff7f0e', ecolor='#FFBB7E', elinewidth=2, capsize=4, 
             label='Solar Energy')

# Title and labels
plt.title("Trends in Renewable Energy Production (2010-2020):\nWind vs. Solar", 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Production (TWh)", fontsize=14)

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Legend
plt.legend(title='Type of Energy', fontsize=11, loc='upper left')

# Set x-ticks to display each year
plt.xticks(years)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()