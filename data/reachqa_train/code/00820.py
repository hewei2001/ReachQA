import matplotlib.pyplot as plt
import numpy as np

# Data
planets = ['Aridiona', 'Verdeene', 'Nublar', 'Caelum', 'Frostine', 'Terralune']
atmospheric_nitrogen = np.array([30, 55, 60, 20, 45, 50])
nutritional_value = np.array([5.5, 7.3, 6.2, 4.0, 6.8, 7.0])

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 7))
scatter = ax.scatter(atmospheric_nitrogen, nutritional_value, 
                     c=nutritional_value, cmap='viridis', s=150, edgecolor='gray', alpha=0.8)

# Title and labels
ax.set_title('Intergalactic Crop Assessment\nAtmospheric Nitrogen vs. Nutritional Value',
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Atmospheric Nitrogen Level (%)', fontsize=12)
ax.set_ylabel('Nutritional Value Index', fontsize=12)

# Adding a color bar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Nutritional Value Index', fontsize=12, fontweight='bold')

# Annotate each point with planet name
for i, planet_name in enumerate(planets):
    ax.annotate(planet_name, (atmospheric_nitrogen[i], nutritional_value[i]), 
                fontsize=10, ha='right', va='bottom', color='black')

# Enhancements
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
ax.set_xlim(15, 65)  # Adjusted limits for a better view
ax.set_ylim(3.5, 7.5)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()