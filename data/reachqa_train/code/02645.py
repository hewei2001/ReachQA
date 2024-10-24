import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Define the years for the chart
years = np.arange(2010, 2021)

# Data representing the percentage contribution of each energy source
solar_power = np.array([1, 2, 3, 5, 7, 10, 12, 14, 18, 22, 25])
wind_power = np.array([3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 22])
hydro_power = np.array([15, 15, 16, 16, 17, 18, 19, 20, 21, 22, 22])
geothermal_power = np.array([2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7])

# Calculate total renewable energy contribution
total_renewable = solar_power + wind_power + hydro_power + geothermal_power

# Initialize the plot
plt.figure(figsize=(14, 9))

# Plotting the stacked area chart
plt.stackplot(years, solar_power, wind_power, hydro_power, geothermal_power,
              labels=['Solar Power', 'Wind Power', 'Hydroelectric Power', 'Geothermal Power'],
              colors=['#FDB813', '#00A4E4', '#4CAF50', '#F47D42'], alpha=0.7)

# Overlay line graph for total contribution
plt.plot(years, total_renewable, color='black', linewidth=2, label='Total Renewable Contribution')

# Adding title and labels
plt.title('Rising Green: A Decade of Renewable Energy Growth\nin Global Electricity Production (2010-2020)',
          fontsize=16, fontweight='bold', color='darkgreen')
plt.xlabel('Year', fontsize=12, color='navy')
plt.ylabel('Percentage of Total Electricity Production', fontsize=12, color='navy')

# Configure x-ticks and y-ticks for better readability
plt.xticks(years, rotation=45)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

# Adding a grid for better readability
plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Annotations for specific points
plt.annotate('Rise of Solar', xy=(2018, 18), xytext=(2015, 32),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='orange', horizontalalignment='right')

plt.annotate('Wind Power Peaks', xy=(2020, 19), xytext=(2016, 38),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='blue', horizontalalignment='right')

# Adding value labels for total renewable contribution
for i, (year, total) in enumerate(zip(years, total_renewable)):
    plt.text(year, total + 1, f'{total}%', fontsize=9, ha='center', color='black')

# Enhance legend styling
plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)

# Automatically adjust the layout for better fit and visibility
plt.tight_layout()

# Show the plot
plt.show()