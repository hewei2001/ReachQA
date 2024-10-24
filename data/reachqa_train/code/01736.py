import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = np.array([1990, 2000, 2010, 2020])

# Original data for renewable energy contribution in percentage
solar = np.array([0.5, 1.5, 5, 10])
wind = np.array([1, 2.5, 7, 15])
hydro = np.array([6, 8, 9, 10])
bioenergy = np.array([2, 3, 4, 5])

# Growth rate calculation (% increase each decade)
def calculate_growth_rate(data):
    return (data[1:] - data[:-1]) / data[:-1] * 100

solar_growth = calculate_growth_rate(solar)
wind_growth = calculate_growth_rate(wind)
hydro_growth = calculate_growth_rate(hydro)
bioenergy_growth = calculate_growth_rate(bioenergy)

# Creating a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Subplot 1: Stacked area chart
ax1.stackplot(decades, solar, wind, hydro, bioenergy, labels=['Solar', 'Wind', 'Hydro', 'Bioenergy'],
              colors=['#FFD700', '#1E90FF', '#32CD32', '#8B4513'], alpha=0.8)
ax1.set_title('Global Shift Towards Renewable Energy:\nContributions to Energy Mix (1990-2020)', fontsize=13, fontweight='bold')
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Percentage of Global Energy Mix', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('#f0f8ff')
ax1.set_xticks(decades)
ax1.set_xticklabels([str(year) for year in decades], rotation=45)
ax1.set_yticks(np.arange(0, 31, 5))
for i, year in enumerate(decades):
    ax1.text(year, np.sum([solar[i], wind[i], hydro[i], bioenergy[i]]) + 1, f"{int(np.sum([solar[i], wind[i], hydro[i], bioenergy[i]]))}%",
             fontsize=10, ha='center', va='bottom', fontweight='bold')
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Subplot 2: Line plot of growth rates
ax2.plot(decades[1:], solar_growth, marker='o', label='Solar', color='#FFD700', linestyle='--')
ax2.plot(decades[1:], wind_growth, marker='o', label='Wind', color='#1E90FF', linestyle='--')
ax2.plot(decades[1:], hydro_growth, marker='o', label='Hydro', color='#32CD32', linestyle='--')
ax2.plot(decades[1:], bioenergy_growth, marker='o', label='Bioenergy', color='#8B4513', linestyle='--')
ax2.set_title('Growth Rate of Renewable Energy Sources\n(1990-2020)', fontsize=13, fontweight='bold')
ax2.set_xlabel('Decade', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_facecolor('#f0f8ff')
ax2.set_xticks(decades[1:])
ax2.set_xticklabels([str(year) for year in decades[1:]], rotation=45)
ax2.set_yticks(np.arange(0, 401, 100))
ax2.legend(loc='upper left')

# Adjust layout
plt.tight_layout()
plt.show()