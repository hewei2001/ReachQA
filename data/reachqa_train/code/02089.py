import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Data for renewable energy sources and their respective percentages
energy_sources = ['Solar Energy', 'Wind Energy', 'Hydroelectric', 'Biomass', 'Geothermal']
percentages = [35, 25, 20, 15, 5]
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513', '#FF4500']
patterns = ['', '\\\\', '//', '||', '++']

# Create a ring chart with enhanced design
fig, ax = plt.subplots(figsize=(10, 10))

# Slightly explode each slice for emphasis
explode = [0.05] * len(percentages)

# Plotting the pie chart with gradient colors and patterns
wedges, texts, autotexts = ax.pie(
    percentages,
    explode=explode,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w', hatch=patterns),
    textprops=dict(color="darkslategray", weight='bold', size=12)
)

# Add a shadow to create a 3D effect
plt.gca().set_aspect('equal')
ax.set_frame_on(False)

# Add central circle for ring effect
center_circle = Circle((0, 0), 0.6, fc='white', edgecolor='gray')
fig.gca().add_artist(center_circle)

# Enhance readability of text
plt.setp(autotexts, size=10, weight='bold', color='navy')

# Title with line breaks and enhanced style
plt.title(
    "Greenfield City's 2023 Green Energy Initiative\nDistribution of Renewable Energy Sources",
    fontsize=16, weight='bold', color='darkgreen', pad=20
)

# Enhanced central text
ax.text(0, 0, 'Green\nEnergy\n2023', horizontalalignment='center', verticalalignment='center',
        fontsize=14, color='darkgreen', weight='bold', style='italic')

# Legend improvements with percentage inclusion
ax.legend(wedges, [f"{energy_sources[i]} - {percentages[i]}%" for i in range(len(energy_sources))],
          title="Energy Sources",
          loc='center left',
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the ring chart
plt.show()