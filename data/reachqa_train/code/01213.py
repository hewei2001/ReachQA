import numpy as np
import matplotlib.pyplot as plt

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

# Create the heat map
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(traffic_data, cmap='YlGnBu', aspect='auto')

# Add a color bar
cbar = fig.colorbar(cax, ax=ax)
cbar.set_label('Internet Traffic (Petabytes)', rotation=270, labelpad=20)

# Set ticks and labels
ax.set_xticks(np.arange(len(days)))
ax.set_yticks(np.arange(len(continents)))
ax.set_xticklabels(days, rotation=45, ha='right')
ax.set_yticklabels(continents)

# Title and layout
ax.set_title('Weekly Internet Traffic Across Continents\n(Reported in Petabytes)', pad=20)

# Annotate traffic values on the heat map
for i in range(len(continents)):
    for j in range(len(days)):
        ax.text(j, i, f'{traffic_data[i, j]}', ha='center', va='center', color='black', fontsize=10)

# Adjust layout for better visibility
plt.tight_layout()

# Show the plot
plt.show()