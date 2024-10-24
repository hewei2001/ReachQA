import matplotlib.pyplot as plt
import numpy as np

# Neighborhoods in Cleanairville
neighborhoods = [
    "Downtown", "Suburbia", "Industrial Park", "Greenview", "Riverside", "Sunnyvale"
]

# PM2.5 concentration data (in micrograms per cubic meter) for each neighborhood
data = [
    [12, 14, 15, 13, 15, 17, 18, 14, 16, 17],
    [8, 9, 11, 10, 9, 12, 10, 8, 10, 9],
    [22, 25, 28, 27, 30, 29, 31, 32, 28, 26],
    [6, 7, 8, 7, 6, 5, 8, 7, 5, 6],
    [14, 15, 16, 15, 18, 19, 17, 16, 18, 17],
    [10, 12, 11, 13, 12, 14, 13, 11, 12, 10]
]

# Create the horizontal box chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the horizontal boxplot
bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, labels=neighborhoods, whis=1.5)

# Customizing the appearance of the boxplot
colors = plt.cm.plasma(np.linspace(0, 1, len(neighborhoods)))
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
# Whiskers and caps are paired, so we tile the colors to ensure every two elements share the same color
whisker_colors = np.repeat(colors, 2, axis=0)
for whisker, color in zip(bp['whiskers'], whisker_colors):
    whisker.set(color=color, linewidth=1.5)
for cap, color in zip(bp['caps'], whisker_colors):
    cap.set(color=color, linewidth=1.5)
for median in bp['medians']:
    median.set(color='black', linewidth=2)

# Adding titles and labels
ax.set_title("PM2.5 Concentration Levels Across Cleanairville Neighborhoods\n(Air Quality Index Study)", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("PM2.5 Concentration (\u03bcg/m\u00b3)", fontsize=12)
ax.set_ylabel("Neighborhood", fontsize=12)

# Adding gridlines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_facecolor('#f9f9f9')

# Customize tick parameters
ax.tick_params(axis='y', which='major', labelsize=11)
ax.tick_params(axis='x', which='major', labelsize=10)

# Set x-axis limits for better visualization
ax.set_xlim(0, 35)

# Add annotations for medians
for i, median in enumerate(bp['medians']):
    median_value = median.get_xdata()[1]
    ax.text(median_value, i + 1, f'{median_value:.1f}', va='center', ha='left', color='black', fontsize=10, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()