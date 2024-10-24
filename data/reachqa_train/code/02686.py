import matplotlib.pyplot as plt
import numpy as np

# List of household appliances
appliances = [
    'Refrigerator', 'Washing Machine', 'Dryer', 'Dishwasher', 
    'Microwave', 'Electric Oven', 'Air Conditioner', 'Television'
]

# Corresponding energy consumption in kWh per year
energy_consumption = [400, 200, 500, 250, 120, 100, 900, 130]

# Bar colors for each appliance
colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', 
          '#581845', '#1C1C1C', '#2ECC71', '#3498DB']

# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(appliances, energy_consumption, color=colors, edgecolor='black', height=0.6)

# Add annotations to each bar
for bar, consumption in zip(bars, energy_consumption):
    plt.text(consumption + 10, bar.get_y() + bar.get_height() / 2,
             f'{consumption} kWh', va='center', ha='left', fontsize=9, color='black')

# Labels and title
plt.xlabel('Annual Energy Consumption (kWh)', fontsize=12)
plt.ylabel('Appliance Type', fontsize=12)
plt.title('Household Appliance Energy Consumption:\nUnderstanding Usage Patterns',
          fontsize=14, weight='bold', pad=15)

# Enhance readability with a grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()