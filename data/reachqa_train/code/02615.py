import matplotlib.pyplot as plt
import numpy as np

# Define decades and renewable energy sources
decades = np.arange(1980, 2070, 10)
renewable_sources = ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass']

# Create data representing growth over time (units in GW)
solar = [0.5, 1, 4, 12, 50, 200, 500, 800, 1200]
wind = [1, 3, 10, 25, 80, 150, 300, 600, 1000]
hydroelectric = [200, 220, 250, 300, 340, 380, 420, 450, 480]
geothermal = [5, 6, 8, 10, 15, 20, 25, 30, 35]
biomass = [20, 25, 30, 35, 45, 55, 65, 75, 85]

# Stack data to represent the total renewable contribution over decades
data = np.vstack([solar, wind, hydroelectric, geothermal, biomass])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(decades, data, labels=renewable_sources, 
             colors=['#FFD700', '#87CEEB', '#008000', '#DAA520', '#A52A2A'], alpha=0.8)

# Add a title and labels with an engaging description
ax.set_title("Evolution of Renewable Energy Sources\n1980 - 2060", fontsize=16, pad=20)
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Energy Output (Gigawatts)", fontsize=12)

# Enhance the plot with a legend outside the plot area
ax.legend(loc='upper left', title="Renewable Sources", fontsize=10, bbox_to_anchor=(1.05, 1))

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Rotate x-axis labels for better clarity
plt.xticks(rotation=45)

# Adjust the layout for a tidy presentation
plt.tight_layout()

# Display the chart
plt.show()