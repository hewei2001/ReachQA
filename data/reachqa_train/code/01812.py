import matplotlib.pyplot as plt
import numpy as np

# Define the data for exoplanet discoveries
years = np.array([2018, 2019, 2020, 2021, 2022])
missions = ['Kepler', 'TESS', 'CHEOPS', 'JWST']
discovery_data = np.array([
    [100, 80, 60, 40, 20],   # Kepler
    [10, 20, 30, 40, 50],    # TESS
    [5, 15, 10, 20, 25],     # CHEOPS
    [0, 0, 5, 15, 30]        # JWST
])

# Calculate cumulative discoveries
cumulative_discovery = np.cumsum(discovery_data, axis=1)

# Create subplots
fig = plt.figure(figsize=(16, 8))

# 3D Bar Chart
ax1 = fig.add_subplot(121, projection='3d')
xpos, ypos = np.meshgrid(np.arange(discovery_data.shape[1]), np.arange(discovery_data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dz = discovery_data.flatten()
dx = dy = 0.5
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i in range(discovery_data.shape[0]):
    ax1.bar3d(xpos[ypos == i], ypos[ypos == i], zpos[ypos == i], dx, dy, dz[ypos == i], 
              color=colors[i], alpha=0.8, label=missions[i])

ax1.set_xlabel('Year')
ax1.set_ylabel('Mission')
ax1.set_zlabel('Exoplanets Discovered')
ax1.set_yticks(range(len(missions)))
ax1.set_yticklabels(missions)
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years)
ax1.view_init(elev=20, azim=45)
ax1.set_title('Exoplanet Discovery\nBy Space Missions (2018-2022)', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

# 2D Line Plot for Cumulative Discoveries
ax2 = fig.add_subplot(122)
for i in range(len(missions)):
    ax2.plot(years, cumulative_discovery[i, :], marker='o', color=colors[i], label=missions[i])

ax2.set_xlabel('Year')
ax2.set_ylabel('Cumulative Discoveries')
ax2.set_title('Cumulative Exoplanet Discoveries\nPer Mission (2018-2022)', fontsize=14, fontweight='bold')
ax2.set_xticks(years)
ax2.legend(loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()