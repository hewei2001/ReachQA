import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable, viridis

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

# Calculating medians for color mapping
medians = [np.median(d) for d in data]

# Create a figure with subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Configure a colormap
norm = Normalize(vmin=min(medians), vmax=max(medians))
cmap = viridis

# Create a horizontal boxplot
boxplot = ax.boxplot(data, vert=False, patch_artist=True, notch=True, showmeans=True)

# Customize colors using colormap
for patch, median in zip(boxplot['boxes'], medians):
    patch.set_facecolor(cmap(norm(median)))

# Customize mean and median lines
for mean, median in zip(boxplot['means'], boxplot['medians']):
    mean.set(marker='D', color='blue', markersize=7)
    median.set(color='red', linewidth=2)

# Add trendline
means = [np.mean(d) for d in data]
ax.plot(means, np.arange(1, len(means) + 1), 'k--', label='Mean Trendline')

# Set title and labels
ax.set_title('Wildlife Conservation Investments\n(2010-2020) Across Continents', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Annual Investment (Million USD)', fontsize=12)
ax.set_ylabel('Continent', fontsize=12)
ax.set_yticklabels(labels, fontsize=12)

# Add gridlines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add a colorbar for investment medians
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Median Investment Level', fontsize=12)

# Annotate mean values on the plot
for i, mean in enumerate(means, start=1):
    ax.annotate(f'{mean:.1f}', (mean, i), xytext=(10, 0),
                textcoords='offset points', color='blue', fontsize=10, va='center')

# Add a legend
ax.legend(loc='lower right', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Display the plot
plt.show()