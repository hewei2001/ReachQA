import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects

# Define the e-commerce platforms and service aspects
platforms = ['Amazon', 'eBay', 'Alibaba', 'Walmart', 'Etsy']
service_aspects = ['Delivery', 'Quality', 'Support', 'Experience', 'Value']

# Ratings data
ratings_data = np.array([
    [4.5, 4.2, 4.0, 4.8, 4.3],  # Amazon
    [4.0, 4.1, 3.5, 4.2, 4.0],  # eBay
    [4.3, 4.5, 3.9, 4.5, 4.4],  # Alibaba
    [4.1, 4.0, 3.8, 4.4, 4.1],  # Walmart
    [4.2, 4.6, 4.3, 4.7, 4.5]   # Etsy
])

# Set up the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and positions
bar_width = 0.15
positions = np.arange(len(platforms))

# Improved color palette for enhanced visibility
colors = ['#4c72b0', '#dd8452', '#55a868', '#c44e52', '#8172b2']

# Plot each aspect as a series of bars
for idx, (aspect, color) in enumerate(zip(service_aspects, colors)):
    bars = ax.bar(positions + idx * bar_width, ratings_data[:, idx], bar_width,
                  label=aspect, color=color, edgecolor='gray', alpha=0.85)
    # Adding subtle shadows for 3D effect
    for bar in bars:
        bar.set_path_effects([path_effects.withStroke(linewidth=1, foreground='black')])

# Add labels and title with better positioning
ax.set_xlabel('E-commerce Platforms', fontsize=12, labelpad=10)
ax.set_ylabel('Satisfaction Rating (1 to 5)', fontsize=12, labelpad=10)
ax.set_title('Customer Satisfaction Ratings Across E-commerce Platforms\n' +
             'First Quarter 2023', fontsize=14, fontweight='bold', pad=15)
ax.set_xticks(positions + 2 * bar_width)
ax.set_xticklabels(platforms, fontsize=11, rotation=45, ha='right')

# Add legend with a slight inset and improved positioning
ax.legend(title='Service Aspects', loc='upper left', fontsize=10, bbox_to_anchor=(1.01, 1), borderaxespad=0.)

# Annotate each bar with the rating value
for i in range(len(platforms)):
    for j in range(len(service_aspects)):
        ax.text(i + j * bar_width, ratings_data[i, j] + 0.05, f'{ratings_data[i, j]:.1f}', 
                ha='center', va='bottom', fontsize=9, color='black')

# Highlight the highest rating in each platform with an annotation
highest_ratings = ratings_data.max(axis=1)
for i, pos in enumerate(positions):
    highest_idx = np.argmax(ratings_data[i])
    ax.annotate(f'Highest: {highest_ratings[i]:.1f}', 
                xy=(pos + highest_idx * bar_width, highest_ratings[i] + 0.1), 
                fontsize=9, color='darkred', weight='bold', ha='center', arrowprops=dict(arrowstyle='->', lw=1.5))

# Add grid lines with improved visibility
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Ensure the layout is tight and elements do not overlap
plt.tight_layout()

# Show the plot
plt.show()