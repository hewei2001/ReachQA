import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional data representing the number of registered eco-friendly vehicles
electric_cars = np.array([500, 700, 900, 1200, 1500, 1900, 2400, 3000, 3700, 4500, 5400])
hybrid_cars = np.array([1000, 1300, 1700, 2100, 2500, 2900, 3400, 4000, 4700, 5500, 6500])
bicycles = np.array([3000, 3200, 3400, 3700, 4000, 4300, 4600, 5000, 5400, 5900, 6400])
scooters = np.array([200, 250, 300, 400, 600, 900, 1300, 1800, 2400, 3100, 3900])

# Total number of eco-friendly vehicles each year
total_vehicles = electric_cars + hybrid_cars + bicycles + scooters

# Hypothetical data: percentage of eco-friendly vehicles compared to total vehicles
# Assuming a hypothetical steady total vehicle growth from 20000 to 80000 over 2010-2020
total_vehicle_market = np.linspace(20000, 80000, len(years))
percentage_eco_friendly = (total_vehicles / total_vehicle_market) * 100

# Stack the data for the area chart
transport_data = np.vstack([electric_cars, hybrid_cars, bicycles, scooters])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax1.stackplot(years, transport_data, labels=['Electric Cars', 'Hybrid Cars', 'Bicycles', 'Scooters'], 
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd'], alpha=0.8)

# Twin the x-axis for the overlay line plot
ax2 = ax1.twinx()

# Plot the line for the percentage of eco-friendly vehicles
ax2.plot(years, percentage_eco_friendly, color='black', linewidth=2, linestyle='--', marker='o', label='Percentage of Eco-Friendly Vehicles (%)')

# Label the axes
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Registered Vehicles', fontsize=14)
ax2.set_ylabel('Percentage of Eco-Friendly Vehicles (%)', fontsize=14)

# Add a title with multiple lines for clarity
ax1.set_title("Eco-Friendly Transportation Adoption in Greenfield (2010-2020)\nTotal and Percentage of Eco-Friendly Vehicles", fontsize=18, fontweight='bold')

# Customize the x-axis to show every year
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Adding grid lines for better readability
ax1.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add legends for both plots
stacked_legend = ax1.legend(loc='upper left', bbox_to_anchor=(1, 0.7), title='Transportation Mode')
line_legend = ax2.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Market Penetration')

# Ensure legends do not overlap
ax1.add_artist(stacked_legend)

# Annotate significant developments
ax1.annotate('Scooter Boom', xy=(2018, scooters[-1]), xytext=(2015, 15000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Adjust layout to ensure proper spacing
plt.tight_layout()

# Display the plot
plt.show()