import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Define the decades for the x-axis
decades = ['1990s', '2000s', '2010s', '2020s']

# Define the energy production data for each source (in TWh)
solar = np.array([5, 20, 100, 250])
wind = np.array([10, 50, 200, 500])
hydroelectric = np.array([200, 250, 300, 350])
biomass = np.array([30, 60, 100, 150])
geothermal = np.array([15, 25, 40, 60])

# Data stack for the area plot
data = np.vstack([solar, wind, hydroelectric, biomass, geothermal])

# Colors for each energy source with higher contrast
colors = ['#d73027', '#fc8d59', '#fee08b', '#91bfdb', '#4575b4']

# Create the stacked area chart
plt.figure(figsize=(14, 9))
plt.stackplot(decades, data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal'], colors=colors, alpha=0.8)

# Add axis labels and title
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Energy Production (TWh)', fontsize=12)
plt.title('The Growth of Renewable Energy Sources\nOver Recent Decades', fontsize=16, fontweight='bold', pad=20)

# Add a legend to identify the layers
plt.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Rotate x-tick labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Add gridlines for better readability
plt.grid(visible=True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Custom y-axis ticks and minor ticks
plt.yticks(np.arange(0, 601, 100))
plt.gca().yaxis.set_minor_locator(MultipleLocator(50))
plt.grid(which='minor', linestyle=':', linewidth=0.5)

# Annotate significant growth points
plt.annotate('Solar Surge', xy=('2010s', 100), xytext=('2010s', 150),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='black')

# Highlight recent decade
plt.axvspan(2.5, 3.5, color='grey', alpha=0.1)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()