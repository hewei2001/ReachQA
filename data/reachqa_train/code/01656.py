import matplotlib.pyplot as plt

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

# Creating the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting
boxes = ax.boxplot(platform_listener_data, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightblue', color='darkblue'),
                   whiskerprops=dict(color='darkblue', linestyle='--'),
                   capprops=dict(color='darkblue'),
                   flierprops=dict(marker='o', color='orange', alpha=0.5),
                   medianprops=dict(color='red'))

# Customizing box colors for differentiation
colors = ['#ffa07a', '#20b2aa', '#87cefa', '#db7093', '#d3d3d3']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Customizing the plot
ax.set_yticklabels(platforms)
ax.set_xlabel('Monthly Listener Numbers (in millions)', fontsize=12, fontweight='bold')
ax.set_title('Monthly Listener Trends\nAcross Music Streaming Services', fontsize=16, fontweight='bold', pad=20)

# Adding grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adding annotations for special insights
ax.annotate('Consistent growth in Spotify', xy=(88.5, 1), xytext=(91, 0.8),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

ax.annotate('Stable figures for Tidal', xy=(15, 5), xytext=(18, 4.5),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to fit the elements and avoid overlapping
plt.tight_layout()

# Show the plot
plt.show()