import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Define adoption rates for different energy sources as percentages
solar_adoption = [2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40]  # Rapid increase due to tech advancements
wind_adoption = [10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30]  # Steady growth due to policy support
hydro_adoption = [30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36]  # Slight increase as it's more established

# Create the line chart
plt.figure(figsize=(12, 6))

# Plot each energy source with distinct line styles and markers
plt.plot(years, solar_adoption, label='Solar Energy', color='gold', linestyle='--', marker='o', linewidth=2)
plt.plot(years, wind_adoption, label='Wind Energy', color='skyblue', linestyle='-', marker='s', linewidth=2)
plt.plot(years, hydro_adoption, label='Hydropower', color='lightgreen', linestyle='-.', marker='^', linewidth=2)

# Title and labels
plt.title('The Evolution of Renewable Energy Adoption\nin EcoLand (2010-2020)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (% of Total Energy Consumption)', fontsize=12)

# Legend to differentiate the lines
plt.legend(title="Energy Source", loc='upper left', fontsize=10)

# Add grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Highlight major milestones or trends
plt.annotate('Solar Boost\nInnovations', xy=(2015, 14), xytext=(2013, 25),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.annotate('Steady Wind\nPolicy Support', xy=(2017, 24), xytext=(2015, 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

# Ensure the layout is optimized for readability
plt.tight_layout()

# Show the plot
plt.show()