import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Data for renewable energy adoption across continents (in exajoules)
solar_energy = {
    "North America": [0.1, 0.2, 0.3, 0.5, 0.7, 1.1, 1.4, 1.6, 2.0, 2.4, 2.9, 3.5, 4.0, 4.6, 5.1, 5.7, 6.3, 7.0, 7.8, 8.5, 9.3, 10.2, 11.0, 12.0, 13.0, 14.0, 15.2, 16.5, 17.9, 19.5, 21.0],
    "Europe": [0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.3, 1.7, 2.0, 2.5, 3.1, 3.8, 4.5, 5.3, 6.2, 7.2, 8.1, 9.1, 10.0, 11.2, 12.4, 13.7, 15.1, 16.5, 18.0, 19.6, 21.3, 23.1, 25.0, 27.0],
    "Asia": [0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.9, 1.2, 1.6, 2.0, 2.5, 3.1, 3.8, 4.6, 5.5, 6.5, 7.6, 8.7, 9.9, 11.2, 12.6, 14.1, 15.7, 17.4, 19.2, 21.1, 23.1, 25.2, 27.4, 29.7, 32.0],
    "Africa": [0.01, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 0.9, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.6, 5.4, 6.3, 7.3, 8.4, 9.6, 10.9, 12.3, 13.8, 15.4, 17.1, 18.9, 20.8],
    "South America": [0.02, 0.04, 0.07, 0.1, 0.15, 0.21, 0.28, 0.35, 0.43, 0.52, 0.62, 0.73, 0.85, 0.98, 1.12, 1.27, 1.43, 1.6, 1.78, 1.97, 2.17, 2.38, 2.6, 2.83, 3.07, 3.32, 3.58, 3.85, 4.13, 4.42, 4.72]
}

# Adjust colors for clarity
colors = ['#FFD700', '#FFA07A', '#20B2AA', '#87CEFA', '#FF69B4']

# Plot stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, 
             solar_energy['North America'], 
             solar_energy['Europe'], 
             solar_energy['Asia'], 
             solar_energy['Africa'], 
             solar_energy['South America'], 
             labels=solar_energy.keys(), 
             colors=colors, alpha=0.8)

# Titles and labels
ax.set_title('Evolution of Renewable Energy Adoption Across Continents\n1990-2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Solar Energy Consumption (Exajoules)', fontsize=14)

# Customize legend
ax.legend(loc='upper left', title='Continent', fontsize=12, title_fontsize=12, bbox_to_anchor=(1, 1))

# Grid lines for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Auto-adjust layout
plt.tight_layout()

# Display the plot
plt.show()