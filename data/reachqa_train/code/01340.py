import matplotlib.pyplot as plt
import numpy as np

# Data for tree heights (in meters)
redwood_heights = [100, 110, 115, 120, 130, 140, 145, 150, 155, 160]
douglas_fir_heights = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
oak_heights = [60, 65, 70, 75, 78, 80, 85, 90, 92, 95]
maple_heights = [45, 50, 55, 58, 60, 62, 65, 68, 70, 72]
birch_heights = [40, 42, 45, 47, 48, 50, 52, 54, 55, 57]

data = [redwood_heights, douglas_fir_heights, oak_heights, maple_heights, birch_heights]
labels = ['Redwood', 'Douglas Fir', 'Oak', 'Maple', 'Birch']

# Synthesize data for average annual growth (in cm/year)
years = np.arange(10)
redwood_growth = [30, 32, 35, 38, 36, 40, 42, 45, 44, 48]
douglas_fir_growth = [25, 26, 27, 29, 28, 30, 31, 32, 33, 34]
oak_growth = [22, 24, 23, 25, 26, 27, 28, 30, 29, 31]
maple_growth = [18, 20, 19, 21, 22, 23, 24, 25, 26, 27]
birch_growth = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

growth_data = [redwood_growth, douglas_fir_growth, oak_growth, maple_growth, birch_growth]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [1, 1]})

# Create the box plot for tree heights
box = ax1.boxplot(data, patch_artist=True, notch=True,
                  boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                  medianprops=dict(color='darkred', linewidth=2),
                  whiskerprops=dict(color='green'),
                  capprops=dict(color='green'),
                  flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5))

colors = ['#8FBC8F', '#DEB887', '#F4A460', '#BC8F8F', '#DAA520']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_title("Journey Through the Woods:\nDistribution of Tree Heights in Ancient Forests", fontsize=14, fontweight='bold')
ax1.set_xlabel("Tree Species", fontsize=12)
ax1.set_ylabel("Height (meters)", fontsize=12)
ax1.set_xticks(np.arange(1, len(labels) + 1))
ax1.set_xticklabels(labels, rotation=30, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_facecolor('#F5F5DC')

highlight_species = 'Redwood'
highlight_index = labels.index(highlight_species) + 1
ax1.plot([highlight_index-0.25, highlight_index+0.25], 
         [np.median(redwood_heights), np.median(redwood_heights)], 
         color='darkorange', lw=3, label=f'{highlight_species} Median')
ax1.legend(loc='upper right', frameon=True, fontsize=10)

# Create a line plot for average annual growth
for growth, label, color in zip(growth_data, labels, colors):
    ax2.plot(years, growth, label=label, color=color, linewidth=2)

ax2.set_title("Average Annual Growth of Tree Species\n(Over 10 Years)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Years", fontsize=12)
ax2.set_ylabel("Growth (cm/year)", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc='upper left', fontsize=10)
ax2.set_facecolor('#FAFAD2')

plt.tight_layout()
plt.show()