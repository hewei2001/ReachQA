import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2013, 2024)

# Population data for each species over the years
lynx_population = [100, 120, 140, 165, 185, 210, 240, 270, 300, 330, 360]
wolf_population = [80, 90, 95, 105, 120, 115, 130, 145, 160, 170, 180]
bear_population = [50, 60, 75, 85, 95, 110, 125, 140, 155, 170, 185]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data for each species
ax.plot(years, lynx_population, marker='o', linestyle='-', linewidth=2, color='green', label='Lynx')
ax.plot(years, wolf_population, marker='s', linestyle='--', linewidth=2, color='blue', label='Wolf')
ax.plot(years, bear_population, marker='^', linestyle='-.', linewidth=2, color='brown', label='Bear')

# Add annotations for key milestones
ax.annotate('Lynx Reintroduction Peak', xy=(2018, 240), xytext=(2016, 280),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Wolf Population Surge', xy=(2019, 130), xytext=(2017, 160),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Bear Breeding Success', xy=(2022, 170), xytext=(2020, 190),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Add data point labels
for (x, y) in zip(years, lynx_population):
    ax.text(x, y + 10, f'{y}', ha='center', fontsize=9, color='green')
for (x, y) in zip(years, wolf_population):
    ax.text(x, y - 15, f'{y}', ha='center', fontsize=9, color='blue')
for (x, y) in zip(years, bear_population):
    ax.text(x, y + 10, f'{y}', ha='center', fontsize=9, color='brown')

# Set title and labels
ax.set_title('Biodiversity Restoration in Mystic Forest:\nKey Species Population (2013-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population Count', fontsize=12)

# Adjust axis limits and add grid
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 400)
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(title="Species", loc="upper left", fontsize=11)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()