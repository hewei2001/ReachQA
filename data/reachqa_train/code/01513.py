import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional data representing the number of registered eco-friendly vehicles
electric_cars = np.array([500, 700, 900, 1200, 1500, 1900, 2400, 3000, 3700, 4500, 5400])
hybrid_cars = np.array([1000, 1300, 1700, 2100, 2500, 2900, 3400, 4000, 4700, 5500, 6500])
bicycles = np.array([3000, 3200, 3400, 3700, 4000, 4300, 4600, 5000, 5400, 5900, 6400])
scooters = np.array([200, 250, 300, 400, 600, 900, 1300, 1800, 2400, 3100, 3900])

# Stack the data for the area chart
transport_data = np.vstack([electric_cars, hybrid_cars, bicycles, scooters])

fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, transport_data, labels=['Electric Cars', 'Hybrid Cars', 'Bicycles', 'Scooters'], 
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd'], alpha=0.8)

# Set labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Registered Vehicles', fontsize=14)
ax.set_title("Eco-Friendly Transportation Adoption in Greenfield\n2010-2020", fontsize=18, fontweight='bold')

# Customize the x-axis to show every year
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Adding grid lines for better readability
ax.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey', alpha=0.7)

# Add legend outside of plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Transportation Mode')

# Annotate significant developments
ax.annotate('Scooter Boom', xy=(2018, 18000), xytext=(2016, 20000),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Adjust layout to ensure proper spacing
plt.tight_layout()

# Display the plot
plt.show()