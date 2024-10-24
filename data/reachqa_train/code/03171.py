import matplotlib.pyplot as plt
import numpy as np

# Handcrafted data for different types of stars in the Andromeda Galaxy
red_giants = {
    "Brightness": [70, 68, 72, 75, 74, 69, 71, 73],
    "Distance": [2500, 2400, 2600, 2550, 2450, 2350, 2650, 2500]
}

white_dwarfs = {
    "Brightness": [20, 22, 19, 21, 23, 24, 18, 25],
    "Distance": [3000, 3100, 2950, 3200, 3050, 3250, 3150, 3050]
}

main_sequence_stars = {
    "Brightness": [40, 45, 42, 44, 41, 47, 43, 46],
    "Distance": [4000, 3900, 4100, 4050, 3950, 4150, 4250, 4050]
}

# Additional Data for a new subplot - Star Color Index vs. Temperature
star_types = ['Red Giants', 'White Dwarfs', 'Main Sequence Stars']
average_temperatures = [3500, 10000, 5500]  # in Kelvin
color_indices = [1.5, 0.2, 0.65]  # arbitrary color index

# Create a figure with 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Brightness vs. Distance Scatter Plot
axs[0].scatter(red_giants["Distance"], red_giants["Brightness"], color='red', label='Red Giants', s=120, alpha=0.7, edgecolors='k')
axs[0].scatter(white_dwarfs["Distance"], white_dwarfs["Brightness"], color='blue', label='White Dwarfs', s=120, alpha=0.7, edgecolors='k')
axs[0].scatter(main_sequence_stars["Distance"], main_sequence_stars["Brightness"], color='green', label='Main Sequence Stars', s=120, alpha=0.7, edgecolors='k')

# Add plot details to the first subplot
axs[0].set_title('Brightness vs Distance of Stars\nin the Andromeda Galaxy', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Distance from Earth (light-years)', fontsize=12)
axs[0].set_ylabel('Brightness (arbitrary units)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(title='Star Types', fontsize=10, loc='upper right')

# Second subplot: Star Color Index vs. Temperature Bar Plot
axs[1].bar(star_types, color_indices, color=['red', 'blue', 'green'], alpha=0.7)
axs[1].set_title('Star Color Index vs. Temperature', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Star Type', fontsize=12)
axs[1].set_ylabel('Color Index (arbitrary units)', fontsize=12)
axs[1].set_xticks(np.arange(len(star_types)))
axs[1].set_xticklabels(star_types, fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()