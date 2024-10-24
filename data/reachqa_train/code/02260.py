import matplotlib.pyplot as plt
import numpy as np

# Define the music streaming platforms and their market share percentages
platforms = ['Spotify', 'Apple Music', 'Amazon Music', 'YouTube Music', 'Tidal']
market_share = [32, 24, 18, 16, 10]

# Define colors for each platform
colors = ['#1DB954', '#FA233B', '#FF9900', '#FF0000', '#002B7F']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate positions for the bars
x_pos = np.arange(len(platforms))

# Plot the bar chart
bars = ax.bar(x_pos, market_share, color=colors, alpha=0.8, width=0.6)

# Set the title and labels
ax.set_title('Market Share of Music Streaming Platforms\nin 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Streaming Platforms', fontsize=14)
ax.set_ylabel('Market Share (%)', fontsize=14)
ax.set_xticks(x_pos)
ax.set_xticklabels(platforms, fontsize=12, rotation=15)

# Add text annotations on top of each bar for clarity
for bar, share in zip(bars, market_share):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{share}%', ha='center', va='bottom', fontsize=12)

# Add grid lines along the y-axis for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent text overlap
plt.tight_layout()

# Show the plot
plt.show()