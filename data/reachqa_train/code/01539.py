import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Define energy contributions over the years in TWh
coal = np.array([200, 195, 190, 185, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55])
natural_gas = np.array([120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240])
nuclear = np.array([50, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])
solar = np.array([5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
wind = np.array([10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100, 120, 140, 160, 180, 200, 220])

# Calculate total energy for secondary Y-axis
total_energy = coal + natural_gas + nuclear + solar + wind
renewable_energy = solar + wind
renewable_percentage = (renewable_energy / total_energy) * 100

plt.figure(figsize=(14, 9))

# Create stacked area plot with gradients
plt.stackplot(years, coal, natural_gas, nuclear, solar, wind,
              labels=['Coal', 'Natural Gas', 'Nuclear', 'Solar', 'Wind'],
              colors=['#a83232', '#eb8334', '#6e6ec2', '#f2e431', '#8cc13f'],
              alpha=0.9)

# Add title and labels
plt.title("Energy Source Evolution in Imaginaryland (2000 - 2020)\nTransition from Fossil Fuels to Renewables", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Contribution (TWh)", fontsize=12)

# Secondary Y-axis for renewable percentage
ax2 = plt.gca().twinx()
ax2.plot(years, renewable_percentage, 'k--', label='Renewable Percentage', linewidth=1.5)
ax2.set_ylabel("Renewable Percentage (%)", fontsize=12, color='gray')
ax2.tick_params(axis='y', colors='gray')

# Add legends with enhanced details
plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0., title='Energy Sources')
ax2.legend(loc='upper left', bbox_to_anchor=(1.02, 0.85))

# Annotate significant points
plt.annotate('Solar overtakes Nuclear', xy=(2018, 340), xytext=(2010, 450),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')
plt.annotate('Rapid Wind Growth', xy=(2017, 280), xytext=(2010, 380),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

# Add vertical lines for policy change periods
plt.axvline(x=2010, color='grey', linestyle='--', alpha=0.6, label='Policy Change')
plt.axvline(x=2015, color='grey', linestyle='--', alpha=0.6)

# Customize grid lines
plt.grid(linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()