import matplotlib.pyplot as plt
import numpy as np

# Define expanded data for light intensity and multiple plant height datasets
light_intensity = np.linspace(100, 1000, 20)  # Increased number of data points
plant_height_species1 = np.array([15, 18, 23, 27, 33, 36, 35, 32, 31, 29, 27, 25, 24, 23, 22, 21, 20, 19, 18, 17])
plant_height_species2 = np.array([10, 15, 20, 25, 30, 33, 36, 38, 35, 34, 33, 32, 30, 28, 26, 24, 22, 20, 18, 16])

# Create subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# First subplot: Plant Height vs. Light Intensity for Species 1
ax[0].scatter(light_intensity, plant_height_species1, color='forestgreen', edgecolors='black', s=80, alpha=0.7, label='Species 1')
z1 = np.polyfit(light_intensity, plant_height_species1, 3)  # Fit cubic polynomial
p1 = np.poly1d(z1)
ax[0].plot(light_intensity, p1(light_intensity), "r--", label='Cubic Trend', linewidth=1.5)
ax[0].set_title('Impact of Light Intensity on Plant Growth\nSpecies 1', fontsize=12, fontweight='bold', pad=20)
ax[0].set_xlabel('Light Intensity (Lux)', fontsize=10)
ax[0].set_ylabel('Average Plant Height (cm)', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(title='Growth Pattern', loc='best')

# Second subplot: Plant Height vs. Light Intensity for Species 2
ax[1].scatter(light_intensity, plant_height_species2, color='royalblue', edgecolors='black', s=80, alpha=0.7, label='Species 2')
z2 = np.polyfit(light_intensity, plant_height_species2, 3)  # Fit cubic polynomial
p2 = np.poly1d(z2)
ax[1].plot(light_intensity, p2(light_intensity), "m--", label='Cubic Trend', linewidth=1.5)
ax[1].set_title('Impact of Light Intensity on Plant Growth\nSpecies 2', fontsize=12, fontweight='bold', pad=20)
ax[1].set_xlabel('Light Intensity (Lux)', fontsize=10)
ax[1].set_ylabel('Average Plant Height (cm)', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend(title='Growth Pattern', loc='best')

# Annotate significant changes or peaks
for i in range(0, len(light_intensity), 3):
    ax[0].text(light_intensity[i] + 10, plant_height_species1[i] + 1, f'{plant_height_species1[i]}cm', fontsize=8)
    ax[1].text(light_intensity[i] + 10, plant_height_species2[i] + 1, f'{plant_height_species2[i]}cm', fontsize=8)

# Automatic layout adjustment
plt.tight_layout()

# Display the plots
plt.show()