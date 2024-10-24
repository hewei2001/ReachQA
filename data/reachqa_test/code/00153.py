import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Streaming data in billion hours for each genre
pop_streaming = [20, 23, 25, 28, 30, 35, 38, 42]
hiphop_streaming = [15, 18, 20, 24, 28, 34, 40, 44]
rock_streaming = [12, 13, 15, 16, 18, 19, 20, 21]
classical_streaming = [4, 5, 5, 6, 6, 7, 8, 9]
jazz_streaming = [6, 7, 8, 7, 7, 6, 6, 7]
electronic_streaming = [7, 8, 10, 11, 13, 14, 16, 17]
country_streaming = [5, 6, 6, 7, 8, 8, 9, 10]

# Stack the data
streaming_data = np.array([pop_streaming, hiphop_streaming, rock_streaming, 
                           classical_streaming, jazz_streaming, electronic_streaming, 
                           country_streaming])

# Define genre labels and colors
genres = ['Pop', 'Hip Hop', 'Rock', 'Classical', 'Jazz', 'Electronic', 'Country']
colors = ['#FFC0CB', '#FF5733', '#C0C0C0', '#B0E0E6', '#6A5ACD', '#7FFF00', '#FFD700']

# Position of bars on x-axis
ind = np.arange(len(years))

# Define the width of bars
width = 0.6

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))

# Plot each genre's data
bottoms = np.zeros(len(years))
bars = []
for i, genre in enumerate(genres):
    bars.append(ax.bar(ind, streaming_data[i], width, bottom=bottoms, label=genre, color=colors[i]))
    bottoms += streaming_data[i]

# Titles and labels
ax.set_title('Digital Music Streaming Trends\n(2016-2023)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Streaming Hours (Billion)', fontsize=14)

# x-axis ticks and labels
ax.set_xticks(ind)
ax.set_xticklabels(years, fontsize=12)

# Add a legend to the chart
ax.legend(title='Music Genres', loc='upper left', fontsize=12)

# Add value labels on the bars for significant data points
for i in range(len(years)):
    total_height = 0
    for j, bar in enumerate(bars):
        height = streaming_data[j][i]
        total_height += height
        ax.text(i, total_height - height / 2, f'{height}', ha='center', va='center', color='black', fontsize=8)

# Plot total streaming hours as a line plot
total_streaming = streaming_data.sum(axis=0)
ax.plot(ind, total_streaming, marker='o', color='navy', label='Total', linewidth=2)
for i, total in enumerate(total_streaming):
    ax.text(i, total + 1, f'{total}', ha='center', va='bottom', color='navy', fontsize=9)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()