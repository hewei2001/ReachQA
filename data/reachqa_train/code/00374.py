import matplotlib.pyplot as plt

# Neighborhoods and their corresponding volunteering hours data
neighborhoods = ['Greenfield', 'Rivertown', 'Sunnydale', 'Hillcrest', 'Brookside']
volunteering_hours = [
    [2, 4, 6, 8, 12, 14, 16, 18, 20, 25],  # Greenfield
    [1, 3, 5, 10, 12, 14, 16, 19, 22],     # Rivertown
    [3, 5, 7, 10, 11, 13, 15, 17, 21, 23], # Sunnydale
    [2, 4, 9, 11, 12, 15, 17, 18, 19, 22], # Hillcrest
    [1, 5, 8, 10, 12, 14, 17, 18, 21]      # Brookside
]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Generate horizontal box plot
bp = ax.boxplot(volunteering_hours, vert=False, patch_artist=True, notch=True,
                meanline=True, showmeans=True, meanprops=dict(linestyle='-', linewidth=2, color='darkorange'))

# Customizing the appearance of the box plots
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.7)

# Customize whiskers, caps, medians, means
for whisker in bp['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")

for cap in bp['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in bp['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp['means']:
    mean.set(marker='o', markerfacecolor='darkorange', markersize=8)

# Add title and labels
ax.set_title('Community Engagement in Volunteering Initiatives\nAcross Neighborhoods', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours Volunteered', fontsize=13)
ax.set_yticklabels(neighborhoods, fontsize=12)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend to denote mean and median
mean_legend = plt.Line2D([], [], color='darkorange', marker='o', linestyle='None', markersize=8, label='Mean')
median_legend = plt.Line2D([], [], color='blue', linestyle='-', linewidth=2, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='lower right')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()