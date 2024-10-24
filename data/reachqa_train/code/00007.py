import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

# Energy sources
energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Renewable']

# Energy consumption data (in arbitrary units)
consumption_data = np.array([
    [80, 40, 30, 20, 10],  # 1980s
    [70, 50, 35, 25, 15],  # 1990s
    [60, 55, 40, 30, 20],  # 2000s
    [50, 60, 50, 35, 30],  # 2010s
    [40, 70, 55, 40, 50]   # 2020s
])

# Calculate percentage contributions for each energy source per decade
total_per_decade = consumption_data.sum(axis=1, keepdims=True)
percentage_contributions = (consumption_data / total_per_decade) * 100

# Colors for each energy source
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF2']

# Set up figure with two subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(18, 7), constrained_layout=True, subplot_kw={'projection': None})

# 3D Stacked Bar Chart (original)
ax1 = fig.add_subplot(121, projection='3d')
x_pos = np.arange(len(decades))
width = depth = 0.5
z_base = np.zeros(len(decades))

for i, (source, color) in enumerate(zip(energy_sources, colors)):
    ax1.bar3d(x_pos, z_base, np.zeros_like(x_pos), width, depth, consumption_data[:, i], color=color, alpha=0.8)
    z_base += consumption_data[:, i]

ax1.set_xlabel('Decade')
ax1.set_ylabel('Energy Source')
ax1.set_zlabel('Consumption (units)')
ax1.set_xticks(x_pos + width / 2)
ax1.set_xticklabels(decades)
ax1.set_title('Energy Sources Consumption in Energio\n (1980s to 2020s)', pad=20)
ax1.view_init(elev=20, azim=-45)

# 2D Line Plot for Percentage Contributions
ax2 = axs[1]
for i, (source, color) in enumerate(zip(energy_sources, colors)):
    ax2.plot(decades, percentage_contributions[:, i], marker='o', color=color, label=source)

ax2.set_xlabel('Decade')
ax2.set_ylabel('Percentage (%)')
ax2.set_title('Percentage Contribution of Energy Sources per Decade')
ax2.set_ylim(0, 100)
ax2.legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1, 1))

# Show plot
plt.show()