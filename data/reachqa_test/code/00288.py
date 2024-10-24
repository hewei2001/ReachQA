import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define the futuristic cities and their renewable energy adoption percentages
cities = ['NeoTokyo', 'Utopia', 'Solarpoli', 'Windville', 'Hydroburg', 
          'Biomassatopia', 'GeoHaven', 'Futuris', 'EcoMetropolis', 'GreenCrest']

energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal']

energy_data = np.array([
    [40, 20, 15, 15, 10],  # NeoTokyo
    [25, 35, 20, 10, 10],  # Utopia
    [60, 10, 10, 10, 10],  # Solarpoli
    [10, 50, 20, 10, 10],  # Windville
    [10, 10, 60, 10, 10],  # Hydroburg
    [15, 15, 15, 45, 10],  # Biomassatopia
    [10, 10, 10, 10, 60],  # GeoHaven
    [20, 30, 20, 20, 10],  # Futuris
    [30, 20, 30, 10, 10],  # EcoMetropolis
    [25, 25, 25, 15, 10]   # GreenCrest
])

colors = ['#FFD700', '#87CEEB', '#4682B4', '#8B4513', '#2E8B57']

fig, ax = plt.subplots(figsize=(16, 9))

max_index = np.unravel_index(np.argmax(energy_data), energy_data.shape)
min_index = np.unravel_index(np.argmin(energy_data), energy_data.shape)

for i, (city, energy) in enumerate(zip(cities, energy_data)):
    bottom = 0
    for j, (source, percentage) in enumerate(zip(energy_sources, energy)):
        edgecolor = 'black' if (i, j) in [max_index, min_index] else None
        bars = ax.bar(city, percentage, bottom=bottom, color=colors[j], edgecolor=edgecolor)
        bottom += percentage

        ax.text(x=bars[0].get_x() + bars[0].get_width() / 2, 
                y=bottom - percentage / 2, 
                s=f"{percentage}%", 
                ha='center', 
                va='center',
                fontsize=9, 
                color='white', 
                fontweight='bold')
    
    # Adding city icons
    ax.text(i, -5, "🏙️", ha='center', va='center', fontsize=14)

ax.legend([mpatches.Patch(color=color) for color in colors], energy_sources,
          title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1))

ax.set_title('Renewable Energy Adoption in Futuristic Cities\n'
             'Distribution by Energy Source\n'
             'Max & Min highlighted with outlines', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xlabel('Cities', fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.set_ylim(-10, 100)

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.xaxis.grid(False)

plt.tight_layout()
plt.show()