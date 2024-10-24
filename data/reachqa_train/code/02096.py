import matplotlib.pyplot as plt
import numpy as np

# Data for the stacked bar chart
continents = ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania']
solar_energy = [350, 500, 420, 150, 200, 100]
wind_energy = [400, 300, 600, 100, 150, 200]
hydroelectric_energy = [500, 700, 350, 450, 300, 150]
geothermal_energy = [50, 100, 70, 30, 40, 60]

# Initialize the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Bar positions
bar_width = 0.6
x_pos = np.arange(len(continents))

# Create stacked bars
ax.bar(x_pos, solar_energy, bar_width, label='Solar', color='#FFD700', edgecolor='black', alpha=0.9)
ax.bar(x_pos, wind_energy, bar_width, bottom=solar_energy, label='Wind', color='#87CEEB', edgecolor='black', alpha=0.8)
ax.bar(x_pos, hydroelectric_energy, bar_width, bottom=np.add(solar_energy, wind_energy), label='Hydroelectric', color='#3CB371', edgecolor='black', alpha=0.7)
ax.bar(x_pos, geothermal_energy, bar_width, bottom=np.add(np.add(solar_energy, wind_energy), hydroelectric_energy), label='Geothermal', color='#FFA07A', edgecolor='black', alpha=0.6)

# Set labels and title
ax.set_xlabel('Continent', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)
ax.set_title('Global Contributions to Renewable Energy:\nA Continent-Wise Breakdown', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(continents, fontsize=10, rotation=45, ha='right')

# Add legend
ax.legend(loc='upper left', title='Energy Type', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()