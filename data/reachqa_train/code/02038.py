import matplotlib.pyplot as plt
import numpy as np

# Define age groups
age_groups = ['Children', 'Teenagers', 'Young Adults', 'Adults', 'Seniors']

# Artificial data for weekly hours dedicated to arts and culture activities
children_hours = [4, 5, 7, 6, 8, 5, 9, 10, 11, 7]
teenagers_hours = [3, 4, 5, 5, 6, 7, 8, 5, 4, 6]
young_adults_hours = [2, 2, 3, 4, 5, 3, 4, 3, 3, 4]
adults_hours = [1, 1, 2, 3, 1, 2, 3, 1, 1, 2]
seniors_hours = [3, 4, 5, 4, 5, 4, 4, 6, 5, 5]

# Combine data into a list
arts_data = [children_hours, teenagers_hours, young_adults_hours, adults_hours, seniors_hours]

# Additional dataset for physical activities (for the second subplot)
children_physical = [3, 2, 4, 3, 4, 2, 5, 6, 5, 3]
teenagers_physical = [4, 5, 6, 5, 5, 6, 6, 6, 5, 6]
young_adults_physical = [3, 4, 4, 5, 6, 5, 5, 4, 4, 5]
adults_physical = [2, 3, 2, 3, 2, 2, 3, 3, 3, 3]
seniors_physical = [2, 3, 3, 3, 3, 3, 3, 3, 3, 4]

# Calculate average hours for physical activities
physical_avg = [
    np.mean(children_physical),
    np.mean(teenagers_physical),
    np.mean(young_adults_physical),
    np.mean(adults_physical),
    np.mean(seniors_physical)
]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# First subplot: Box plot for arts and culture activities
box = axs[0].boxplot(arts_data, vert=True, patch_artist=True, notch=True,
                     boxprops=dict(facecolor='#ffcc99', color='navy', alpha=0.7),
                     whiskerprops=dict(color='navy'),
                     capprops=dict(color='navy'),
                     medianprops=dict(color='red', linewidth=2),
                     flierprops=dict(marker='o', color='orange', alpha=0.5))

axs[0].set_title("Weekly Hours Dedicated to Arts and Culture\nActivities by Age Group",
                 fontsize=16, fontweight='bold', pad=15)
axs[0].set_xlabel('Age Groups', fontsize=14)
axs[0].set_ylabel('Weekly Hours', fontsize=14)
axs[0].set_xticklabels(age_groups, fontsize=12)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_facecolor('#f0f0f0')

# Annotate medians on the box plot
for i, line in enumerate(box['medians']):
    x, y = line.get_xydata()[1]  # top of median line
    axs[0].text(x, y, f'{y:.1f}', horizontalalignment='center',
                verticalalignment='bottom', fontsize=10, fontweight='bold',
                color='black', backgroundcolor='white')

# Second subplot: Bar plot for physical activity averages
axs[1].bar(age_groups, physical_avg, color='#99ccff', edgecolor='black', alpha=0.7)
axs[1].set_title("Average Weekly Hours for Physical Activities\nby Age Group",
                 fontsize=16, fontweight='bold', pad=15)
axs[1].set_xlabel('Age Groups', fontsize=14)
axs[1].set_ylabel('Average Weekly Hours', fontsize=14)
axs[1].set_xticklabels(age_groups, fontsize=12, rotation=45)
axs[1].set_facecolor('#f0f0f0')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()