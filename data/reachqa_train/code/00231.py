import matplotlib.pyplot as plt
import numpy as np

# Data for the x-axis: Years
years = np.arange(2010, 2020)

# Data for electricity generation in TWh for each energy source
coal = np.array([300, 290, 280, 260, 240, 220, 200, 180, 160, 140])
natural_gas = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
solar = np.array([10, 20, 30, 45, 60, 80, 100, 120, 150, 180])
wind = np.array([15, 25, 35, 50, 65, 85, 110, 135, 160, 190])
hydroelectric = np.array([50, 50, 50, 50, 50, 50, 50, 50, 50, 50])

# Stack the energy source data
energy_sources = np.vstack([coal, natural_gas, solar, wind, hydroelectric])

# Colors for the areas
colors = ['#444444', '#FFA07A', '#FFD700', '#7FFFD4', '#4682B4']

# Plot setup
fig, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(years, energy_sources, labels=['Coal', 'Natural Gas', 'Solar', 'Wind', 'Hydroelectric'], 
             colors=colors, alpha=0.8)

# Customization
ax.set_title('Electricity Generation Sources in Energilania\n(2010-2019)', fontsize=16, pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Electricity Generation (TWh)', fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 900)

# Add grid lines for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Rotate x-axis labels if needed
plt.xticks(years, rotation=45)

# Legend
ax.legend(loc='upper left', title='Energy Sources', fontsize=10)

# Add annotations for emphasis
ax.annotate('Rise in Solar and Wind', xy=(2017, 350), xytext=(2013, 500),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()