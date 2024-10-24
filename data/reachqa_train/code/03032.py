import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2020, 2031)

# Create data for energy sources (in TWh)
solar_energy = np.array([5, 10, 18, 30, 50, 75, 100, 130, 165, 200, 240])
wind_energy = np.array([8, 12, 25, 35, 55, 80, 110, 150, 190, 230, 270])
hydro_energy = np.array([15, 15, 15, 18, 22, 30, 40, 55, 70, 85, 100])

# Calculate total renewable energy
total_renewable_energy = solar_energy + wind_energy + hydro_energy

# Calculate percentage growth year-over-year for total energy
percentage_growth = np.zeros(len(total_renewable_energy))
percentage_growth[1:] = ((total_renewable_energy[1:] - total_renewable_energy[:-1]) / total_renewable_energy[:-1]) * 100

# Set up a figure with two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(14, 8))

# Plotting the stacked bar chart on the first subplot
axes[0].bar(years, solar_energy, label='Solar Energy', color='#ffa726', alpha=0.9)
axes[0].bar(years, wind_energy, bottom=solar_energy, label='Wind Energy', color='#42a5f5', alpha=0.9)
axes[0].bar(years, hydro_energy, bottom=solar_energy + wind_energy, label='Hydro Energy', color='#66bb6a', alpha=0.9)

# Customize the first plot
axes[0].set_title('The Rise of Renewable Energy\nin Countryland (2020-2030)', fontsize=15, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Consumption (TWh)', fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45)
axes[0].set_ylim(0, 620)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].legend(loc='upper left', fontsize=11, title='Energy Types', title_fontsize='12')

# Add annotations to the first plot
for i, (s, w, h) in enumerate(zip(solar_energy, wind_energy, hydro_energy)):
    axes[0].text(years[i], s / 2, f'{s}', ha='center', va='center', color='black', fontsize=9)
    axes[0].text(years[i], s + w / 2, f'{w}', ha='center', va='center', color='black', fontsize=9)
    axes[0].text(years[i], s + w + h / 2, f'{h}', ha='center', va='center', color='black', fontsize=9)

# Plotting the line chart on the second subplot
axes[1].plot(years, total_renewable_energy, label='Total Renewable Energy', color='purple', marker='o', linewidth=2)
axes[1].plot(years, percentage_growth, label='Year-over-Year Growth (%)', color='red', linestyle='--', marker='x', linewidth=1)

# Customize the second plot
axes[1].set_title('Total Renewable Energy & Growth', fontsize=15, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('TWh / Growth (%)', fontsize=12)
axes[1].set_xticks(years)
axes[1].set_xticklabels(years, rotation=45)
axes[1].set_ylim(0, max(total_renewable_energy) * 1.2)
axes[1].legend(loc='upper left', fontsize=11)
axes[1].grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()