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

# Create a scatter plot
plt.figure(figsize=(12, 8))

# Plot each star type with distinctive markers and colors
plt.scatter(red_giants["Distance"], red_giants["Brightness"], 
            color='red', label='Red Giants', s=120, alpha=0.7, edgecolors='k')
plt.scatter(white_dwarfs["Distance"], white_dwarfs["Brightness"], 
            color='blue', label='White Dwarfs', s=120, alpha=0.7, edgecolors='k')
plt.scatter(main_sequence_stars["Distance"], main_sequence_stars["Brightness"], 
            color='green', label='Main Sequence Stars', s=120, alpha=0.7, edgecolors='k')

# Add plot details
plt.title('Brightness vs Distance of Stars\nin the Andromeda Galaxy', fontsize=16, fontweight='bold')
plt.xlabel('Distance from Earth (light-years)', fontsize=14)
plt.ylabel('Brightness (arbitrary units)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend and ensure it does not obstruct the data visualization
plt.legend(title='Star Types', fontsize=12, loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()