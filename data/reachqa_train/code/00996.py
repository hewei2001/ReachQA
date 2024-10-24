import matplotlib.pyplot as plt
import numpy as np

# Define sectors and commodities
sectors = ['Alpha', 'Beta', 'Gamma', 'Delta']
commodities = ['Water', 'Minerals', 'Food Supplies', 'Tech Components']

# Percentage distribution data for each sector
distribution_data = np.array([
    [28, 32, 20, 20],  # Alpha
    [22, 25, 28, 25],  # Beta
    [25, 18, 35, 22],  # Gamma
    [25, 25, 17, 33]   # Delta
])

# Additional data for a line chart representing time progression
time_periods = ['Year 1', 'Year 2', 'Year 3', 'Year 4']
trend_data = np.array([
    [26, 29, 19, 18],
    [28, 32, 20, 20],
    [30, 34, 22, 24],
    [32, 36, 24, 28]
])

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Calculate positions for the bars in the 3D bar chart
xpos, ypos = np.meshgrid(np.arange(len(sectors)), np.arange(len(commodities)))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = distribution_data.flatten()
dx = dy = 0.4
colors = ['#1E90FF', '#FFD700', '#32CD32', '#8A2BE2']

# Plot the 3D bar chart
ax1 = plt.subplot(121, projection='3d')
for i in range(len(commodities)):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i],
              color=colors[i], alpha=0.8, label=commodities[i])

ax1.set_xlabel('Sectors', fontsize=12, labelpad=10)
ax1.set_ylabel('Commodities', fontsize=12, labelpad=10)
ax1.set_zlabel('Percentage (%)', fontsize=12, labelpad=10)
ax1.set_xticks(np.arange(len(sectors)))
ax1.set_xticklabels(sectors, fontsize=10, rotation=45, ha='right')
ax1.set_yticks(np.arange(len(commodities)))
ax1.set_yticklabels(commodities, fontsize=10)
ax1.set_zlim(0, 100)
ax1.set_title('3D Distribution of Commodities\nin the Interstellar Trade Federation', 
              fontsize=14, weight='bold', pad=20)
ax1.legend(title='Commodity', loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

# Plot the line chart showing trends over time
for idx, commodity in enumerate(commodities):
    ax2.plot(time_periods, trend_data[:, idx], marker='o', label=commodity, color=colors[idx])

ax2.set_xlabel('Time Period', fontsize=12)
ax2.set_ylabel('Percentage (%)', fontsize=12)
ax2.set_title('Trend of Commodities Over Time', fontsize=14, weight='bold')
ax2.set_ylim(0, 40)
ax2.legend(title='Commodity', fontsize=10)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.show()