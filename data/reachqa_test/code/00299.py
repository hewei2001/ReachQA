import matplotlib.pyplot as plt
import numpy as np

# Constructing rating data for each galactic cuisine
nebula_noodles = [3.5, 4.0, 4.2, 3.8, 4.5, 4.7, 3.9, 4.1, 4.3, 4.0]
cosmic_curry = [3.0, 3.2, 3.3, 3.1, 3.0, 3.4, 3.2, 3.1, 3.3, 3.5]
astro_appetizers = [4.0, 4.5, 4.7, 4.8, 4.9, 4.3, 4.6, 4.4, 4.5, 4.7]
meteor_munchies = [2.5, 2.8, 3.0, 3.1, 2.9, 3.0, 2.7, 3.2, 3.0, 3.1]
stellar_sweets = [4.1, 4.3, 4.5, 4.2, 4.7, 4.8, 4.6, 4.4, 4.5, 4.3]

# Combined data for plotting
data = [nebula_noodles, cosmic_curry, astro_appetizers, meteor_munchies, stellar_sweets]

# Define the plot
fig, ax = plt.subplots(figsize=(14, 8))
boxprops = dict(linestyle='-', linewidth=2, color='black')

# Plotting the box plot with horizontal orientation
bp = ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, notch=True, boxprops=boxprops)

# Customizing plot appearance
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Customizing other elements
for whisker, cap, flier, median, mean in zip(bp['whiskers'], bp['caps'], bp['fliers'], bp['medians'], bp['means']):
    whisker.set(color='gray', linewidth=1.5, linestyle='--')
    cap.set(color='gray', linewidth=1.5)
    flier.set(markerfacecolor='black', marker='o', alpha=0.5)
    median.set(color='yellow', linewidth=2)
    mean.set(marker='D', color='red', markersize=6)

# Adding a violin plot for better distribution visualization
parts = ax.violinplot(data, vert=False, showmeans=False, showmedians=False, showextrema=False)

for pc, color in zip(parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.2)

# Set cuisine labels on Y-axis
cuisine_labels = ['Nebula Noodles', 'Cosmic Curry', 'Astro Appetizers', 'Meteor Munchies', 'Stellar Sweets']
ax.set_yticks(np.arange(1, len(cuisine_labels) + 1))
ax.set_yticklabels(cuisine_labels)

# Set axis labels and title
ax.set_xlabel('Review Ratings (1 to 5 Stars)', fontsize=12)
ax.set_title('Galactic Culinary Reviews:\nA Flavored Journey Across the Stars', fontsize=16, fontweight='bold', pad=15)

# Highlighting the overall average rating
overall_avg_rating = 3.5
ax.axvline(x=overall_avg_rating, linestyle='--', color='blue', alpha=0.7, label=f'Overall Avg Rating: {overall_avg_rating}')
ax.legend(loc='lower right', fontsize=10)

# Customize the grid
ax.xaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()