import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2012, 2023)

# Fictional energy production data in TWh
solar_energy = np.array([15, 20, 28, 40, 60, 85, 115, 150, 190, 235, 290])
wind_energy = np.array([30, 45, 55, 75, 100, 130, 165, 205, 250, 310, 375])
hydro_energy = np.array([200, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255])

# Calculate total energy and percentage share
total_energy = solar_energy + wind_energy + hydro_energy
solar_share = (solar_energy / total_energy) * 100
wind_share = (wind_energy / total_energy) * 100
hydro_share = (hydro_energy / total_energy) * 100

# Create the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Plot lines for each energy source in the first subplot
axes[0].plot(years, solar_energy, marker='o', linestyle='-', color='orange', linewidth=2, label='Solar Energy')
axes[0].plot(years, wind_energy, marker='^', linestyle='-', color='green', linewidth=2, label='Wind Energy')
axes[0].plot(years, hydro_energy, marker='s', linestyle='-', color='blue', linewidth=2, label='Hydroelectric Energy')
axes[0].set_title('Technological Advancements in Renewable Energy\nGlobal Trends (2012-2022)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Energy Production (TWh)', fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45)
axes[0].yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axes[0].legend(title='Energy Source', fontsize=11, loc='upper left')
axes[0].annotate('Rapid Solar Growth', xy=(2017, 60), xytext=(2014.5, 150),
                 arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=11, color='darkorange')
axes[0].annotate('Consistent Hydro Increase', xy=(2019, 245), xytext=(2016, 255),
                 arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=11, color='navy')

# Plot the percentage share as a bar plot in the second subplot
width = 0.25  # Width of the bars
x = np.arange(len(years))

axes[1].bar(x - width, solar_share, width, label='Solar Energy', color='orange', alpha=0.7)
axes[1].bar(x, wind_share, width, label='Wind Energy', color='green', alpha=0.7)
axes[1].bar(x + width, hydro_share, width, label='Hydroelectric Energy', color='blue', alpha=0.7)

axes[1].set_title('Percentage Share of Renewable Energy Sources', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Percentage Share (%)', fontsize=12)
axes[1].set_xticks(x)
axes[1].set_xticklabels(years, rotation=45)
axes[1].legend(title='Energy Source', fontsize=11, loc='upper right')
axes[1].set_ylim(0, 100)
axes[1].yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()