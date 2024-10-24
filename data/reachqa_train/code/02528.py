import matplotlib.pyplot as plt
import numpy as np

# Define the decades and music genres
decades = np.array(['1970s', '1980s', '1990s', '2000s', '2010s', '2020s'])
genres = ['Rock', 'Pop', 'Hip Hop', 'Electronic', 'Jazz/Blues']

# Create data representing the percentage of popularity for each genre
rock = np.array([50, 40, 30, 25, 20, 15])
pop = np.array([20, 25, 30, 30, 25, 20])
hip_hop = np.array([5, 10, 20, 25, 30, 30])
electronic = np.array([5, 5, 10, 15, 20, 25])
jazz_blues = 100 - (rock + pop + hip_hop + electronic)

# Generate related data for the line plot (e.g., number of songs produced)
songs_produced = np.array([1000, 1500, 2000, 2500, 3000, 3500])

# Create the figure and axis for the percentage bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot data using stacked bar chart
bar_width = 0.6
ax1.bar(decades, rock, label=genres[0], width=bar_width, color='#1f77b4', alpha=0.85)
ax1.bar(decades, pop, bottom=rock, label=genres[1], width=bar_width, color='#ff7f0e', alpha=0.85)
ax1.bar(decades, hip_hop, bottom=rock + pop, label=genres[2], width=bar_width, color='#2ca02c', alpha=0.85)
ax1.bar(decades, electronic, bottom=rock + pop + hip_hop, label=genres[3], width=bar_width, color='#d62728', alpha=0.85)
ax1.bar(decades, jazz_blues, bottom=rock + pop + hip_hop + electronic, label=genres[4], width=bar_width, color='#9467bd', alpha=0.85)

# Overlay line plot using secondary y-axis
ax2 = ax1.twinx()
ax2.plot(decades, songs_produced, label='Songs Produced', color='darkblue', linestyle='-', marker='o', linewidth=2)
ax2.set_ylabel('Number of Songs Produced', fontsize=14, fontweight='semibold', color='darkblue')

# Title and labels
ax1.set_title("Distribution of Popular Musical Genres Over Decades\nand Number of Songs Produced (1970-2020)", fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel("Decades", fontsize=14, fontweight='semibold')
ax1.set_ylabel("Popularity Percentage (%)", fontsize=14, fontweight='semibold')

# Legend configuration
ax1.legend(loc='upper left', title='Music Genres', title_fontsize='13', fontsize=11, framealpha=0.9)
ax2.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Set y-axis to percentage format and limit
ax1.set_yticks(np.arange(0, 101, 10))
ax1.set_yticklabels([f"{i}%" for i in range(0, 101, 10)])

# Annotate the chart for notable genre rises
annotations = {
    '1990s': "Rise of Hip Hop",
    '2000s': "Electronic Boom",
    '1980s': "Pop Music Peak",
}
for decade, label in annotations.items():
    ax1.annotate(label, xy=(decade, 90), xytext=(decade, 95),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Adjust x-axis label rotation and styling for clarity
plt.xticks(rotation=30, ha='right')

# Style and layout adjustments
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.set_axisbelow(True)  # Ensure grid lines are below plot elements
plt.tight_layout()

# Display the plot
plt.show()