import matplotlib.pyplot as plt
import numpy as np

# Expanded list of household appliances with subcategories
appliances = [
    'Refrigerator (Model A)', 'Refrigerator (Model B)', 
    'Washing Machine (Top Load)', 'Washing Machine (Front Load)', 
    'Dryer (Standard)', 'Dryer (High Efficiency)', 
    'Dishwasher (Compact)', 'Dishwasher (Standard)',
    'Microwave', 'Electric Oven', 'Air Conditioner (Window)', 
    'Air Conditioner (Split)', 'Television (LCD)', 'Television (LED)'
]

# Corresponding energy consumption in kWh per year
energy_consumption = [
    350, 450, 180, 220, 400, 550, 200, 300, 
    120, 100, 800, 1000, 150, 130
]

# Calculate percentage of total consumption for each appliance
total_consumption = sum(energy_consumption)
percentage_consumption = [round((ec / total_consumption) * 100, 2) for ec in energy_consumption]

# Colors for each appliance
colors = [
    '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#1C1C1C', 
    '#2ECC71', '#3498DB', '#8E44AD', '#27AE60', '#F39C12', '#E74C3C', 
    '#D35400', '#7D3C98'
]

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bar chart
bars = ax.barh(appliances, energy_consumption, color=colors, edgecolor='black', height=0.6)

# Add annotations for kWh and percentage
for bar, consumption, percentage in zip(bars, energy_consumption, percentage_consumption):
    ax.text(consumption + 10, bar.get_y() + bar.get_height() / 2,
            f'{consumption} kWh ({percentage}%)', va='center', ha='left', fontsize=9, color='black')

# Labels and title
ax.set_xlabel('Annual Energy Consumption (kWh)', fontsize=12)
ax.set_ylabel('Appliance Type', fontsize=12)
ax.set_title('Household Appliance Energy Consumption\nComparison by Models and Types',
             fontsize=14, weight='bold', pad=15)

# Add grid for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Calculate and plot total energy line
ax.axvline(x=total_consumption / len(appliances), color='red', linestyle='--', linewidth=1, label='Average Consumption')

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()