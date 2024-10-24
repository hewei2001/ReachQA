import matplotlib.pyplot as plt
import numpy as np

# Data setup
garden_sizes = np.array([50, 75, 100, 150, 180, 210, 230, 250, 275, 300])
plant_species_count = np.array([10, 15, 20, 30, 35, 40, 42, 45, 47, 50])
uniqueness = np.array([2, 3, 2, 5, 4, 6, 3, 5, 5, 6])

# Define colors for different levels of uniqueness
colors = np.array(['#76C7C0', '#76C7C0', '#4D9C89', '#38876B', '#285D4C', '#6FA579',
                   '#92C7A3', '#438D72', '#5BA680', '#3D7F63'])

# Overlay Line Plot Data (using a polynomial fit for complexity)
z = np.polyfit(garden_sizes, plant_species_count, 2)  # Quadratic fit
p = np.poly1d(z)
garden_fit = np.linspace(garden_sizes.min(), garden_sizes.max(), 100)
species_fit = p(garden_fit)

# Create the figure and main scatter plot
plt.figure(figsize=(12, 8))
scatter = plt.scatter(garden_sizes, plant_species_count, s=uniqueness*80, c=colors, alpha=0.6, edgecolor='k', label='Actual Data')

# Add the polynomial fit line plot
plt.plot(garden_fit, species_fit, "r--", label='Estimated Trend', linewidth=2)

# Enhance visual complexity with annotations for selected data points
selected_indices = [1, 3, 5, 8]
for i in selected_indices:
    plt.annotate(f'Size: {garden_sizes[i]}\nSpecies: {plant_species_count[i]}', 
                 (garden_sizes[i], plant_species_count[i]), textcoords="offset points",
                 xytext=(-30,10), ha='center', fontsize=9, color='navy', 
                 arrowprops=dict(arrowstyle='->', lw=0.8, color='navy'))

# Chart details
plt.title("Gardens of Imagination:\nBiodiversity in Urban Community Spaces", fontsize=16, weight='bold')
plt.xlabel("Garden Size (Square Meters)", fontsize=12)
plt.ylabel("Number of Plant Species", fontsize=12)

# Adding legend for scatter plot
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='High Design Uniqueness', 
               markerfacecolor='#285D4C', markersize=15),
    plt.Line2D([0], [0], marker='o', color='w', label='Moderate Design Uniqueness', 
               markerfacecolor='#4D9C89', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Low Design Uniqueness', 
               markerfacecolor='#76C7C0', markersize=5)
]
plt.legend(handles=legend_elements + [scatter], loc="upper left", title="Design Uniqueness", fontsize=10, title_fontsize='11')

# Customize the grid and layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()