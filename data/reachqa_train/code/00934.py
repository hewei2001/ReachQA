import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional discovery data in number of discoveries
stars_discovered = np.array([20, 50, 90, 150, 220, 310, 420, 560, 720, 920, 1150])
exoplanets_discovered = np.array([10, 25, 55, 95, 140, 190, 250, 330, 420, 520, 630])
galaxies_discovered = np.array([5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330])
cosmic_phenomena = np.array([2, 5, 12, 20, 30, 45, 63, 85, 110, 140, 175])

# Calculate annual growth rates
growth_stars = np.diff(stars_discovered, prepend=stars_discovered[0])
growth_exoplanets = np.diff(exoplanets_discovered, prepend=exoplanets_discovered[0])
growth_galaxies = np.diff(galaxies_discovered, prepend=galaxies_discovered[0])
growth_cosmic = np.diff(cosmic_phenomena, prepend=cosmic_phenomena[0])

# Create the figure and axes for two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16, 8))

# Plot the stacked area chart on the first subplot
discovery_data = np.vstack([stars_discovered, exoplanets_discovered, galaxies_discovered, cosmic_phenomena])
ax1.stackplot(years, discovery_data, labels=['Stars', 'Exoplanets', 'Galaxies', 'Cosmic Phenomena'], 
              colors=['#ffcc99', '#99ccff', '#ff9999', '#ccccff'], alpha=0.8)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Discoveries', fontsize=12)
ax1.set_title("A Decade of Celestial Discoveries\nVisualizing the Unseen Universe", fontsize=16, fontweight='bold')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax1.legend(loc='upper left', title='Celestial Objects')
ax1.annotate('Exoplanet Exploration Boom', xy=(2016, 250), xytext=(2013, 400),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=11)

# Plot the line chart for growth rates on the second subplot
ax2.plot(years, growth_stars, label='Stars', marker='o', color='#ffcc99', linewidth=2)
ax2.plot(years, growth_exoplanets, label='Exoplanets', marker='s', color='#99ccff', linewidth=2)
ax2.plot(years, growth_galaxies, label='Galaxies', marker='^', color='#ff9999', linewidth=2)
ax2.plot(years, growth_cosmic, label='Cosmic Phenomena', marker='d', color='#ccccff', linewidth=2)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Annual Growth', fontsize=12)
ax2.set_title('Yearly Growth in Celestial Discoveries', fontsize=16, fontweight='bold')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, ha='right')
ax2.grid(visible=True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
ax2.legend(loc='upper left', title='Discovery Growth')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()