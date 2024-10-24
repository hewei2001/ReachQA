import matplotlib.pyplot as plt
import numpy as np

# Original data representing average annual revenue in million USD for each genre
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Science Fiction']
revenues = [550, 400, 300, 200, 450]

# Constructing data for overlay plot: Revenue growth rates in percentage
growth_rates = [5.2, 3.8, 4.0, 2.5, 4.5]

# Define colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFA833']

# Create the figure and primary y-axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot the horizontal bar chart
bars = ax1.barh(genres, revenues, color=colors, edgecolor='black', height=0.6)
ax1.set_xlabel('Average Annual Revenue (Million USD)', fontsize=12)
ax1.set_title('Annual Revenue and Growth Rate of Movie Genres\nA Comprehensive Look at the 2020s Film Industry', fontsize=14, fontweight='bold', pad=20)

# Secondary y-axis for growth rates
ax2 = ax1.twiny()
ax2.plot(growth_rates, genres, 'go--', marker='o', label='Growth Rate (%)')
ax2.set_xlabel('Annual Revenue Growth Rate (%)', fontsize=12)

# Add value labels to bars
for bar, revenue in zip(bars, revenues):
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{revenue}M', va='center', fontsize=10, color='black', fontweight='bold')

# Add data points labels for the line plot
for genre, growth in zip(genres, growth_rates):
    ax2.text(growth + 0.2, genre, f'{growth}%', va='center', fontsize=10, color='green', fontweight='bold')

# Unified legend
ax1.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=color) for color in colors] +
           [plt.Line2D([0], [0], color='green', marker='o', linestyle='--')], 
           labels=genres + ['Growth Rate'], loc='lower right', frameon=False, title='Legend')

# Set grid lines for better readability
ax1.xaxis.grid(True, linestyle='--', color='grey', alpha=0.6)
ax2.xaxis.grid(True, linestyle='--', color='green', alpha=0.3)

# Ensure there is no overlap
plt.tight_layout()

# Display the plot
plt.show()