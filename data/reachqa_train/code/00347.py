import matplotlib.pyplot as plt
import numpy as np

# Data for time allocation in weeks for each development phase
indie_games = {
    "Planning": [4, 5, 6, 3, 5],
    "Development": [20, 22, 25, 18, 21],
    "Testing": [8, 10, 9, 7, 8],
    "Marketing": [5, 4, 6, 7, 5]
}

major_games = {
    "Planning": [6, 7, 8, 5, 6],
    "Development": [30, 28, 32, 35, 31],
    "Testing": [12, 15, 11, 13, 14],
    "Marketing": [10, 12, 11, 9, 10]
}

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Plot horizontal box plots for indie games
indie_box = ax.boxplot(indie_games.values(), vert=False, positions=range(1, 5), widths=0.35,
                       patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'),
                       whiskerprops=dict(color='blue'), capprops=dict(color='blue'),
                       medianprops=dict(color='darkblue'), flierprops=dict(markerfacecolor='blue', marker='o'))

# Plot horizontal box plots for major games
major_box = ax.boxplot(major_games.values(), vert=False, positions=[x + 0.4 for x in range(1, 5)], widths=0.35,
                       patch_artist=True, boxprops=dict(facecolor='lightcoral', color='red'),
                       whiskerprops=dict(color='red'), capprops=dict(color='red'),
                       medianprops=dict(color='darkred'), flierprops=dict(markerfacecolor='red', marker='o'))

# Add gridlines
ax.xaxis.grid(True, linestyle='--', which='both', color='grey', alpha=0.7)

# Add annotations for medians
for i, median in enumerate(indie_box['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{x_median:.1f}', xy=(x_median, y_median), xytext=(5, -5), 
                textcoords='offset points', color='darkblue', fontsize=10)

for i, median in enumerate(major_box['medians']):
    x_median = median.get_xdata()[1]
    y_median = median.get_ydata()[1]
    ax.annotate(f'{x_median:.1f}', xy=(x_median, y_median), xytext=(5, -5), 
                textcoords='offset points', color='darkred', fontsize=10)

# Customize plot labels and title
ax.set_yticks([1.2, 2.2, 3.2, 4.2])
ax.set_yticklabels(["Planning", "Development", "Testing", "Marketing"], fontsize=12)
ax.set_xlabel('Time in Weeks', fontsize=14)
ax.set_title("Time Allocation in Video Game Development Phases:\nIndie vs. Major Studios\nWith Medians Highlighted", 
             fontsize=16, fontweight='bold')

# Add a legend
colors = ["lightblue", "lightcoral"]
labels = ["Indie Studios", "Major Studios"]
handles = [plt.Line2D([0], [0], color=colors[i], lw=4, label=labels[i]) for i in range(len(labels))]
ax.legend(handles=handles, title='Studio Type', loc='upper right', fontsize=10, title_fontsize=12)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()