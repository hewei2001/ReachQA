import matplotlib.pyplot as plt
import numpy as np

# Define the years and energy consumption data for each source
years = np.arange(1990, 2021, 10)
solar_energy = [20, 150, 400, 1000]  # Solar energy consumption in TWh
wind_energy = [50, 250, 600, 1200]   # Wind energy consumption in TWh
hydro_energy = [500, 550, 600, 650]  # Hydro energy consumption in TWh

# Stack the data for the area chart
data = np.vstack([solar_energy, wind_energy, hydro_energy])

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the area chart using fill_between for clarity and custom styling
ax.fill_between(years, data[0], color='#FFD700', alpha=0.7, label='Solar Energy')
ax.fill_between(years, data[0] + data[1], data[0], color='#87CEFA', alpha=0.7, label='Wind Energy')
ax.fill_between(years, data[0] + data[1] + data[2], data[0] + data[1], color='#2E8B57', alpha=0.7, label='Hydro Energy')

# Titles and labels
ax.set_title('Evolution of Renewable Energy Sources Usage Over Decades\n(1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=12)

# Set x-ticks to be more frequent for better readability
ax.set_xticks(np.arange(1990, 2021, 5))

# Add legend and grid
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate significant trends
ax.annotate('Rise in Solar Energy\nTechnology', xy=(2000, 200), xytext=(2005, 800),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkorange')
ax.annotate('Policy Boost\nfor Wind Energy', xy=(2010, 800), xytext=(2015, 1600),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='royalblue')

# Rotate x-ticks for better visibility
plt.xticks(rotation=45)

# Automatically adjust layout for clarity
plt.tight_layout()

# Display the plot
plt.show()