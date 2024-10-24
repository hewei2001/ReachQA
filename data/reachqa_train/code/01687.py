import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for coffee ratings
coffee_blends = ['Sumatran Bliss', 'Javanese Delight', 'Bali Blue Moon', 
                 'Sulawesi Serenity', 'Papua Paradise', 'Toraja Treasure', 
                 'Aceh Aroma', 'Lampung Luxury']

# Constructing more detailed data
ratings_data = [
    np.array([7.8, 8.0, 8.2, 8.5, 7.9, 8.1, 8.3, 7.8, 8.0, 8.2, 7.9, 8.1, 8.4, 8.6, 7.7]),
    np.array([6.5, 6.7, 6.8, 6.4, 6.6, 6.7, 6.9, 6.5, 6.8, 6.9, 6.6, 6.7, 6.5, 6.8, 6.4]),
    np.array([9.1, 9.0, 8.9, 9.2, 9.1, 9.3, 9.2, 9.0, 9.1, 9.2, 9.1, 9.3, 8.9, 9.0, 9.3]),
    np.array([8.0, 7.8, 7.9, 8.1, 8.3, 8.2, 8.0, 8.1, 7.9, 8.2, 7.7, 8.0, 8.2, 8.1, 7.8]),
    np.array([7.2, 7.1, 7.4, 7.0, 7.3, 7.5, 7.2, 7.1, 7.3, 7.4, 7.2, 7.5, 7.0, 7.3, 7.2]),
    np.array([8.5, 8.3, 8.7, 8.4, 8.6, 8.8, 8.5, 8.3, 8.7, 8.6, 8.5, 8.4, 8.6, 8.7, 8.4]),
    np.array([7.9, 7.8, 7.7, 8.0, 7.9, 8.1, 8.2, 8.0, 7.9, 7.8, 7.6, 7.9, 8.0, 8.1, 7.8]),
    np.array([8.6, 8.4, 8.5, 8.7, 8.9, 8.8, 8.7, 8.6, 8.5, 8.8, 8.9, 8.7, 8.5, 8.4, 8.9])
]

fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 2]})

# Box plot
box = axes[0].boxplot(ratings_data, patch_artist=True, notch=True, vert=True, showmeans=True)

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ff6666', '#99ffcc', '#ffb3e6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Box plot customization
axes[0].set_title('Gourmet Coffee Ratings in Cafés Across Java Island\nExploring Different Blends', fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel('Coffee Blend', fontsize=12)
axes[0].set_ylabel('Customer Rating (out of 10)', fontsize=12)
axes[0].set_xticks(np.arange(1, len(coffee_blends) + 1))
axes[0].set_xticklabels(coffee_blends, rotation=45, ha='right')

for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

# Custom legend
median_legend = plt.Line2D([0], [0], color='black', lw=2, label='Median')
mean_legend = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=8, label='Mean')
axes[0].legend(handles=[median_legend, mean_legend], loc='upper left')

# Density plot
for i, blend_ratings in enumerate(ratings_data):
    sns.kdeplot(blend_ratings, ax=axes[1], label=coffee_blends[i], color=colors[i], shade=True, alpha=0.6)

# Density plot customization
axes[1].set_title('Density Estimation of Coffee Ratings\nFor Different Blends', fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel('Customer Rating (out of 10)', fontsize=12)
axes[1].set_ylabel('Density', fontsize=12)
axes[1].legend(loc='upper left')

plt.tight_layout()
plt.show()