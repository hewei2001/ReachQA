import matplotlib.pyplot as plt
import numpy as np

# Define game genres
genres = ['FPS: First-Person Shooter', 'RPG: Role-Playing Game', 'RTS: Real-Time Strategy', 'Sports Game']

# FPS data for each genre
fps_data = [
    [58, 61, 59, 62, 70, 65, 56, 60, 63, 67],  # FPS: Tight consistency
    [44, 50, 47, 51, 49, 54, 45, 48, 53, 50],  # RPG: Higher variability
    [72, 75, 73, 72, 76, 73, 78, 71, 79, 74],  # RTS: Generally high FPS
    [66, 69, 71, 67, 65, 69, 70, 68, 72, 70]   # Sports: Consistent FPS
]

# Construct average FPS data for different settings (Low, Medium, High)
fps_settings = {
    'Low': [65, 55, 80, 68],
    'Medium': [60, 50, 75, 66],
    'High': [55, 45, 70, 62]
}

# Setup the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# First subplot: Box plot for FPS data
boxplots = ax1.boxplot(fps_data, vert=True, patch_artist=True, notch=True, showmeans=True)
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_title('Frame Rate Analysis\nAcross Game Genres', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Game Genres', fontsize=12)
ax1.set_ylabel('Frames Per Second (FPS)', fontsize=12)
ax1.set_xticks(np.arange(1, len(genres) + 1))
ax1.set_xticklabels(genres, rotation=15, ha='right', fontsize=10, fontweight='bold')

# Second subplot: Bar plot for average FPS at different settings
x = np.arange(len(genres))
width = 0.2

low_bars = ax2.bar(x - width, fps_settings['Low'], width, label='Low', color='#FFD700')
medium_bars = ax2.bar(x, fps_settings['Medium'], width, label='Medium', color='#87CEFA')
high_bars = ax2.bar(x + width, fps_settings['High'], width, label='High', color='#32CD32')

ax2.set_title('Average FPS at Different Graphics Settings', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Game Genres', fontsize=12)
ax2.set_ylabel('Average FPS', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels([genre.split(':')[0] for genre in genres], rotation=15, ha='right', fontsize=10, fontweight='bold')
ax2.legend(title="Settings", fontsize=10)

# Adjust layout for clarity and readability
plt.tight_layout()

# Display the plot
plt.show()