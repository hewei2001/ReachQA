import matplotlib.pyplot as plt
import numpy as np

# Listener numbers (in millions) for each platform over a few months
spotify_listeners = [78, 80, 82, 79, 84, 81, 85, 83, 82, 86, 87, 89]
apple_music_listeners = [55, 57, 56, 58, 60, 62, 59, 61, 60, 64, 63, 65]
amazon_music_listeners = [40, 39, 41, 43, 42, 44, 45, 46, 44, 43, 47, 48]
youtube_music_listeners = [68, 70, 69, 67, 71, 72, 70, 73, 74, 75, 72, 76]
tidal_listeners = [12, 13, 14, 13, 15, 14, 16, 15, 14, 17, 18, 16]

# Grouping the data together for plotting
platform_listener_data = [spotify_listeners, apple_music_listeners, amazon_music_listeners,
                          youtube_music_listeners, tidal_listeners]
platforms = ['Spotify', 'Apple Music', 'Amazon Music', 'YouTube Music', 'Tidal']

# Calculate percentage growth for each platform
def calculate_growth(data):
    return [((data[i] - data[i - 1]) / data[i - 1]) * 100 if i > 0 else 0 for i in range(len(data))]

growth_data = [calculate_growth(spotify_listeners), calculate_growth(apple_music_listeners),
               calculate_growth(amazon_music_listeners), calculate_growth(youtube_music_listeners),
               calculate_growth(tidal_listeners)]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))
fig.suptitle('Music Streaming Platform Listener Analysis', fontsize=16, fontweight='bold', y=1.02)

# First subplot: Box plot for listener numbers
boxes = axs[0].boxplot(platform_listener_data, vert=False, patch_artist=True, notch=True,
                       boxprops=dict(facecolor='lightblue', color='darkblue'),
                       whiskerprops=dict(color='darkblue', linestyle='--'),
                       capprops=dict(color='darkblue'),
                       flierprops=dict(marker='o', color='orange', alpha=0.5),
                       medianprops=dict(color='red'))

colors = ['#ffa07a', '#20b2aa', '#87cefa', '#db7093', '#d3d3d3']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_yticklabels(platforms)
axs[0].set_xlabel('Monthly Listener Numbers (in millions)', fontsize=12, fontweight='bold')
axs[0].set_title('Monthly Listener Trends Across Platforms', fontsize=14, fontweight='bold', pad=20)
axs[0].xaxis.grid(True, linestyle='--', alpha=0.7)

axs[0].annotate('Consistent growth in Spotify', xy=(88.5, 1), xytext=(91, 0.8),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

axs[0].annotate('Stable figures for Tidal', xy=(15, 5), xytext=(18, 4.5),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Second subplot: Line plot for growth rates
months = np.arange(1, 13)
for growth, platform, color in zip(growth_data, platforms, colors):
    axs[1].plot(months, growth, label=platform, marker='o', color=color)

axs[1].set_xlabel('Months', fontsize=12, fontweight='bold')
axs[1].set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
axs[1].set_title('Monthly Growth Rates', fontsize=14, fontweight='bold', pad=20)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(pad=3.0)
plt.show()