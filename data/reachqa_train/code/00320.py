import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2050, 2101)  # 51 years

# Generate complex data for energy consumption (in TWh) by energy source
# Exponential growth for solar energy
solar_energy = 80 * np.exp(0.03 * (years - 2050))

# Logistic growth for wind energy
wind_energy = 300 / (1 + np.exp(-0.05 * (years - 2075)))

# Polynomial growth for fusion energy
fusion_energy = 10 + 0.4 * (years - 2050)**2

# Sine wave pattern for biomass energy
biomass_energy = 50 + 20 * np.sin(0.2 * (years - 2050))

# Linear increase for hydro energy
hydro_energy = np.linspace(30, 80, len(years))

# Calculate cumulative data for stacked area chart
cumulative_data = np.vstack([solar_energy, wind_energy, fusion_energy, biomass_energy, hydro_energy])

# Create a figure and axis for the plot
plt.figure(figsize=(16, 10))

# Create the stacked area chart with transparency
plt.stackplot(years, cumulative_data, labels=['Solar', 'Wind', 'Fusion', 'Biomass', 'Hydro'],
              colors=['#FFD700', '#87CEEB', '#FF69B4', '#8A2BE2', '#32CD32'], alpha=0.85)

# Add title and labels with line breaks for clarity
plt.title("Energy Consumption Trends in NeoCity\n2050-2100", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Energy Consumption (TWh)", fontsize=14)

# Add a legend and position it outside the plot
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Energy Source')

# Add grid lines for better readability
plt.grid(alpha=0.3)

# Add annotations for notable years
plt.annotate('Fusion Breakthrough', xy=(2085, 300), xytext=(2070, 400),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.annotate('Biomass Fluctuation Peak', xy=(2063, 70), xytext=(2050, 110),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()