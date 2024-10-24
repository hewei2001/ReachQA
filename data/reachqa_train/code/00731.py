import matplotlib.pyplot as plt
import numpy as np

# Define extended years
years = np.arange(2010, 2031)

# Extended energy production data (TWh)
wind_energy = np.array(
    [150, 170, 190, 210, 250, 275, 300, 330, 370, 390, 420, 450, 480, 510, 540, 580, 610, 640, 670, 700, 730]
)
solar_energy = np.array(
    [20, 30, 50, 70, 95, 130, 180, 220, 260, 300, 360, 380, 400, 420, 460, 500, 550, 600, 650, 700, 750]
)
hydro_energy = np.array(
    [350, 340, 330, 335, 340, 345, 355, 360, 370, 380, 390, 400, 410, 420, 430, 440, 455, 470, 480, 490, 500]
)
geothermal_energy = np.array(
    [30, 32, 33, 34, 35, 38, 39, 40, 42, 45, 47, 50, 52, 55, 57, 60, 62, 65, 67, 70, 73]
)

# Errors in energy production
wind_error = np.array([15, 10, 12, 10, 13, 10, 11, 12, 10, 15, 12, 10, 11, 13, 12, 15, 11, 14, 13, 12, 14])
solar_error = np.array([5, 8, 7, 10, 12, 11, 10, 15, 10, 12, 10, 9, 8, 10, 11, 12, 11, 10, 12, 11, 10])

# Create the plot
plt.figure(figsize=(14, 8))

# Plot with error bars
plt.errorbar(years, wind_energy, yerr=wind_error, fmt='-o', color='#1f77b4', ecolor='#A0C8E5', elinewidth=1.5, capsize=3, label='Wind Energy')
plt.errorbar(years, solar_energy, yerr=solar_error, fmt='-s', color='#ff7f0e', ecolor='#FFBB7E', elinewidth=1.5, capsize=3, label='Solar Energy')
plt.plot(years, hydro_energy, '-^', color='#2ca02c', label='Hydroelectric Energy')
plt.plot(years, geothermal_energy, '-d', color='#9467bd', label='Geothermal Energy')

# Cumulative sum and plot
cumulative_energy = wind_energy + solar_energy + hydro_energy + geothermal_energy
plt.plot(years, cumulative_energy, '--', color='grey', linewidth=2, label='Total Cumulative Energy Production')

# Adding a moving average line
moving_avg = np.convolve(wind_energy, np.ones(3)/3, mode='valid')
plt.plot(years[1:-1], moving_avg, ':', color='black', label='3-Year Moving Avg (Wind)')

# Title and labels
plt.title("Renewable Energy Production (2010-2030)\nA Comparative Analysis of Energy Sources", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Production (TWh)", fontsize=14)

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Legend
plt.legend(title='Type of Energy', fontsize=11, loc='upper left', bbox_to_anchor=(1, 1))

# Set x-ticks to display each year
plt.xticks(years)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()