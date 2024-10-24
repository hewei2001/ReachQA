import matplotlib.pyplot as plt
import numpy as np

# Residential zones and months
zones = ['Zone A', 'Zone B', 'Zone C', 'Zone D', 'Zone E', 'Zone F']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Energy consumption data in kilowatt-hours (kWh)
energy_consumption = np.array([
    [320, 310, 290, 280, 250, 245, 260, 270, 300, 320, 340, 330],
    [210, 200, 190, 180, 170, 165, 175, 185, 200, 210, 220, 215],
    [450, 440, 430, 420, 410, 405, 410, 420, 440, 450, 460, 455],
    [370, 360, 355, 345, 335, 330, 340, 350, 360, 370, 380, 375],
    [400, 395, 390, 380, 370, 365, 370, 380, 395, 400, 410, 405],
    [280, 270, 265, 260, 255, 250, 255, 260, 270, 280, 290, 285],
])

# Plotting the heat map
plt.figure(figsize=(12, 8))
heatmap = plt.imshow(energy_consumption, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Adding title and axis labels
plt.title('Eco-Impact Footprints:\nEnergy Consumption in Urban Residential Areas', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Residential Zones', fontsize=12)

# Adding ticks and labels
plt.xticks(ticks=np.arange(len(months)), labels=months, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(zones)), labels=zones)

# Adding a color bar for scale
cbar = plt.colorbar(heatmap)
cbar.set_label('Energy Consumption (kWh)', fontsize=12)

# Annotating the heat map with values
for i in range(len(zones)):
    for j in range(len(months)):
        plt.text(j, i, f'{energy_consumption[i, j]}', ha='center', va='center', color='black', fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()