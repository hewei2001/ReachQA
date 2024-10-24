import matplotlib.pyplot as plt
import numpy as np

# Defining decades
decades = ['1990', '2000', '2010']

# Production data for each component (in millions of units)
sensors = [20, 45, 70]
actuators = [15, 35, 55]
controllers = [10, 15, 20]
power_supplies = [5, 20, 40]

# Plotting an area chart
fig, ax = plt.subplots(figsize=(12, 8))

# Stack data for area chart
stacked_data = np.row_stack((sensors, actuators, controllers, power_supplies))
ax.stackplot(decades, stacked_data, labels=['Sensors', 'Actuators', 'Controllers', 'Power Supplies'],
             colors=['#8e44ad', '#2980b9', '#27ae60', '#f39c12'], alpha=0.8)

# Customize the plot
ax.set_title("The Evolution of Robotics Components Production\nOver the Decades", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Production (Millions of Units)', fontsize=14)
ax.legend(loc='upper left', fontsize=12, title='Component Type')
ax.grid(linestyle='--', alpha=0.6, axis='y')

# Annotating the end value for each component at 2010
components = [sensors, actuators, controllers, power_supplies]
positions = [sensors[-1], actuators[-1] + sensors[-1], controllers[-1] + actuators[-1] + sensors[-1], 
             power_supplies[-1] + controllers[-1] + actuators[-1] + sensors[-1]]

for component, pos, label in zip(components, positions, ['Sensors', 'Actuators', 'Controllers', 'Power Supplies']):
    ax.text(2, pos - 10, f'{label}: {component[-1]}M', fontsize=10, va='center', ha='center', color='white', fontweight='bold')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()