import matplotlib.pyplot as plt
import numpy as np

# Define the months and apparent magnitude data for each celestial object
months = np.arange(1, 13)
variable_star_magnitude = [6.0, 5.8, 5.5, 5.7, 5.3, 5.6, 5.4, 5.2, 5.5, 5.7, 5.8, 6.0]
comet_magnitude = [9.5, 8.8, 7.5, 6.0, 5.5, 5.7, 6.8, 7.5, 8.0, 8.7, 9.0, 9.5]
galaxy_magnitude = [10.0, 10.1, 10.0, 10.2, 10.0, 10.1, 10.0, 10.3, 10.1, 10.0, 10.1, 10.0]

# Set up the plot
plt.figure(figsize=(14, 8))

# Plot data for each celestial object with different styles
plt.plot(months, variable_star_magnitude, color='gold', marker='o', linestyle='-', linewidth=2, label='Variable Star')
plt.plot(months, comet_magnitude, color='cyan', marker='v', linestyle='--', linewidth=2, label='Comet')
plt.plot(months, galaxy_magnitude, color='magenta', marker='s', linestyle='-.', linewidth=2, label='Galaxy')

# Add titles and labels
plt.title("Tracking Luminosity:\nA Year of Observations from Stellar Horizons", fontsize=16, fontweight='bold')
plt.xlabel("Month of Observation", fontsize=14)
plt.ylabel("Apparent Magnitude (lower is brighter)", fontsize=14)
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=12)
plt.yticks(fontsize=12)

# Add a grid and legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Celestial Objects', fontsize=12, loc='upper right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()