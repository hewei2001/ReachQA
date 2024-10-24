import matplotlib.pyplot as plt
import numpy as np

# Fictional directors and their annual box office revenues in millions
directors = ['Ava Silverstone', 'Liam Channing', 'Nina Trevors', 'Zeke Grant', 'Olivia Raine']

# Box office data for each director across multiple films over the last three years
ava_revenues = [120, 135, 95, 105, 140, 115, 125]
liam_revenues = [110, 125, 130, 100, 115, 90, 95]
nina_revenues = [150, 160, 145, 170, 155, 165, 150]
zeke_revenues = [130, 120, 125, 140, 135, 110, 100]
olivia_revenues = [140, 155, 135, 145, 150, 160, 145]

# Collate data into a single list for box plot
data = [ava_revenues, liam_revenues, nina_revenues, zeke_revenues, olivia_revenues]

# Calculate average revenue for each director
average_revenues = [np.mean(ava_revenues), np.mean(liam_revenues), np.mean(nina_revenues),
                    np.mean(zeke_revenues), np.mean(olivia_revenues)]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Box plot on the left
boxprops = dict(facecolor='skyblue', color='darkblue')
medianprops = dict(color='firebrick', linewidth=2)
whiskerprops = dict(color='darkblue', linestyle='--')

axes[0].boxplot(data, labels=directors, patch_artist=True, notch=True,
                boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops)

axes[0].set_title("Box Office Performance of Fictional Directors:\nAnnual Gross Revenue Impact (2019-2021)",
                  fontsize=14, weight='bold', pad=20)
axes[0].set_xlabel("Directors", fontsize=12)
axes[0].set_ylabel("Gross Revenue (in Millions)", fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar chart on the right
bar_colors = ['#add8e6', '#87cefa', '#4682b4', '#5f9ea0', '#00ced1']
axes[1].bar(directors, average_revenues, color=bar_colors, edgecolor='black')

# Adding individual values on the bars
for i, revenue in enumerate(average_revenues):
    axes[1].text(i, revenue + 1, f'{revenue:.1f}', ha='center', va='bottom', fontweight='bold')

axes[1].set_title("Average Annual Revenue per Director (2019-2021)", fontsize=14, weight='bold', pad=20)
axes[1].set_xlabel("Directors", fontsize=12)
axes[1].set_ylabel("Average Revenue (in Millions)", fontsize=12)

# Improve spacing
plt.tight_layout()

# Display the charts
plt.show()