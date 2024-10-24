import matplotlib.pyplot as plt
import numpy as np

# Data for tome discoveries by decade and guild
bards_discoveries = [
    [15, 18, 20, 22, 17, 21],  # 1920s
    [25, 28, 30, 32, 27, 29],  # 1940s
    [35, 38, 40, 45, 37, 42],  # 1960s
    [50, 53, 55, 58, 52, 57],  # 1980s
    [70, 73, 75, 78, 72, 77]   # 2000s
]

monks_discoveries = [
    [12, 15, 10, 14, 16, 18],  # 1920s
    [22, 25, 20, 24, 26, 28],  # 1940s
    [32, 35, 30, 34, 36, 38],  # 1960s
    [42, 45, 40, 44, 46, 48],  # 1980s
    [62, 65, 60, 64, 66, 68]   # 2000s
]

# Prepare cumulative sum data for line plot
cumulative_bards = [sum(decade) for decade in bards_discoveries]
cumulative_monks = [sum(decade) for decade in monks_discoveries]

# Labels for the decades and guilds
decades = ['1920s', '1940s', '1960s', '1980s', '2000s']
guilds = ['Bards', 'Monks']

# Create the figure and axes
fig, ax = plt.subplots(1, 3, figsize=(18, 8), sharey=False, gridspec_kw={'width_ratios': [2, 2, 1]})

# Set colors for the guilds
colors = ['#7fc97f', '#beaed4']
titles = ["Bards' Discoveries by Decade", "Monks' Discoveries by Decade"]

# Create box plots for Bards and Monks
for i, (discoveries, color, title) in enumerate(zip([bards_discoveries, monks_discoveries], colors, titles)):
    boxplots = ax[i].boxplot(discoveries, vert=False, patch_artist=True, showmeans=True, notch=True, whis=[5, 95])
    ax[i].set_title(title, fontsize=14, pad=10)
    ax[i].set_xlabel('Number of Tomes Discovered', fontsize=12)
    for patch in boxplots['boxes']:
        patch.set_facecolor(color)
    for median in boxplots['medians']:
        median.set(color='orange', linewidth=2)
    for mean in boxplots['means']:
        mean.set(marker='o', color='red', markersize=5)
    for whisker in boxplots['whiskers']:
        whisker.set(color='blue', linestyle='--', linewidth=1.5)
    for cap in boxplots['caps']:
        cap.set(color='black', linewidth=1.5)
    ax[i].set_yticks(np.arange(1, len(decades) + 1))
    ax[i].set_yticklabels(decades, fontsize=12)
    ax[i].xaxis.grid(True, linestyle='--', alpha=0.7)

# Create a line plot for cumulative discoveries
ax[2].plot(decades, cumulative_bards, label='Bards', color='#7fc97f', marker='o')
ax[2].plot(decades, cumulative_monks, label='Monks', color='#beaed4', marker='o')
ax[2].set_title("Cumulative Discoveries by Decade", fontsize=14, pad=10)
ax[2].set_xlabel('Decades', fontsize=12)
ax[2].set_ylabel('Cumulative Discoveries', fontsize=12)
ax[2].legend(loc='upper left')
ax[2].grid(True, linestyle='--', alpha=0.7)

# Set a shared title for the plots
fig.suptitle("Bards vs. Monks: A Century of Tome Discoveries\nin the Kingdom of Lorethania", fontsize=16, fontweight='bold', y=0.98)

# Adjust layout to prevent text overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()