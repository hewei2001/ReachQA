import matplotlib.pyplot as plt
import numpy as np

# Defining decades
decades = ['1990', '2000', '2010']

# Production data for each component (in millions of units)
sensors = [20, 45, 70]
actuators = [15, 35, 55]
controllers = [10, 15, 20]
power_supplies = [5, 20, 40]

# Related data for line plot: Innovation Index
innovation_index = [10, 25, 50]

# Create figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Stack data for area chart
stacked_data = np.row_stack((sensors, actuators, controllers, power_supplies))
ax1.stackplot(decades, stacked_data, labels=['Sensors', 'Actuators', 'Controllers', 'Power Supplies'],
              colors=['#8e44ad', '#2980b9', '#27ae60', '#f39c12'], alpha=0.8)

# Customize the primary axis (area chart)
ax1.set_title("The Evolution of Robotics Components Production\nand Innovation Over the Decades", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Decade', fontsize=14)
ax1.set_ylabel('Production (Millions of Units)', fontsize=14)
ax1.legend(loc='upper left', fontsize=12, title='Component Type')
ax1.grid(linestyle='--', alpha=0.6, axis='y')

# Annotating the end value for each component at 2010
components = [sensors, actuators, controllers, power_supplies]
positions = [sensors[-1], actuators[-1] + sensors[-1], controllers[-1] + actuators[-1] + sensors[-1], 
             power_supplies[-1] + controllers[-1] + actuators[-1] + sensors[-1]]

for component, pos, label in zip(components, positions, ['Sensors', 'Actuators', 'Controllers', 'Power Supplies']):
    ax1.text(2, pos - 10, f'{label}: {component[-1]}M', fontsize=10, va='center', ha='center', color='white', fontweight='bold')

# Create secondary axis for the line plot
ax2 = ax1.twinx()
ax2.plot(decades, innovation_index, color='black', marker='o', linestyle='-', linewidth=2, markersize=8, label='Innovation Index')

# Customize the secondary axis (line plot)
ax2.set_ylabel('Innovation Index', fontsize=14, color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.legend(loc='upper right', fontsize=12, title='Innovation Metric')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()