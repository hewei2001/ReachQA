import matplotlib.pyplot as plt
import numpy as np

# Define the types of smart devices and the years
devices = ["Smart Lights", "Smart Thermostats", "Smart Security", "Smart Appliances"]
years = np.arange(2010, 2021)

# Define the artificial data for each smart device adoption rate
adoption_lights = [2, 4, 7, 10, 14, 20, 28, 38, 50, 65, 80]
adoption_thermostats = [1, 3, 5, 8, 12, 18, 25, 33, 44, 58, 73]
adoption_security = [1, 2, 4, 6, 9, 14, 21, 29, 38, 50, 65]
adoption_appliances = [0, 1, 2, 4, 7, 12, 18, 26, 35, 47, 60]

# Create the plot
plt.figure(figsize=(12, 7))

# Plot the stacked area chart
plt.stackplot(years, adoption_lights, adoption_thermostats, adoption_security, adoption_appliances,
              labels=devices,
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'], alpha=0.8)

# Add title and labels
plt.title("Evolution of Household Smart Technology Adoption (2010-2020)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Adoption Rate (%)", fontsize=12)
plt.xlim(years[0], years[-1])
plt.xticks(years, rotation=45)
plt.legend(loc='upper left', fontsize=10, title='Smart Devices')

# Add grid for better readability
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()