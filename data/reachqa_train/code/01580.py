import matplotlib.pyplot as plt
import numpy as np

# Planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Average temperatures in degrees Celsius (approximate values)
temperatures = np.array([
    [430, 465, 440, 420, 430, 460, 430, 440],    # Mercury (varies drastically)
    [462, 462, 462, 462, 462, 462, 462, 462],    # Venus (constant high temperature)
    [15, 16, 14, 15, 14, 13, 15, 15],            # Earth (seasonal variation)
    [-55, -60, -58, -56, -57, -59, -60, -58],    # Mars (cold and dry)
    [-108, -108, -110, -107, -108, -106, -108, -109],  # Jupiter
    [-139, -140, -138, -137, -138, -139, -140, -138],  # Saturn
    [-195, -198, -197, -196, -195, -194, -195, -196],  # Uranus
    [-201, -202, -200, -199, -198, -199, -200, -201]   # Neptune
])

# Transpose the data for better orientation in the heat map
temperatures = np.transpose(temperatures)

# Create the heat map
plt.figure(figsize=(12, 6))
heatmap = plt.imshow(temperatures, cmap='coolwarm', aspect='auto', interpolation='nearest')

# Add a color bar with label
cbar = plt.colorbar(heatmap)
cbar.set_label('Average Temperature (°C)', rotation=270, labelpad=15)

# Set x and y ticks with planet names
plt.xticks(ticks=np.arange(len(planets)), labels=planets, rotation=45, ha='right', fontsize=10)
plt.yticks(ticks=np.arange(len(planets)), labels=planets, fontsize=10)

# Add labels and title
plt.xlabel('Planet', fontsize=12)
plt.ylabel('Planet', fontsize=12)
plt.title('Solar System Temperature Variations', fontsize=16, pad=20)

# Annotate each cell with the temperature value
for i in range(temperatures.shape[0]):
    for j in range(temperatures.shape[1]):
        plt.text(j, i, f'{temperatures[i, j]}°C', ha='center', va='center', color='black', fontsize=9)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()