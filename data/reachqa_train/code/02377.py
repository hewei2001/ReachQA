import matplotlib.pyplot as plt
import numpy as np

# Define the decades and energy sources
decades = ['1960s', '1970s', '1980s', '1990s', '2000s']
energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Fossil Fuels']

# Data representing the percentage contribution of each energy source per decade
solar_data = [5, 10, 15, 20, 30]
wind_data = [2, 5, 10, 15, 20]
hydro_data = [10, 15, 20, 20, 20]
nuclear_data = [0, 10, 20, 25, 20]
fossil_fuels_data = [83, 60, 35, 20, 10]

# Compile data into a 2D array for plotting
data = np.array([solar_data, wind_data, hydro_data, nuclear_data, fossil_fuels_data])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for different energy sources
colors = ['#FFD700', '#00BFFF', '#32CD32', '#800080', '#A52A2A']

# Plot the data using stackplot
ax.stackplot(decades, data, labels=energy_sources, colors=colors, alpha=0.85)

# Set labels and a multi-line title for better readability
ax.set_xlabel('Decades', fontsize=12, weight='bold')
ax.set_ylabel('Percentage Contribution', fontsize=12, weight='bold')
ax.set_title('Energy Sources Evolution\nOver Decades in Solaris City', fontsize=16, weight='bold', pad=20)

# Add legend outside of the plot to avoid occlusion of data
ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10, title_fontsize='11')

# Enhance grid visibility
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()