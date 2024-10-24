import matplotlib.pyplot as plt
import numpy as np

# Insect specimen sizes in millimeters for each region (original data)
data_north_america = [10, 11, 12, 14, 13, 15, 12, 11, 13, 14, 12, 13, 15, 14, 13]
data_south_america = [20, 22, 24, 25, 23, 21, 22, 25, 24, 23, 21, 25, 23, 22, 24]
data_europe = [30, 32, 31, 33, 30, 32, 34, 33, 31, 30, 32, 33, 31, 34, 32]
data_africa = [40, 42, 41, 43, 40, 42, 45, 44, 41, 40, 42, 43, 41, 44, 42]
data_asia = [50, 52, 54, 53, 51, 52, 54, 53, 51, 50, 52, 53, 51, 54, 52]

# Related but altered data for violin plot
data_north_america_v = [x + 0.5 for x in data_north_america]
data_south_america_v = [x - 0.5 for x in data_south_america]
data_europe_v = [x + 1 for x in data_europe]
data_africa_v = [x - 1 for x in data_africa]
data_asia_v = [x + 0.8 for x in data_asia]

# Combine data for plots
data_boxplot = [data_north_america, data_south_america, data_europe, data_africa, data_asia]
data_violinplot = [data_north_america_v, data_south_america_v, data_europe_v, data_africa_v, data_asia_v]

regions = ['North America', 'South America', 'Europe', 'Africa', 'Asia']
colors = ['#ffb3ba', '#baffc9', '#bae1ff', '#ffffba', '#ffdfba']

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 7), sharey=True)

# Box Plot
box = axes[0].boxplot(data_boxplot, patch_artist=True, vert=False, notch=True,
                      boxprops=dict(facecolor='#b3cde3', color='#011f4b'),
                      whiskerprops=dict(color='#011f4b'),
                      capprops=dict(color='#011f4b'),
                      medianprops=dict(color='#ff0000'))

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axes[0].set_title('Insect Diversity Across Global Regions:\nBox Plot of Specimen Size Variation', fontsize=12, fontweight='bold', pad=10)
axes[0].set_xlabel('Specimen Size (mm)', fontsize=10)
axes[0].set_yticklabels(regions, fontsize=9)
axes[0].grid(True, linestyle='--', alpha=0.5)

# Violin Plot
violin = axes[1].violinplot(data_violinplot, vert=False, showmeans=True, showextrema=True, showmedians=True)
for i, pc in enumerate(violin['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.7)

axes[1].set_title('Violin Plot of Specimen Size Distribution', fontsize=12, fontweight='bold', pad=10)
axes[1].set_xlabel('Specimen Size (mm)', fontsize=10)

# Add legend
for ax, title in zip(axes, ['Box Plot', 'Violin Plot']):
    for i, color in enumerate(colors):
        ax.plot([], [], color=color, label=regions[i], linewidth=6)
    ax.legend(loc='lower right', title=title, frameon=True, fontsize=8)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()