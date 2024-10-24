import matplotlib.pyplot as plt
import numpy as np

# Define primary renewable energy sources and their distribution in urban areas
energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal']
source_distribution = [45, 25, 15, 10, 5]

# Define sub-categories for each energy source and their distribution
sub_sources = [
    ['Residential Solar', 'Commercial Solar'],
    ['Onshore Wind', 'Offshore Wind'],
    ['Large-scale Hydro', 'Small-scale Hydro'],
    ['Biogas', 'Biofuel'],
    ['Direct Use', 'Enhanced Systems']
]
sub_source_distribution = [
    [60, 40],
    [70, 30],
    [80, 20],
    [50, 50],
    [30, 70],
]

# Calculate absolute numbers for sub-sources based on their parent distribution
sub_source_absolute = []
for i, source_dist in enumerate(source_distribution):
    sub_source_absolute.append([source_dist * p / 100 for p in sub_source_distribution[i]])

# Define colors for each energy source and its sub-categories using gradients
colors = ['#ffcc00', '#0099cc', '#33cc33', '#996633', '#cc6600']
sub_colors = [
    ['#ffe680', '#ffd11a'], 
    ['#80d4ff', '#1ab3ff'], 
    ['#66ff66', '#33cc33'], 
    ['#ccb38c', '#b37700'], 
    ['#ffcc80', '#e68a00'],
]

# Create figure and axes for the donut chart
fig, ax = plt.subplots(figsize=(12, 10))

# Outer ring chart for primary energy sources with an exploded view
wedges, texts, autotexts = ax.pie(
    source_distribution,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.9),
    explode=[0.05] * len(source_distribution)
)

# Inner ring chart for sub-categories with a 3D effect
for i, sub_dist in enumerate(sub_source_absolute):
    ax.pie(
        sub_dist,
        radius=0.7,
        startangle=140,
        colors=sub_colors[i],
        wedgeprops=dict(width=0.3, edgecolor='w', alpha=0.85)
    )

# Central label inside the ring chart
central_label = "Urban Renewable\nEnergy 2023"
plt.text(0, 0, central_label, ha='center', va='center', fontsize=14, weight='bold')

# Title
plt.title("Urban Areas' Renewable Energy Sources 2023:\nDistribution and Technologies",
          fontsize=16, weight='bold')

# Legend with interactive capability
legend = plt.legend(
    wedges, energy_sources, title="Energy Sources", loc='center left',
    bbox_to_anchor=(1, 0.5), fontsize='11'
)

# Functionality to toggle legend items
def on_pick(event):
    legend_item = event.artist
    index = legend_item.get_label()
    wedges[int(index)].set_visible(not wedges[int(index)].get_visible())
    plt.draw()

fig.canvas.mpl_connect("pick_event", on_pick)

# Ensure aspect ratio is equal to maintain circular shape
plt.axis('equal')

# Automatically adjust layout for optimal display
plt.tight_layout()

# Display the plot
plt.show()