import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
genres = ['Action', 'Adventure', 'RPG', 'Simulation', 'Strategy']
daily_players = [15.2, 8.6, 12.4, 5.8, 9.0]  # Average daily active players in millions

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))
y_positions = np.arange(len(genres))

# Plot the bars
bars = ax.barh(y_positions, daily_players, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], edgecolor='black', height=0.6)

# Add data labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width:.1f}', xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

# Customize the axis
ax.set_yticks(y_positions)
ax.set_yticklabels(genres, fontsize=12)
ax.invert_yaxis()  # Highest values at the top

# Set labels and title
ax.set_xlabel('Average Daily Active Players (in millions)', fontsize=12)
ax.set_title('Daily Engagement Across\nPopular Video Game Genres', fontsize=16, fontweight='bold', loc='center', pad=20)

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()