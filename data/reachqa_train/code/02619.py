import matplotlib.pyplot as plt
import numpy as np

# Define countries and consumption categories
countries = ['Italy', 'USA', 'Japan', 'Brazil', 'India', 'Germany']
categories = ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly']

# Construct data reflecting fictional coffee consumption patterns (in thousands)
# Additional data introduces more complexity
coffee_data = {
    'Italy': [800, 150, 50, 20, 10],
    'USA': [400, 300, 100, 50, 25],
    'Japan': [150, 350, 200, 100, 50],
    'Brazil': [700, 200, 100, 40, 20],
    'India': [300, 250, 150, 70, 35],
    'Germany': [600, 250, 120, 60, 30]
}

# Colors for each category
category_colors = ['#d62728', '#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

# Prepare data for box and violin plot
data_for_box = [coffee_data[country] for country in countries]

# Create figure and axes for multiple plots
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Box Plot
box = axs[0].boxplot(data_for_box, patch_artist=True, labels=countries, notch=True, vert=True)

for patch, color in zip(box['boxes'], category_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle='--')

for cap in box['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

axs[0].yaxis.grid(True, linestyle='--', alpha=0.6, color='gray')
axs[0].set_xticklabels(countries, fontsize=10, fontweight='bold')
axs[0].set_yticks(np.arange(0, 901, 100))
axs[0].set_ylabel('Number of Coffee Drinkers (in thousands)', fontsize=10, fontweight='bold')
axs[0].set_title("Global Coffee Consumption Patterns:\nDiverse Habits Across Various Countries", 
                 fontsize=12, fontweight='bold', ha='center')

# Add legend for categories
legend_labels = categories
legend_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in category_colors]
axs[0].legend(legend_patches, legend_labels, loc='upper right', fontsize=10, frameon=False)

# Violin Plot with Dual Axis
data_for_violin = np.array(data_for_box).T
violin_parts = axs[1].violinplot(data_for_violin, vert=False, showmeans=True, showmedians=False)

# Set colors for violin parts
for i, pc in enumerate(violin_parts['bodies']):
    pc.set_facecolor(category_colors[i % len(category_colors)])
    pc.set_alpha(0.7)

for partname in ('cmeans', 'cmaxes', 'cmins'):
    vp = violin_parts[partname]
    vp.set_edgecolor('gray')
    vp.set_linewidth(1.5)
    vp.set_linestyle('--')

axs[1].set_yticks(range(1, len(categories) + 1))
axs[1].set_yticklabels(categories, fontsize=10, fontweight='bold')
axs[1].set_xticks(np.arange(0, 901, 100))
axs[1].set_xlabel('Number of Coffee Drinkers (in thousands)', fontsize=10, fontweight='bold')
axs[1].set_title("Coffee Consumption Density by Category", fontsize=12, fontweight='bold')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()