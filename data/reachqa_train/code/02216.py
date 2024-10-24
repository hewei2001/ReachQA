import matplotlib.pyplot as plt
import numpy as np

# Define the decades from the 1980s to the 2020s
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Streaming data for each genre in millions
classical = np.array([15, 20, 22, 24, 28])
jazz = np.array([25, 30, 28, 22, 18])
rock = np.array([30, 40, 35, 30, 25])
hip_hop = np.array([5, 10, 25, 40, 50])
electronic = np.array([2, 5, 15, 30, 45])

# Compute total streams and percentage change for each genre
total_streams = classical + jazz + rock + hip_hop + electronic
percentage_change = {
    'Classical': np.diff(classical) / classical[:-1] * 100,
    'Jazz': np.diff(jazz) / jazz[:-1] * 100,
    'Rock': np.diff(rock) / rock[:-1] * 100,
    'Hip-Hop': np.diff(hip_hop) / hip_hop[:-1] * 100,
    'Electronic': np.diff(electronic) / electronic[:-1] * 100
}

# Prepare subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Stacked area plot
axs[0].stackplot(decades, classical, jazz, rock, hip_hop, electronic,
                 labels=['Classical', 'Jazz', 'Rock', 'Hip-Hop', 'Electronic'],
                 colors=['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99'],
                 alpha=0.8)
axs[0].set_title('Evolution of Music Streaming Preferences\nfrom the 1980s to the 2020s', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Decade', fontsize=12)
axs[0].set_ylabel('Streams (Millions)', fontsize=12)
axs[0].legend(loc='upper left', title='Music Genres')
axs[0].set_xticks(decades)
axs[0].set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Line plot showing percentage change
for genre, change in percentage_change.items():
    axs[1].plot(decades[1:], change, marker='o', label=genre)

axs[1].set_title('Percentage Change in Music Streaming by Genre\n(per Decade)', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Decade', fontsize=12)
axs[1].set_ylabel('Percentage Change (%)', fontsize=12)
axs[1].legend(loc='upper right')
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].set_xticks(decades[1:])
axs[1].set_xticklabels([f"{decade}s" for decade in decades[1:]], fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()