import matplotlib.pyplot as plt
import numpy as np

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

# Colors for each energy source
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(decades, data, labels=['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal'], colors=colors, alpha=0.8)

# Add axis labels and title
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Energy Production (TWh)', fontsize=12)
plt.title('The Growth of Renewable Energy Sources\nOver Recent Decades', fontsize=16, fontweight='bold', pad=20)

# Add a legend to identify the layers
plt.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Rotate x-tick labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()