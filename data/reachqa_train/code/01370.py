import matplotlib.pyplot as plt
import numpy as np

# Define city names
cities = [
    'Metropolis', 'Gotham', 'Atlantis', 'Zion', 'Neo City', 
    'Elysium', 'Arcadia', 'Utopia', 'Avalon', 'Shangri-La', 
    'Valhalla', 'Erewhon', 'El Dorado', 'Brigadoon', 'Camelot'
]

# Data for the original scatter plot
infrastructure_index = np.array([
    78, 65, 85, 90, 72, 
    88, 67, 55, 73, 69, 
    80, 66, 77, 62, 94
])
advocacy_density = np.array([
    120, 95, 150, 170, 110, 
    160, 105, 80, 100, 90, 
    140, 85, 115, 75, 180
])
sizes = np.array([
    200, 150, 250, 300, 180, 
    270, 160, 130, 190, 140, 
    230, 145, 185, 125, 310
])

# New data for the additional subplot
economic_stability_index = np.array([
    70, 60, 88, 92, 75, 
    86, 70, 65, 72, 68, 
    82, 64, 76, 61, 95
])
cultural_events_per_year = np.array([
    35, 25, 45, 55, 30, 
    50, 28, 20, 25, 22, 
    40, 18, 30, 15, 60
])

# Create the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# First subplot: Scatter plot
sc = ax1.scatter(infrastructure_index, advocacy_density, s=sizes, c=sizes, cmap='viridis', alpha=0.8, edgecolors='w', linewidth=0.5)
ax1.set_title("Nexus of City Infrastructure & Legal Advocacy\nA Study of Urban Dynamics", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Infrastructure Index", fontsize=12)
ax1.set_ylabel("Legal Advocacy Group Density\n(per 100k Population)", fontsize=12)
ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
cbar = plt.colorbar(sc, ax=ax1)
cbar.set_label('Point Size Indicator', fontsize=12)
for i, city in enumerate(cities):
    ax1.annotate(city, (infrastructure_index[i], advocacy_density[i]), fontsize=9, ha='right', textcoords='offset points', xytext=(-5, -5))

# Second subplot: Bar plot
bar_width = 0.35
indices = np.arange(len(cities))

ax2.bar(indices - bar_width/2, economic_stability_index, bar_width, label='Economic Stability Index', color='teal')
ax2.bar(indices + bar_width/2, cultural_events_per_year, bar_width, label='Cultural Events per Year', color='goldenrod')
ax2.set_title("Economic & Cultural Profiles of Cities", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Cities", fontsize=12)
ax2.set_ylabel("Index / Events per Year", fontsize=12)
ax2.set_xticks(indices)
ax2.set_xticklabels(cities, rotation=45, ha='right', fontsize=9)
ax2.legend(fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

# Adjust layout for clarity
plt.tight_layout()

# Display the plots
plt.show()