import matplotlib.pyplot as plt
import numpy as np

# Air Quality Index (AQI) data for each region
region_a_aqi = np.array([50, 55, 60, 62, 58, 59, 61, 54, 53, 57, 63, 66, 68])
region_b_aqi = np.array([80, 82, 85, 87, 83, 88, 84, 85, 81, 90, 92, 95, 97])
region_c_aqi = np.array([40, 42, 45, 41, 43, 46, 39, 37, 48, 45, 47, 44, 43])
region_d_aqi = np.array([70, 75, 78, 72, 76, 73, 74, 77, 79, 71, 72, 70, 69])
region_e_aqi = np.array([60, 65, 68, 66, 67, 69, 61, 64, 62, 63, 70, 72, 73])

# Collecting data into a list for boxplot
data = [region_a_aqi, region_b_aqi, region_c_aqi, region_d_aqi, region_e_aqi]

# Create the vertical box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the boxplot
bp = ax.boxplot(data, patch_artist=True, vert=True, widths=0.6, notch=True,
                boxprops=dict(facecolor='lightgrey', color='black'),
                whiskerprops=dict(color='black'), capprops=dict(color='black'),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='red', alpha=0.6))

# Adding grid for clarity
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Customizing plot labels and title
ax.set_xticklabels(['Region A', 'Region B', 'Region C', 'Region D', 'Region E'], fontsize=12)
ax.set_ylabel('Air Quality Index (AQI)', fontsize=14)
ax.set_xlabel('Urban Regions', fontsize=14)
ax.set_title('Variability in Air Quality Index (AQI)\nAcross Major Urban Regions',
             fontsize=16, fontweight='bold', pad=20)

# Highlighting medians with annotations
for i, median in enumerate(bp['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{y_median:.1f}', xy=(x_median, y_median), xytext=(0, 10), 
                textcoords='offset points', color='red', fontsize=10, ha='center')

# Enhancing visual distinctiveness by coloring the boxes differently
colors = ['skyblue', 'lightgreen', 'lightpink', 'lightyellow', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Ensure no overlap and improve layout
plt.tight_layout()

# Display the chart
plt.show()