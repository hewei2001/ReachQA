import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2020, 2031)

# Create data for energy sources (in TWh)
solar_energy = np.array([5, 10, 18, 30, 50, 75, 100, 130, 165, 200, 240])
wind_energy = np.array([8, 12, 25, 35, 55, 80, 110, 150, 190, 230, 270])
hydro_energy = np.array([15, 15, 15, 18, 22, 30, 40, 55, 70, 85, 100])

# Plotting setup
plt.figure(figsize=(12, 8))

# Stacked bar chart
plt.bar(years, solar_energy, label='Solar Energy', color='#ffa726', alpha=0.9)
plt.bar(years, wind_energy, bottom=solar_energy, label='Wind Energy', color='#42a5f5', alpha=0.9)
plt.bar(years, hydro_energy, bottom=solar_energy + wind_energy, label='Hydro Energy', color='#66bb6a', alpha=0.9)

# Customize the plot
plt.title('The Rise of Renewable Energy Sources\nin Countryland (2020-2030)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Consumption (TWh)', fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 601, 50))
plt.ylim(0, 620)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=12, title='Energy Types', title_fontsize='13')

# Add annotations for clarity
for i, (s, w, h) in enumerate(zip(solar_energy, wind_energy, hydro_energy)):
    plt.text(years[i], s / 2, f'{s}', ha='center', va='center', color='black', fontsize=10)
    plt.text(years[i], s + w / 2, f'{w}', ha='center', va='center', color='black', fontsize=10)
    plt.text(years[i], s + w + h / 2, f'{h}', ha='center', va='center', color='black', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()