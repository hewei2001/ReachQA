import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2012, 2023)

# Fictional energy production data in TWh
solar_energy = np.array([15, 20, 28, 40, 60, 85, 115, 150, 190, 235, 290])
wind_energy = np.array([30, 45, 55, 75, 100, 130, 165, 205, 250, 310, 375])
hydro_energy = np.array([200, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines for each energy source
ax.plot(years, solar_energy, marker='o', linestyle='-', color='orange', linewidth=2, label='Solar Energy')
ax.plot(years, wind_energy, marker='^', linestyle='-', color='green', linewidth=2, label='Wind Energy')
ax.plot(years, hydro_energy, marker='s', linestyle='-', color='blue', linewidth=2, label='Hydroelectric Energy')

# Add titles and labels
ax.set_title('Technological Advancements in Renewable Energy\nGlobal Trends (2012-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Customize ticks and grid
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend with title
ax.legend(title='Energy Source', fontsize=11, loc='upper left')

# Annotations to highlight significant trends
ax.annotate('Rapid Solar Growth', xy=(2017, 60), xytext=(2014.5, 150),
            arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=11, color='darkorange')

ax.annotate('Consistent Hydro Increase', xy=(2019, 245), xytext=(2016, 255),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=11, color='navy')

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()