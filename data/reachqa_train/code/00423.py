import matplotlib.pyplot as plt
import numpy as np

# Data representing daily energy consumption (in terajoules) over a month for each sector
residential = [22, 24, 21, 23, 25, 30, 22, 23, 19, 24, 25, 26, 21, 23, 24, 24, 27, 29, 30, 32, 28, 23, 21, 22, 23, 24, 28, 27, 22, 24]
agricultural = [35, 32, 33, 34, 31, 38, 37, 34, 35, 33, 36, 38, 32, 31, 33, 34, 38, 40, 36, 37, 35, 34, 33, 32, 31, 39, 36, 34, 33, 32]
research = [18, 19, 20, 21, 22, 17, 18, 19, 25, 24, 23, 26, 20, 21, 18, 19, 22, 21, 20, 24, 25, 26, 21, 22, 20, 19, 18, 22, 20, 19]
industrial = [50, 55, 53, 52, 51, 58, 60, 59, 57, 56, 54, 52, 53, 55, 50, 51, 59, 58, 60, 57, 56, 58, 59, 60, 55, 53, 52, 54, 55, 56]
commercial = [28, 29, 30, 31, 29, 32, 31, 30, 33, 34, 28, 29, 27, 30, 31, 35, 36, 34, 33, 32, 31, 30, 29, 32, 34, 30, 29, 28, 31, 30]

# Calculate total monthly consumption for each sector
total_consumption = [sum(residential), sum(agricultural), sum(research), sum(industrial), sum(commercial)]

# Sector labels
sectors = ["Residential", "Agricultural", "Research", "Industrial", "Commercial"]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 8), gridspec_kw={'width_ratios': [2, 1]})

# First subplot - Box Plot
box = axs[0].boxplot([residential, agricultural, research, industrial, commercial], vert=False, patch_artist=True, notch=True,
                     boxprops=dict(facecolor='lightblue', color='navy'),
                     whiskerprops=dict(color='navy'),
                     capprops=dict(color='navy'),
                     flierprops=dict(marker='o', color='red', markersize=8, alpha=0.6),
                     medianprops=dict(color='orange', linewidth=2))

colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title('Energy Consumption Patterns in New Phoenix:\nDaily Usage Across Different Sectors', fontsize=14, fontweight='bold', color='darkgreen')
axs[0].set_xlabel('Daily Energy Consumption (Terajoules)', fontsize=12, fontweight='bold')
axs[0].set_yticks(np.arange(1, len(sectors) + 1))
axs[0].set_yticklabels(sectors, fontsize=12, fontweight='bold')
axs[0].grid(axis='x', linestyle='--', alpha=0.7)

# Second subplot - Bar Chart
axs[1].barh(sectors, total_consumption, color=colors, edgecolor='navy')
axs[1].set_title('Total Monthly Energy Consumption\nby Sector', fontsize=14, fontweight='bold', color='darkblue')
axs[1].set_xlabel('Total Energy Consumption (Terajoules)', fontsize=12, fontweight='bold')
axs[1].set_xlim(0, max(total_consumption) * 1.1)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()