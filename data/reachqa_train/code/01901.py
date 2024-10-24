import matplotlib.pyplot as plt
import numpy as np

# Define the fashion styles and months
styles = ['Minimalist', 'Streetwear', 'Vintage', 'Bohemian', 'Athleisure', 'Gothic']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Engagement rates (manually constructed data)
engagement_rates = np.array([
    [65, 70, 68, 75, 80, 85, 90, 88, 83, 78, 72, 68],  # Minimalist
    [72, 77, 75, 82, 88, 92, 95, 93, 87, 83, 78, 74],  # Streetwear
    [60, 65, 63, 67, 70, 76, 80, 78, 74, 70, 66, 63],  # Vintage
    [58, 62, 60, 65, 68, 72, 76, 73, 70, 66, 62, 60],  # Bohemian
    [70, 75, 73, 78, 82, 87, 90, 89, 84, 79, 74, 71],  # Athleisure
    [50, 55, 53, 57, 60, 65, 68, 66, 61, 58, 54, 51]   # Gothic
])

# Calculate the average engagement rate for all styles per month
average_engagement = np.mean(engagement_rates, axis=0)

# Setup figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
fig.suptitle('Fashion Trends Analysis\nEngagement Rates and Trends', fontsize=16, fontweight='bold')

# Plot heatmap
heatmap = axes[0].imshow(engagement_rates, cmap='YlGnBu', aspect='auto', interpolation='nearest')
cbar = fig.colorbar(heatmap, ax=axes[0])
cbar.set_label('Engagement Level\n(Scale 1-100)', fontsize=10)

axes[0].set_title('Engagement Rates by Style and Month', fontsize=12)
axes[0].set_xlabel('Month', fontsize=10)
axes[0].set_ylabel('Fashion Style', fontsize=10)
axes[0].set_xticks(np.arange(len(months)))
axes[0].set_xticklabels(months, fontsize=8, rotation=45)
axes[0].set_yticks(np.arange(len(styles)))
axes[0].set_yticklabels(styles, fontsize=8)

for i in range(len(styles)):
    for j in range(len(months)):
        axes[0].text(j, i, f"{engagement_rates[i, j]}", ha='center', va='center', color='black', fontsize=7)

# Plot line chart for average engagement trends
axes[1].plot(months, average_engagement, marker='o', color='orange', linewidth=2, label='Average Engagement')
axes[1].set_title('Average Engagement Trend Across Styles', fontsize=12)
axes[1].set_xlabel('Month', fontsize=10)
axes[1].set_ylabel('Average Engagement Level', fontsize=10)
axes[1].set_xticks(np.arange(len(months)))
axes[1].set_xticklabels(months, fontsize=8, rotation=45)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(fontsize=9)
axes[1].set_ylim(60, 95)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make space for the common title

# Display the plot
plt.show()