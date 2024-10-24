import matplotlib.pyplot as plt
import numpy as np

# Expanded Floral diversity index scores for each decade
floral_1930s = [1, 2, 3, 2, 3, 4, 2, 3, 4, 3, 4, 2, 3]
floral_1940s = [2, 3, 3, 3, 4, 4, 3, 4, 5, 4, 3, 4, 3]
floral_1950s = [2, 3, 4, 4, 5, 5, 4, 5, 6, 5, 4, 5, 4]
floral_1960s = [3, 5, 4, 6, 7, 5, 6, 7, 8, 5, 4, 6, 7]
floral_1970s = [4, 6, 5, 7, 6, 5, 8, 9, 7, 6, 6, 8, 7]
floral_1980s = [5, 7, 6, 8, 9, 7, 8, 10, 9, 8, 7, 9, 8]
floral_1990s = [6, 8, 7, 9, 10, 8, 9, 11, 10, 9, 8, 10, 9]
floral_2000s = [7, 9, 8, 10, 11, 9, 10, 12, 11, 10, 9, 11, 10]
floral_2010s = [8, 10, 9, 11, 12, 10, 11, 13, 12, 11, 10, 12, 11]
floral_2020s = [9, 11, 10, 12, 13, 11, 12, 14, 13, 12, 11, 13, 12]

# Combine data into a single list for plotting
data = [floral_1930s, floral_1940s, floral_1950s, floral_1960s, floral_1970s,
        floral_1980s, floral_1990s, floral_2000s, floral_2010s, floral_2020s]

# Labels for each decade
labels = ['1930s', '1940s', '1950s', '1960s', '1970s', '1980s', 
          '1990s', '2000s', '2010s', '2020s']

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create the box plot with additional statistical measures
bplot = ax.boxplot(data, notch=True, vert=True, patch_artist=True, labels=labels,
                   boxprops=dict(linewidth=2, color='black'), 
                   medianprops=dict(linewidth=2, color='firebrick'),
                   whiskerprops=dict(linestyle='--', linewidth=1.5, color='black'),
                   capprops=dict(linewidth=1.5, color='black'), 
                   showmeans=True, meanprops=dict(marker='D', markerfacecolor='blue', markersize=6))

# Color the boxes with transparency
colors = ['#FFD700', '#8A2BE2', '#FF69B4', '#3CB371', '#FF4500', 
          '#FFA07A', '#7FFFD4', '#D2691E', '#DC143C', '#00BFFF']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)

# Titles and labels
ax.set_title('Floral Diversity Trends Across Decades\nExpanding Aesthetics from 1930s to 2020s', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Floral Diversity Index', fontsize=12)

# Adding grid lines and rotating x-tick labels
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.xticks(rotation=45)

# Second plot: Mean trends
ax2 = ax.twinx()
decade_indices = np.arange(len(data))
means = [np.mean(decade) for decade in data]
ax2.plot(decade_indices + 1, means, marker='o', linestyle='-', color='darkblue', label='Mean Trend')
ax2.set_ylabel('Mean Diversity Index', fontsize=12, color='darkblue')
ax2.tick_params(axis='y', labelcolor='darkblue')

# Adding legends
ax.legend([bplot["medians"][0], bplot["means"][0]], ['Median', 'Mean'], loc='upper left')
ax2.legend(loc='upper right')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()