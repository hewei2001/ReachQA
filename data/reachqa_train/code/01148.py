import matplotlib.pyplot as plt
import numpy as np

# Data representing financial investments in wildlife conservation (in millions) over the last decade
investments = {
    'Africa': [25, 30, 35, 20, 40, 50, 55, 60, 65, 30],
    'Asia': [15, 20, 15, 25, 30, 10, 20, 20, 25, 20],
    'Europe': [60, 70, 65, 75, 80, 85, 90, 95, 100, 85],
    'North America': [45, 50, 55, 65, 70, 75, 80, 85, 90, 60],
    'South America': [35, 40, 30, 25, 50, 45, 40, 60, 65, 55]
}

# Extracting data and labels
data = list(investments.values())
labels = list(investments.keys())

# Create a horizontal boxplot
fig, ax = plt.subplots(figsize=(12, 8))
boxplot = ax.boxplot(data, vert=False, patch_artist=True, notch=True, showmeans=True)

# Customize colors for each box plot
colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Customize mean and median lines
for mean, median in zip(boxplot['means'], boxplot['medians']):
    mean.set(marker='D', color='black', markersize=5)
    median.set(color='red', linewidth=2)

# Set title and labels
ax.set_title('Wildlife Conservation Investments (2010-2020)\nAcross Continents', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Annual Investment (Million USD)', fontsize=12)
ax.set_ylabel('Continent', fontsize=12)
ax.set_yticklabels(labels, fontsize=12)

# Add gridlines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust the layout to prevent label and title overlaps
plt.tight_layout()

# Display the plot
plt.show()