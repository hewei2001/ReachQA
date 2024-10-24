import matplotlib.pyplot as plt
import numpy as np

# Artificial data for the number of different bird species spotted weekly in each park
greengrove = [15, 18, 20, 22]
sunnyvale = [25, 28, 30, 27]
oakwood = [10, 12, 14, 11]
meadowlark = [19, 22, 20, 21]

# List of data for the box plot
data = [greengrove, sunnyvale, oakwood, meadowlark]

# Creating a vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, patch_artist=True, notch=True, showmeans=True, meanline=True, widths=0.6)

# Define colors for each boxplot
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

# Customizing each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.2)

# Customizing the appearance of the means
for mean in bp['means']:
    mean.set(color='red', linewidth=1.2)

# Customizing the appearance of medians
for median in bp['medians']:
    median.set(color='black', linewidth=1.2)

# Customizing whiskers
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.2, linestyle='--')

# Customizing caps
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.2)

# Adding titles and labels
ax.set_title('Bird Species Diversity in Avianville Parks\nMonthly Observations', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Number of Bird Species', fontsize=12)
ax.set_xticklabels(['GreenGrove', 'SunnyVale', 'Oakwood', 'MeadowLark'], fontsize=12)

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a legend for clarity
legend_handles = [
    plt.Line2D([0], [0], color=color, lw=4, label=park) 
    for color, park in zip(colors, ['GreenGrove', 'SunnyVale', 'Oakwood', 'MeadowLark'])
]
legend_handles.append(plt.Line2D([0], [0], color='red', lw=2, label='Mean'))
ax.legend(handles=legend_handles, title='Parks', fontsize=10, loc='upper right', framealpha=0.5)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()