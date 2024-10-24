import matplotlib.pyplot as plt
import numpy as np

# Define decades
decades = ['1960s', '1970s', '1980s', '1990s', '2000s']

# Define music genres
genres = ['Rock', 'Pop', 'Hip Hop', 'Jazz', 'Country', 'Classical', 'Electronic']

# Data: percentage popularity of each genre over the decades
data = np.array([
    [40, 30, 5, 10, 8, 7, 0],   # 1960s
    [35, 30, 10, 10, 8, 5, 2],  # 1970s
    [30, 35, 15, 5, 8, 3, 4],   # 1980s
    [25, 30, 20, 5, 7, 3, 10],  # 1990s
    [20, 25, 25, 5, 5, 2, 18]   # 2000s
])

# Transpose data for plotting
data_transposed = data.T

# Colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c0c0c0']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Initialize bottom at zero for stacking
bottom = np.zeros(len(decades))

# Plot each genre's data as a stacked bar
for idx, genre in enumerate(genres):
    ax.bar(decades, data_transposed[idx], bottom=bottom, label=genre, color=colors[idx], alpha=0.8)
    bottom += data_transposed[idx]  # Update bottom for the next stack

# Set the title and labels
ax.set_title('The Evolution of Music Genres Over the Decades', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Popularity (%)', fontsize=12)

# Adjust y-axis to always show 0 to 100%
ax.set_ylim(0, 100)

# Display a legend outside the chart
ax.legend(title='Genres', loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=10)

# Style adjustments
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()