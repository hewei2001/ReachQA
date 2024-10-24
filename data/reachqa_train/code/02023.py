import matplotlib.pyplot as plt
import numpy as np

# Define months and product lines
months = np.array(['Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 
                   'Jul 2022', 'Aug 2022', 'Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022', 
                   'Jan 2023', 'Feb 2023', 'Mar 2023', 'Apr 2023', 'May 2023', 'Jun 2023', 
                   'Jul 2023', 'Aug 2023', 'Sep 2023', 'Oct 2023', 'Nov 2023', 'Dec 2023'])

# Revenue data in thousands
solar_panels = [50, 55, 60, 70, 80, 85, 95, 105, 120, 130, 125, 140,
                150, 160, 170, 180, 190, 200, 210, 220, 230, 250, 260, 275]
wind_turbines = [30, 35, 45, 50, 60, 65, 70, 75, 80, 85, 90, 100,
                 110, 115, 120, 125, 130, 135, 140, 145, 155, 165, 170, 180]
energy_storage = [20, 25, 30, 35, 40, 45, 55, 60, 65, 75, 85, 90,
                  95, 105, 110, 115, 125, 135, 140, 150, 160, 165, 175, 185]

# Create plot
plt.figure(figsize=(14, 8))
plt.plot(months, solar_panels, marker='o', linestyle='-', linewidth=2, label='Solar Panels', color='orange')
plt.plot(months, wind_turbines, marker='s', linestyle='--', linewidth=2, label='Wind Turbines', color='blue')
plt.plot(months, energy_storage, marker='^', linestyle=':', linewidth=2, label='Energy Storage', color='green')

# Annotate key milestones
milestones = {
    'Mar 2022': 'Solar Panel Upgrade',
    'Jun 2023': 'Wind Turbine Efficiency Boost',
    'Oct 2022': 'New Storage System'
}

for month, event in milestones.items():
    idx = months.tolist().index(month)
    plt.annotate(event, 
                 xy=(month, solar_panels[idx] if event == 'Solar Panel Upgrade' else 
                     wind_turbines[idx] if event == 'Wind Turbine Efficiency Boost' else 
                     energy_storage[idx]), 
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, color='red', 
                 arrowprops=dict(arrowstyle='->', lw=0.5))

# Customize plot
plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, 300, 20))
plt.xlabel('Month')
plt.ylabel('Revenue (in Thousands USD)')
plt.title('EcoTech Innovations:\nMonthly Revenue Growth by Product Line (2022-2023)')
plt.legend(title='Product Lines')

# Adjust layout and grid
plt.tight_layout()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show plot
plt.show()