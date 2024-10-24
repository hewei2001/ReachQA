import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of languages spoken by a significant percentage of the population in urban areas
language_diversity_data = [
    [15, 22, 10, 25, 18, 30, 19],  # Asia
    [8, 12, 7, 15, 9, 10, 14],     # Europe
    [5, 11, 8, 9, 7, 10],          # North America
    [20, 25, 30, 18, 27, 22, 24],  # Africa
    [10, 14, 9, 13, 11, 15, 12]    # South America
]

# Related data for the new subplot representing rural areas
rural_language_diversity_data = [17, 10, 8, 22, 13]

continents = ['Asia', 'Europe', 'North America', 'Africa', 'South America']

# Create the figure and both subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

# Box plot for urban areas
box = ax1.boxplot(language_diversity_data, vert=False, patch_artist=True, notch=True, whis=1.5,
                 boxprops=dict(facecolor='lightgrey', color='grey'),
                 whiskerprops=dict(color='grey'),
                 capprops=dict(color='grey'),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(marker='d', color='blue', alpha=0.5))

# Assign different colors to each box
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Setting labels and titles for the first plot
ax1.set_yticklabels(continents)
ax1.set_xlabel('Number of Languages Spoken', fontsize=12)
ax1.set_title('Linguistic Diversity in Urban Areas:\nA Comparative Analysis', fontsize=14, weight='bold')
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(left=0, right=35)
ax1.set_xticks(range(0, 36, 5))

# Bar plot for rural vs urban comparison
x = np.arange(len(continents))  # the label locations
width = 0.35  # the width of the bars

urban_means = [np.mean(data) for data in language_diversity_data]

rects1 = ax2.bar(x - width/2, urban_means, width, label='Urban', color='lightblue')
rects2 = ax2.bar(x + width/2, rural_language_diversity_data, width, label='Rural', color='lightgreen')

# Setting labels and title for the second plot
ax2.set_ylabel('Average Number of Languages Spoken', fontsize=12)
ax2.set_title('Urban vs Rural Linguistic Diversity', fontsize=14, weight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(continents)
ax2.legend()

# Adding value annotations to the bars
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1, ax2)
autolabel(rects2, ax2)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()