import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional discovery data in number of discoveries
stars_discovered = np.array([20, 50, 90, 150, 220, 310, 420, 560, 720, 920, 1150])
exoplanets_discovered = np.array([10, 25, 55, 95, 140, 190, 250, 330, 420, 520, 630])
galaxies_discovered = np.array([5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330])
cosmic_phenomena = np.array([2, 5, 12, 20, 30, 45, 63, 85, 110, 140, 175])

# Stack the data for the area chart
discovery_data = np.vstack([stars_discovered, exoplanets_discovered, galaxies_discovered, cosmic_phenomena])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, discovery_data, labels=['Stars', 'Exoplanets', 'Galaxies', 'Cosmic Phenomena'], 
              colors=['#ffcc99', '#99ccff', '#ff9999', '#ccccff'], alpha=0.8)

# Set the labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Discoveries', fontsize=14)
ax.set_title("A Decade of Celestial Discoveries\nVisualizing the Unseen Universe", fontsize=18, fontweight='bold')

# Customize the x-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add a grid for better readability
ax.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax.minorticks_on()
ax.grid(visible=True, which='minor', linestyle=':', linewidth=0.5, color='grey', alpha=0.5)

# Add legend
ax.legend(loc='upper left', title='Celestial Objects')

# Annotate significant data points
ax.annotate('Exoplanet Exploration Boom', xy=(2016, 250), xytext=(2013, 400),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()