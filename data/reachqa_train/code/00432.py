import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Define decades and corresponding data for each mode of transportation
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']
walking = [35, 30, 25, 20, 15]
bicycling = [10, 12, 15, 17, 20]
public_transport = [20, 22, 25, 27, 30]
cars = [30, 32, 28, 30, 25]
air_travel = [5, 4, 7, 6, 10]

# Stack data into a numpy array
data = np.array([walking, bicycling, public_transport, cars, air_travel])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(14, 9))

# Define custom colors with gradients
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3']
textures = ['/', '\\', '|', '-', '+']

# Plot each mode with textures
handles = []
for i, (color, texture) in enumerate(zip(colors, textures)):
    ax.fill_between(decades, np.sum(data[:i+1], axis=0), np.sum(data[:i], axis=0),
                    color=color, alpha=0.8, label='', hatch=texture)
    handles.append(Patch(facecolor=color, edgecolor='black', hatch=texture, label=f'Transportation Mode {i+1}'))

# Configure title, labels, and legend
ax.set_title('Evolution of Transportation Modes\nOver the Decades', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage Usage (%)', fontsize=12)

# Add annotations for key trends
ax.annotate('Walking Decreases', xy=('1990s', 25), xytext=('2000s', 30),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontstyle='italic')

# Highlight key decade change
ax.axvline('2000s', color='grey', linestyle='--', linewidth=1)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.5, which='both')

# Add legend
ax.legend(handles=handles, loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()