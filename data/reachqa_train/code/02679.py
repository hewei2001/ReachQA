import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data set
years = np.arange(2010, 2021)

# Energy consumption in TWh for each energy source
fossil_fuels = np.array([120, 115, 110, 105, 95, 85, 75, 65, 55, 45, 40])
solar = np.array([5, 10, 18, 30, 45, 60, 80, 100, 120, 140, 160])
wind = np.array([15, 25, 35, 45, 55, 65, 80, 90, 105, 115, 130])
hydro = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

# Colors for the area segments
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a stacked area plot
plt.figure(figsize=(14, 8))
plt.stackplot(years, fossil_fuels, solar, wind, hydro, labels=['Fossil Fuels', 'Solar', 'Wind', 'Hydro'], colors=colors, alpha=0.8)

# Add titles and labels
plt.title("EcoLand's Energy Consumption Evolution\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Consumption (TWh)', fontsize=14)

# Customizing the x-axis labels for better readability
plt.xticks(years, rotation=45)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(loc='upper right', fontsize=12, title='Energy Sources')

# Annotating significant milestones
plt.annotate('Fossil Fuels Drop', xy=(2017, 65), xytext=(2015, 100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()