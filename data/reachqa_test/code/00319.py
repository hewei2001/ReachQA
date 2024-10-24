import matplotlib.pyplot as plt
import numpy as np

# Cooking times in minutes for various dishes from different cuisines
italian_times = [30, 45, 25, 60, 50, 40]
chinese_times = [20, 35, 25, 50, 45, 30]
indian_times = [45, 60, 70, 55, 50, 65]
mexican_times = [25, 30, 40, 35, 50, 45]
mediterranean_times = [30, 40, 35, 45, 55, 50]

# Additional data for average preparation time for each cuisine
prep_times = [10, 8, 15, 12, 9]

# Aggregate data for the box plot
cuisine_times = [italian_times, chinese_times, indian_times, mexican_times, mediterranean_times]
cuisine_labels = ['Italian', 'Chinese', 'Indian', 'Mexican', 'Mediterranean']

# Calculate average cooking times
avg_times = [np.mean(times) for times in cuisine_times]

# Create the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Box plot for cooking times
bp = ax1.boxplot(cuisine_times, vert=False, patch_artist=True, labels=cuisine_labels, notch=True)
colors = ['#FFA07A', '#8FBC8F', '#FFD700', '#CD5C5C', '#4682B4']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Customize the boxplot
for whisker in bp['whiskers']:
    whisker.set(color='grey', linewidth=1.5)
for cap in bp['caps']:
    cap.set(color='grey', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkred', linewidth=1.5)

# Annotate average cooking time
for i, avg in enumerate(avg_times):
    ax1.text(avg + 1, i + 1, f'Avg: {avg:.1f} mins', verticalalignment='center', fontsize=10, color='black')

ax1.set_title('Exploration of Global Cuisine:\nCooking Time Distribution', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Cooking Time (Minutes)', fontsize=12)
ax1.set_ylabel('Cuisines', fontsize=12)
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Bar plot for average preparation times
ax2.bar(cuisine_labels, prep_times, color=colors, alpha=0.7)
ax2.set_title('Average Preparation Time\nAcross Different Cuisines', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Cuisines', fontsize=12)
ax2.set_ylabel('Preparation Time (Minutes)', fontsize=12)
for i, prep_time in enumerate(prep_times):
    ax2.text(i, prep_time + 0.5, f'{prep_time} mins', ha='center', fontsize=10, color='black')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()