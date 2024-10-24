import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2024)

# Population data for each species over the years
lynx_population = [100, 120, 140, 165, 185, 210, 240, 270, 300, 330, 360]
wolf_population = [80, 90, 95, 105, 120, 115, 130, 145, 160, 170, 180]
bear_population = [50, 60, 75, 85, 95, 110, 125, 140, 155, 170, 185]

# Environmental data: Annual rainfall in millimeters
rainfall = [600, 550, 575, 610, 620, 650, 590, 680, 700, 690, 710]

# Create the main plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the population data for each species
ax1.plot(years, lynx_population, marker='o', linestyle='-', linewidth=2, color='green', label='Lynx')
ax1.plot(years, wolf_population, marker='s', linestyle='--', linewidth=2, color='blue', label='Wolf')
ax1.plot(years, bear_population, marker='^', linestyle='-.', linewidth=2, color='brown', label='Bear')

# Annotations for key milestones
ax1.annotate('Lynx Peak', xy=(2018, 240), xytext=(2016, 280),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Wolf Surge', xy=(2019, 130), xytext=(2017, 160),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax1.annotate('Bear Success', xy=(2022, 170), xytext=(2020, 190),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Data point labels
for (x, y) in zip(years, lynx_population):
    ax1.text(x, y + 10, f'{y}', ha='center', fontsize=9, color='green')
for (x, y) in zip(years, wolf_population):
    ax1.text(x, y - 15, f'{y}', ha='center', fontsize=9, color='blue')
for (x, y) in zip(years, bear_population):
    ax1.text(x, y + 10, f'{y}', ha='center', fontsize=9, color='brown')

# Set title and labels
ax1.set_title('Biodiversity and Climate Interplay in Mystic Forest (2013-2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Population Count', fontsize=12, color='black')

# Add a secondary y-axis for the environmental data
ax2 = ax1.twinx()
ax2.bar(years, rainfall, color='lightblue', alpha=0.3, width=0.6, label='Rainfall (mm)')
ax2.set_ylabel('Annual Rainfall (mm)', fontsize=12, color='lightblue')
ax2.set_ylim(0, 1000)

# Adjust axis limits and add grid to ax1
ax1.set_xlim(years.min(), years.max())
ax1.set_ylim(0, 400)
ax1.grid(True, linestyle='--', alpha=0.5)

# Add legends
ax1.legend(loc="upper left", fontsize=11, title="Species")
ax2.legend(loc="upper right", fontsize=11)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()