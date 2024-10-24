import numpy as np
import matplotlib.pyplot as plt

# Define the sectors in the Martian colony
sectors = ['Agriculture', 'Research', 'Engineering', 'Entertainment']

# Data for hours spent on work and leisure for each sector
data = {
    'Agriculture': [45, 50, 52, 48, 49, 55, 47, 51, 50, 53],
    'Research': [40, 42, 39, 43, 41, 44, 38, 40, 42, 39],
    'Engineering': [50, 55, 53, 52, 56, 54, 51, 52, 55, 53],
    'Entertainment': [35, 36, 34, 38, 37, 39, 35, 34, 36, 35]
}

# Calculate average hours for each sector
average_hours = [np.mean(hours) for hours in data.values()]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Box plot in the first subplot
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
bp = axs[0].boxplot(data.values(), vert=False, patch_artist=True, notch=True,
                    boxprops=dict(facecolor='c', color='navy'),
                    whiskerprops=dict(color='navy'),
                    capprops=dict(color='navy'),
                    flierprops=dict(markerfacecolor='red', marker='o', color='navy'),
                    medianprops=dict(color='orange'))

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Titles, labels, and grid for the first plot
axs[0].set_title("Productivity and Leisure Balance\nin a Futuristic Martian Colony", fontsize=14, fontweight='bold', pad=20)
axs[0].set_xlabel("Weekly Hours", fontsize=12)
axs[0].set_yticks(np.arange(1, len(sectors) + 1))
axs[0].set_yticklabels(sectors, fontsize=11)
axs[0].xaxis.grid(True, linestyle='--', alpha=0.6)
axs[0].set_xlim(30, 60)

# Bar chart in the second subplot
bars = axs[1].barh(sectors, average_hours, color=colors, edgecolor='navy', height=0.5)

# Titles and labels for the second plot
axs[1].set_title("Average Weekly Hours Across Sectors", fontsize=14, fontweight='bold', pad=20)
axs[1].set_xlabel("Average Hours", fontsize=12)
axs[1].set_xlim(30, 60)

# Annotate bar chart with average hours
for bar, avg_hour in zip(bars, average_hours):
    axs[1].text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{avg_hour:.1f}',
                va='center', ha='left', color='navy', fontsize=11)

# Shared legend
legend_labels = ['Interquartile Range', 'Whiskers', 'Outliers', 'Median']
legend_patches = [plt.Line2D([0], [0], color=color, lw=2, marker='s', markersize=10, label=label)
                  for color, label in zip(['#66b3ff', 'navy', 'red', 'orange'], legend_labels)]
fig.legend(handles=legend_patches, title='Box Plot Elements', fontsize=10, loc='upper right')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()