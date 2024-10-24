import matplotlib.pyplot as plt
import numpy as np

# Define the years and the energy generation data in TWh
years = np.arange(2010, 2021)
solar = [0.5, 0.8, 1.2, 2.5, 4.0, 6.0, 8.5, 10.0, 12.0, 14.5, 17.0]
wind = [2.0, 2.5, 3.5, 5.0, 7.5, 10.0, 13.0, 15.5, 17.5, 19.0, 20.5]
hydro = [4.0, 4.1, 4.3, 4.4, 4.5, 4.7, 4.8, 5.0, 5.2, 5.5, 5.7]
biomass = [1.0, 1.2, 1.5, 2.0, 2.8, 3.5, 4.0, 4.5, 4.7, 5.0, 5.3]

# Create an area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.fill_between(years, 0, solar, label='Solar', color='#FFD700', alpha=0.6)
ax.fill_between(years, solar, np.array(solar) + np.array(wind), label='Wind', color='#87CEEB', alpha=0.6)
ax.fill_between(years, np.array(solar) + np.array(wind), np.array(solar) + np.array(wind) + np.array(hydro), 
                label='Hydro', color='#4682B4', alpha=0.6)
ax.fill_between(years, np.array(solar) + np.array(wind) + np.array(hydro), 
                np.array(solar) + np.array(wind) + np.array(hydro) + np.array(biomass), 
                label='Biomass', color='#6B8E23', alpha=0.6)

# Customize the plot
ax.set_title("Renewable Energy Generation in Greenlandia (2010-2020)", fontsize=16, weight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Generation (TWh)", fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 50)

# Add grid lines
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(loc='upper left', fontsize=10, title='Energy Source', title_fontsize='13')

# Annotations for significant milestones
ax.annotate('Solar Energy Surge', xy=(2015, 5), xytext=(2015.5, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkorange')
ax.annotate('Wind Overtakes Hydro', xy=(2017, 15), xytext=(2017, 40),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Rotate x-axis labels if necessary
plt.xticks(rotation=45)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()