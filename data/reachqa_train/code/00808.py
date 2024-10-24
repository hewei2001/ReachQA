import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Regions
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']

# Solar power capacity data (in megawatts) for each region
north_america = [150, 160, 165, 170, 155, 160, 165, 180, 175, 160]
europe = [100, 110, 105, 115, 110, 120, 130, 125, 115, 105]
asia = [200, 210, 205, 220, 215, 225, 230, 240, 235, 210]
africa = [50, 55, 60, 65, 70, 55, 60, 75, 65, 60]
south_america = [80, 85, 90, 95, 85, 100, 105, 90, 95, 100]

# Aggregating all data
data = [north_america, europe, asia, africa, south_america]

# Create additional dataset for violin plot (slightly adjusted to create variation)
north_america_v = np.array(north_america) + np.linspace(-10, 10, 10)
europe_v = np.array(europe) * np.linspace(0.9, 1.1, 10)
asia_v = np.array(asia) + np.linspace(-20, 20, 10)
africa_v = np.array(africa) * np.linspace(0.95, 1.05, 10)
south_america_v = np.array(south_america) + np.linspace(-5, 5, 10)

# Aggregating violin data
data_violin = [north_america_v, europe_v, asia_v, africa_v, south_america_v]

# Initialize subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Boxplot on the first subplot
box = axes[0].boxplot(data, patch_artist=True, labels=regions, notch=True, widths=0.6)

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='grey', linewidth=2)
    cap.set(color='grey', linewidth=2)
for median in box['medians']:
    median.set(color='orange', linewidth=3)
for flier in box['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

axes[0].set_title("Distribution of Solar Energy Installations\nAcross Regions (in MW)", fontsize=14, weight='bold')
axes[0].set_ylabel("Solar Power Capacity (MW)")
axes[0].set_xlabel("Regions")
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Violin plot on the second subplot
sns.violinplot(data=data_violin, palette=colors, ax=axes[1])
axes[1].set_title("Violin Plot of Solar Energy Data\n(Adjusted View)", fontsize=14, weight='bold')
axes[1].set_ylabel("Adjusted Solar Power Capacity (MW)")
axes[1].set_xlabel("Regions")
axes[1].set_xticks(range(len(regions)))
axes[1].set_xticklabels(regions)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Shared legend
handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
fig.legend(handles, regions, title="Regions", loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()