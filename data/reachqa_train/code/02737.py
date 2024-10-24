import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2023 to 2123
years = np.arange(2023, 2124)

# Energy source data (in percentage of total energy consumption)
fossil_fuels = np.linspace(75, 5, len(years))
nuclear = np.linspace(10, 15, len(years))
solar = np.linspace(5, 50, len(years))
wind = np.linspace(10, 30, len(years))

# Stack the data for plotting
energy_sources = np.vstack([fossil_fuels, nuclear, solar, wind])

# Create the stacked area plot
plt.figure(figsize=(14, 7))
colors = ['#d95f02', '#7570b3', '#1b9e77', '#e7298a']  # Distinct colors for each energy source
labels = ['Fossil Fuels', 'Nuclear', 'Solar', 'Wind']

# Plot using stackplot
plt.stackplot(years, energy_sources, labels=labels, colors=colors)

# Add titles and labels
plt.title("Energy Transition in Metropolis 2123:\nEvolution of Energy Sources Over a Century", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (%)", fontsize=12)

# Add a legend and position it outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate significant transition points
plt.annotate('Solar becomes dominant', xy=(2080, solar[57]), xytext=(2080, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()