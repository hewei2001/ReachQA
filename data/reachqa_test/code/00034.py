import matplotlib.pyplot as plt
import numpy as np

# Original data for the box plot
apple_yields = [80, 95, 110, 120, 85, 90, 130, 125, 100, 105]
banana_yields = [150, 160, 155, 165, 170, 162, 158, 172, 175, 168]
orange_yields = [65, 70, 75, 80, 68, 72, 78, 82, 77, 74]
strawberry_yields = [40, 45, 50, 42, 48, 47, 49, 51, 44, 46]
grapes_yields = [90, 95, 88, 92, 94, 89, 91, 93, 97, 96]

# Related but distinct data for bar plot
years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
apple_annual = [530, 570, 600, 650, 640]
banana_annual = [1300, 1350, 1400, 1450, 1420]
orange_annual = [720, 740, 760, 780, 750]
strawberry_annual = [440, 450, 460, 480, 470]
grapes_annual = [900, 950, 940, 920, 910]

# Creating subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Box plot
box = axs[0].boxplot([apple_yields, banana_yields, orange_yields, strawberry_yields, grapes_yields],
                     patch_artist=True, labels=['Apples', 'Bananas', 'Oranges', 'Strawberries', 'Grapes'],
                     notch=True, flierprops=dict(marker='o', color='red', markersize=6))

colors = ['#FF9999', '#FFE066', '#99FF99', '#FFCCCC', '#CCCCFF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['whiskers'], color='black', linewidth=1.5, linestyle='--')
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['medians'], color='blue', linewidth=2)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)
axs[0].set_title('Distribution of Annual Fruit Harvest Yields\nAcross Regions', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Type of Fruit', fontsize=12)
axs[0].set_ylabel('Harvest Yield (in tons)', fontsize=12)

# Bar plot
x = np.arange(len(years))
bar_width = 0.15

axs[1].bar(x - 2*bar_width, apple_annual, width=bar_width, color='#FF9999', label='Apples')
axs[1].bar(x - bar_width, banana_annual, width=bar_width, color='#FFE066', label='Bananas')
axs[1].bar(x, orange_annual, width=bar_width, color='#99FF99', label='Oranges')
axs[1].bar(x + bar_width, strawberry_annual, width=bar_width, color='#FFCCCC', label='Strawberries')
axs[1].bar(x + 2*bar_width, grapes_annual, width=bar_width, color='#CCCCFF', label='Grapes')

axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Total Annual Yield (in tons)', fontsize=12)
axs[1].set_title('Total Annual Yields\nOver 5 Years', fontsize=14, fontweight='bold')
axs[1].set_xticks(x)
axs[1].set_xticklabels(years)
axs[1].legend(title='Fruit Type', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.show()