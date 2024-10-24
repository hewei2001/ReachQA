import matplotlib.pyplot as plt
import numpy as np

# Define an expanded dataset for tea quality scores across regions, with varied distributions
assam_tea_data = {
    'Upper Assam': [82, 85, 88, 90, 83, 79, 87, 91, 84, 86, 89, 90, 88, 84, 91, 85, 87, 89, 90, 86],
    'Lower Assam': [75, 80, 77, 82, 74, 70, 79, 76, 73, 78, 77, 72, 81, 74, 75, 79, 77, 78, 73, 80],
    'Central Assam': [90, 93, 95, 92, 89, 88, 94, 96, 91, 89, 90, 91, 92, 93, 95, 90, 94, 92, 91, 93],
    'North Assam': [85, 88, 82, 87, 86, 84, 83, 81, 85, 86, 89, 87, 84, 83, 85, 88, 84, 86, 87, 89],
    'South Assam': [70, 72, 74, 69, 71, 68, 73, 70, 72, 71, 69, 73, 74, 70, 71, 72, 71, 70, 68, 69],
    'East Assam': [78, 80, 77, 81, 79, 82, 83, 76, 78, 80, 79, 81, 82, 78, 80, 77, 79, 81, 83, 82],
    'West Assam': [65, 68, 66, 70, 67, 69, 71, 66, 68, 70, 67, 69, 71, 68, 70, 69, 67, 70, 66, 68]
}

data = list(assam_tea_data.values())
region_names = list(assam_tea_data.keys())

# Create the figure and axes for the boxplot
fig, ax = plt.subplots(1, 2, figsize=(15, 8), gridspec_kw={'width_ratios': [3, 1]})

# Box plot for tea quality scores
bplot = ax[0].boxplot(data, vert=False, patch_artist=True, notch=True,
                      boxprops=dict(facecolor='#F8B195', color='black'),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      flierprops=dict(markerfacecolor='grey', marker='o', markersize=5, linestyle='none'),
                      medianprops=dict(color='blue'))

colors = ['#FFC1C1', '#C1FFC1', '#C1C1FF', '#FFE4C4', '#E6E6FA', '#D8BFD8', '#FFFACD']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax[0].set_yticklabels(region_names, fontsize=10)
ax[0].set_xlabel('Quality Score', fontsize=12)
ax[0].set_title('Distribution of Tea Quality Scores\nAcross Regions of Assam', fontsize=14, fontweight='bold')
ax[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Comparative scatter plot with a fictional external factor (e.g., rainfall)
rainfall = [120, 110, 130, 140, 100, 125, 115]  # fictional data representing average rainfall
average_quality = [np.mean(scores) for scores in data]

ax[1].scatter(rainfall, average_quality, color=colors, s=100, edgecolor='black')
for i, txt in enumerate(region_names):
    ax[1].annotate(txt, (rainfall[i], average_quality[i]), fontsize=10)

ax[1].set_xlabel('Average Rainfall (cm)', fontsize=12)
ax[1].set_ylabel('Average Quality Score', fontsize=12)
ax[1].set_title('Rainfall vs. Quality Score', fontsize=12, fontweight='bold')
ax[1].grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()