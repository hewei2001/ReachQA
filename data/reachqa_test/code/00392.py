import matplotlib.pyplot as plt
import numpy as np

# Data preparation
music_streaming_services = ['Spotify', 'Apple Music', 'Amazon Music', 'TikTok Music', 'YouTube Music', 'Tidal', 'Deezer', 'Google Play Music', 'Pandora Radio', 'SoundCloud']
revenue = [11.8, 6.3, 5.5, 4.2, 3.5, 2.8, 2.3, 2.1, 1.8, 1.5]

# Reverse the lists to plot bars from largest to smallest
music_streaming_services = music_streaming_services[::-1]
revenue = revenue[::-1]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 10))

# Set background gradient
ax.set_facecolor('#f2f2f2')

# Plot horizontal bars
bar_height = np.arange(len(music_streaming_services))
ax.barh(bar_height, revenue, height=0.7, color=plt.cm.coolwarm(np.linspace(0, 1, len(music_streaming_services))))

# Set title and labels
ax.set_title("Top 10 Music Streaming Services by Revenue (2022)\nGlobal Market Share",
             fontsize=16, fontweight='bold', wrap=True)

ax.set_xlabel('Revenue (Billions USD)', fontsize=14, labelpad=10)
ax.set_ylabel('Music Streaming Service', fontsize=14, labelpad=10)

# Set y-axis ticks and labels
ax.set_yticks(bar_height)
ax.set_yticklabels(music_streaming_services, ha='right', fontsize=12)

# Add value labels on the end of each bar
for i, (x, y) in enumerate(zip(revenue, bar_height)):
    ax.text(x + 0.2, y, f'{x:.1f}', ha='left', va='center', fontsize=12)

# Add reference line for average revenue
avg_revenue = sum(revenue) / len(revenue)
ax.axvline(avg_revenue, color='gray', linestyle='--', linewidth=1, label=f'Average Revenue: {avg_revenue:.1f}')

# Set x-axis limits and grid
ax.set_xlim(0, max(revenue) + 2)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Legend for reference line
ax.legend(loc='upper right', fontsize=12)

# Layout adjustments
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Show the plot
plt.show()