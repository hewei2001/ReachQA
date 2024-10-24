import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Data for plotting
genres = ['Action', 'Adventure', 'RPG', 'Simulation', 'Strategy']
daily_players = np.array([15.2, 8.6, 12.4, 5.8, 9.0])  # Average daily active players in millions

# Define a color map based on daily players
colors = cm.viridis(daily_players / max(daily_players))

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
y_positions = np.arange(len(genres))

# Plot the bars with a colormap and error bars for added complexity
error = np.array([0.5, 0.3, 0.4, 0.2, 0.3])
bars = ax.barh(y_positions, daily_players, xerr=error, color=colors, edgecolor='black', height=0.6)

# Add data labels to the end of each bar
for bar, value, err in zip(bars, daily_players, error):
    width = bar.get_width()
    ax.annotate(f'{width:.1f}M ±{err:.1f}', 
                xy=(width + err, bar.get_y() + bar.get_height() / 2),
                xytext=(10, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

# Average line
average_players = np.mean(daily_players)
ax.axvline(average_players, color='gray', linestyle='--', linewidth=1)
ax.text(average_players + 0.5, len(genres) - 1, f'Avg: {average_players:.1f}M', color='gray', fontsize=11)

# Customize the axis
ax.set_yticks(y_positions)
ax.set_yticklabels(genres, fontsize=12)
ax.invert_yaxis()

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set labels and title
ax.set_xlabel('Average Daily Active Players (in millions)', fontsize=12)
ax.set_title('Daily Engagement Across\nPopular Video Game Genres', fontsize=16, fontweight='bold', pad=20)

# Legend with colormap
sm = plt.cm.ScalarMappable(cmap=cm.viridis, norm=plt.Normalize(vmin=min(daily_players), vmax=max(daily_players)))
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Player Count', fontsize=12)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()