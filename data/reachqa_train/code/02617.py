import matplotlib.pyplot as plt
import numpy as np

# Data setup
crop_names = ['Wheat', 'Corn', 'Rice', 'Soybeans', 'Cotton']
wheat_yield = [2.5, 3.0, 3.2, 2.8, 2.9, 3.5, 3.1, 2.7, 3.3, 2.4]
corn_yield = [5.0, 5.5, 5.2, 6.0, 5.8, 5.7, 5.1, 6.2, 5.4, 5.3]
rice_yield = [4.0, 4.2, 4.1, 4.5, 4.3, 4.4, 4.0, 4.6, 4.8, 4.5]
soybean_yield = [3.0, 3.5, 3.7, 3.3, 3.6, 3.4, 3.9, 3.2, 3.1, 3.8]
cotton_yield = [1.8, 2.0, 2.1, 2.3, 2.2, 2.5, 2.4, 2.0, 1.9, 2.1]

# Combine yield data for the plot
data = [wheat_yield, corn_yield, rice_yield, soybean_yield, cotton_yield]

# Create horizontal box plot
fig, ax = plt.subplots(figsize=(10, 7))
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')

# Boxplot with detailed customization
ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, notch=True,
           boxprops=boxprops, medianprops=medianprops, meanprops=meanprops,
           whiskerprops=dict(linewidth=1.5), capprops=dict(linewidth=1.5))

# Setting plot details
ax.set_yticklabels(crop_names, fontsize=12)
ax.set_title('Impact of Climate Change on Crop Yields\nAcross Different Climate Zones', 
             fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Yield (tonnes/ha)', fontsize=12)
ax.set_ylabel('Crops', fontsize=12)

# Adding gridlines
ax.grid(True, which='both', linestyle='--', alpha=0.5)

# Customize colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Add annotations for clarity
for i, crop in enumerate(crop_names):
    ax.text(data[i][-1] + 0.05, i + 1, f'{np.mean(data[i]):.2f} mean',
            va='center', fontsize=10, color='black', weight='bold')

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()