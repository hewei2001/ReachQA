import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Define streaming hours (in millions) for each genre
indie_rock_streaming = [20, 28, 35, 44, 52, 63, 75, 88, 100]
indie_pop_streaming = [15, 22, 30, 39, 45, 55, 67, 78, 92]
indie_folk_streaming = [10, 15, 22, 28, 34, 41, 49, 57, 66]

# Define unique listeners (in millions) for each genre
indie_rock_listeners = [5, 7, 10, 12, 15, 18, 22, 26, 30]
indie_pop_listeners = [4, 6, 8, 11, 13, 16, 19, 22, 27]
indie_folk_listeners = [3, 4, 6, 8, 10, 12, 15, 18, 22]

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot streaming hours line chart
ax1.plot(years, indie_rock_streaming, marker='o', label='Indie Rock Streaming', linestyle='-', linewidth=2, color='#FF6347')
ax1.plot(years, indie_pop_streaming, marker='s', label='Indie Pop Streaming', linestyle='-', linewidth=2, color='#4682B4')
ax1.plot(years, indie_folk_streaming, marker='^', label='Indie Folk Streaming', linestyle='-', linewidth=2, color='#3CB371')

# Create a second y-axis for unique listeners
ax2 = ax1.twinx()

# Plot unique listeners bar chart
width = 0.25
ax2.bar(years - width, indie_rock_listeners, width, label='Indie Rock Listeners', color='lightcoral', alpha=0.6)
ax2.bar(years, indie_pop_listeners, width, label='Indie Pop Listeners', color='lightsteelblue', alpha=0.6)
ax2.bar(years + width, indie_folk_listeners, width, label='Indie Folk Listeners', color='lightgreen', alpha=0.6)

# Annotations for milestones
annotations = [
    {'year': 2017, 'rock_value': 35, 'pop_value': 30, 'folk_value': 22, 'note': 'Major Platform Launch'},
    {'year': 2020, 'rock_value': 63, 'pop_value': 55, 'folk_value': 41, 'note': 'Pandemic Boost'},
    {'year': 2022, 'rock_value': 100, 'pop_value': 92, 'folk_value': 66, 'note': 'Indie Awards Recognition'}
]

for ann in annotations:
    ax1.annotate(ann['note'],
                 xy=(ann['year'], ann['rock_value']), xycoords='data',
                 xytext=(-70, 30), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#FF6347'),
                 fontsize=9, color='#FF6347')

    ax1.annotate(ann['note'],
                 xy=(ann['year'], ann['pop_value']), xycoords='data',
                 xytext=(-70, -40), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#4682B4'),
                 fontsize=9, color='#4682B4')

    ax1.annotate(ann['note'],
                 xy=(ann['year'], ann['folk_value']), xycoords='data',
                 xytext=(10, 50), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#3CB371'),
                 fontsize=9, color='#3CB371')

# Set titles and labels
ax1.set_title('Growth of Indie Music Streaming and Listeners\nAcross Genres (2015-2023)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Streaming Hours (Millions)', fontsize=14)
ax2.set_ylabel('Unique Listeners (Millions)', fontsize=14)

# Customize x-ticks
ax1.set_xticks(years)

# Add grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Combine legends from both plots
lines_labels = ax1.get_legend_handles_labels()
bars_labels = ax2.get_legend_handles_labels()
ax1.legend(lines_labels[0] + bars_labels[0], lines_labels[1] + bars_labels[1], loc='upper left', fontsize=12)

# Automatically adjust layout
fig.tight_layout()

# Show the plot
plt.show()