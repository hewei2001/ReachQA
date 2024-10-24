import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2000, 2021)

# Define energy contributions over the years in TWh
coal = [200, 195, 190, 185, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55]
natural_gas = [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240]
nuclear = [50, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
solar = [5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
wind = [10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 60, 70, 85, 100, 120, 140, 160, 180, 200, 220]

# Plotting the stacked area chart
plt.figure(figsize=(12, 8))

# Create stacked area plot
plt.stackplot(years, coal, natural_gas, nuclear, solar, wind, labels=['Coal', 'Natural Gas', 'Nuclear', 'Solar', 'Wind'], colors=['#a83232', '#eb8334', '#6e6ec2', '#f2e431', '#8cc13f'], alpha=0.8)

# Add title and labels
plt.title("Evolution of Energy Sources in Imaginaryland\nFrom Fossil Fuels to Renewables (2000 - 2020)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Contribution (TWh)", fontsize=12)

# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0., title='Energy Sources')

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Highlight a significant point of transition in the data
plt.annotate('Solar overtakes Nuclear', xy=(2018, 340), xytext=(2010, 450),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

# Ensure layout is neat without overlapping
plt.tight_layout()

# Display the plot
plt.show()