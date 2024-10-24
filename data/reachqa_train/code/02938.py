import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2020, 2031)

# Define the percentage contributions from each renewable source over the years
solar_energy = np.array([5, 7, 10, 13, 17, 21, 25, 30, 35, 40, 45])
wind_energy = np.array([10, 12, 14, 17, 20, 24, 27, 30, 33, 35, 37])
hydroelectric_energy = np.array([15, 15, 16, 16, 17, 18, 19, 20, 21, 22, 22])
geothermal_energy = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Calculate the total renewable energy contribution
total_energy = solar_energy + wind_energy + hydroelectric_energy + geothermal_energy

# Create a figure and axis for plotting
plt.figure(figsize=(12, 8))

# Plot the stacked area chart
plt.stackplot(years, solar_energy, wind_energy, hydroelectric_energy, geothermal_energy,
              labels=['Solar', 'Wind', 'Hydroelectric', 'Geothermal'],
              colors=['#ffcc00', '#6699ff', '#66cc99', '#cc6600'],
              alpha=0.85)

# Overlay a line plot for the total renewable energy
plt.plot(years, total_energy, label='Total Renewable', color='black', linestyle='--', marker='o')

# Add plot titles and labels
plt.title("Rise of Renewable Energy\nHistorical and Forecasted Progress in Urban Areas (2020-2030)", 
          fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Percentage of Total Energy Consumption", fontsize=12)

# Customize ticks and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=10, frameon=True)

# Add annotations to highlight significant points
plt.annotate('Major policy shifts', xy=(2023, 60), xytext=(2020.5, 75),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, color='black')
plt.annotate('Technology breakthroughs', xy=(2027, 90), xytext=(2024, 95),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=10, color='black')

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()