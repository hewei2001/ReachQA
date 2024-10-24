import matplotlib.pyplot as plt
import numpy as np

# Original data for delivery times (in hours) for different regions
urban_delivery_times = [24, 26, 30, 32, 35, 36, 40, 42, 43, 48]
suburban_delivery_times = [20, 22, 25, 28, 29, 30, 33, 34, 35, 38]
rural_delivery_times = [30, 32, 35, 37, 40, 43, 46, 50, 54, 58]
coastal_delivery_times = [18, 20, 22, 25, 27, 28, 29, 30, 31, 33]
mountainous_delivery_times = [36, 38, 42, 45, 47, 49, 52, 55, 58, 60]

# New related data: Success rates of delivery (%) for different regions
urban_success_rate = [90, 88, 85, 87, 86, 89, 92, 91, 93, 94]
suburban_success_rate = [91, 90, 89, 90, 92, 93, 91, 92, 94, 95]
rural_success_rate = [85, 84, 82, 83, 81, 86, 87, 89, 90, 88]
coastal_success_rate = [92, 93, 91, 92, 94, 93, 95, 96, 97, 96]
mountainous_success_rate = [88, 87, 85, 86, 84, 89, 90, 92, 91, 93]

# Combine data into a list for plotting
all_delivery_times = [
    urban_delivery_times,
    suburban_delivery_times,
    rural_delivery_times,
    coastal_delivery_times,
    mountainous_delivery_times
]

all_success_rates = [
    urban_success_rate,
    suburban_success_rate,
    rural_success_rate,
    coastal_success_rate,
    mountainous_success_rate
]

# Define region labels
regions = ['Urban', 'Suburban', 'Rural', 'Coastal', 'Mountainous']

# Create the plot with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Boxplot for delivery times
bp = axes[0].boxplot(all_delivery_times, patch_artist=True, vert=True, labels=regions, notch=True)
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF9966']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkblue', linewidth=1.5)

axes[0].set_title('Package Delivery Times by Region', fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel('Regions', fontsize=12)
axes[0].set_ylabel('Delivery Time (Hours)', fontsize=12)
axes[0].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Violin plot for success rates
vp = axes[1].violinplot(all_success_rates, showmeans=True, showmedians=False)
for pc in vp['bodies']:
    pc.set_facecolor('#D3D3D3')
    pc.set_edgecolor('black')
    pc.set_alpha(0.8)

# Adding mean and median lines
vp['cmeans'].set_color('blue')
vp['cmeans'].set_linewidth(1.5)

# Set x-ticks manually since violin plots don't include them by default
axes[1].set_xticks(np.arange(1, len(regions) + 1))
axes[1].set_xticklabels(regions)

axes[1].set_title('Delivery Success Rates by Region', fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel('Regions', fontsize=12)
axes[1].set_ylabel('Success Rate (%)', fontsize=12)
axes[1].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the chart
plt.show()