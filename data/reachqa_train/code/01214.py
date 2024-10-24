import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

# Define continents and days
continents = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Internet traffic data in petabytes (manually adjusted)
traffic_data = np.array([
    [200, 180, 170, 160, 190, 150, 140],  # North America
    [150, 140, 135, 130, 150, 120, 110],  # Europe
    [320, 310, 300, 290, 330, 300, 290],  # Asia
    [80, 75, 70, 65, 90, 60, 50],         # Africa
    [100, 95, 90, 85, 105, 80, 70]        # South America
])

# Create the heat map with improved visual elements
fig, ax = plt.subplots(figsize=(12, 8))
cmap = get_cmap('coolwarm')
norm = Normalize(vmin=np.min(traffic_data), vmax=np.max(traffic_data))
cax = ax.imshow(traffic_data, cmap=cmap, aspect='auto', norm=norm)

# Add color bar with improved alignment
cbar = fig.colorbar(cax, ax=ax, pad=0.02, fraction=0.03)
cbar.set_label('Internet Traffic (Petabytes)', rotation=270, labelpad=20)

# Set ticks and labels
ax.set_xticks(np.arange(len(days)))
ax.set_yticks(np.arange(len(continents)))
ax.set_xticklabels(days, rotation=45, ha='right')
ax.set_yticklabels(continents)

# Title and layout
ax.set_title('Weekly Internet Traffic Across Continents\n(Data Reported in Petabytes)', pad=20)

# Annotate traffic values on the heat map with dynamic color contrast
for i in range(len(continents)):
    for j in range(len(days)):
        value = traffic_data[i, j]
        text_color = 'white' if norm(value) < 0.5 else 'black'
        ax.text(j, i, f'{value}', ha='center', va='center', color=text_color, fontsize=10)

# Highlight max and min values
min_val, max_val = np.min(traffic_data), np.max(traffic_data)
for i in range(len(continents)):
    for j in range(len(days)):
        if traffic_data[i, j] == min_val or traffic_data[i, j] == max_val:
            ax.text(j, i, f'{traffic_data[i, j]}', ha='center', va='center', color='yellow', fontsize=11, fontweight='bold')

# Add grid lines
ax.grid(visible=True, color='lightgrey', linestyle='-', linewidth=0.5)

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()