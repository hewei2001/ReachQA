import matplotlib.pyplot as plt
import numpy as np

# Define detailed age groups and more streaming platforms
age_groups = [
    'Early Gen Z (10-18)', 'Late Gen Z (19-24)', 
    'Young Millennials (25-34)', 'Older Millennials (35-44)', 
    'Gen X (45-54)', 'Young Baby Boomers (55-64)', 
    'Older Baby Boomers (65-74)'
]
platforms = ['Spotify', 'Apple Music', 'Amazon Music', 'Tidal', 'YouTube Music', 'Pandora', 'Deezer', 'SoundCloud']

# Define a complex percentage distribution for each age group and platform
platform_data = np.array([
    [30, 10, 5, 2, 20, 5, 15, 13],  # Early Gen Z
    [28, 14, 6, 3, 25, 6, 10, 8],   # Late Gen Z
    [25, 20, 10, 4, 18, 12, 5, 6],  # Young Millennials
    [18, 25, 15, 5, 15, 12, 5, 5],  # Older Millennials
    [15, 15, 25, 10, 15, 10, 5, 5], # Gen X
    [10, 10, 30, 12, 10, 12, 8, 8], # Young Baby Boomers
    [5, 5, 35, 15, 10, 15, 5, 10]   # Older Baby Boomers
])

# Positions for each group of bars
x = np.arange(len(age_groups))
bar_width = 0.7

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each platform's data as a stacked bar chart
bottom_heights = np.zeros(len(age_groups))
colors = [
    '#1DB954', '#FA1E44', '#FF9900', '#00CCFF', '#FF0000', 
    '#9467BD', '#8C564B', '#E377C2'
]

for idx, platform in enumerate(platforms):
    ax.bar(x, platform_data[:, idx], bottom=bottom_heights, width=bar_width, label=platform, color=colors[idx])
    bottom_heights += platform_data[:, idx]

# Add labels and title
ax.set_title("Digital Music Streaming Preferences Across Detailed Age Groups", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Age Groups", fontsize=12)
ax.set_ylabel("Usage Percentage (%)", fontsize=12)

# Set x-ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(age_groups, fontsize=10, rotation=45, ha='right')

# Add a legend with title
ax.legend(title='Music Platforms', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

# Configure gridlines
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Display percentage labels on the bars
for i in range(len(age_groups)):
    cumulative_height = 0
    for j in range(len(platforms)):
        percentage = platform_data[i, j]
        ax.text(i, cumulative_height + percentage / 2, f'{percentage}%', ha='center', va='center', color='white', fontsize=8)
        cumulative_height += percentage

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()