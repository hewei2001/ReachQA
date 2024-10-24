import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2015 to 2023
years = np.arange(2015, 2024)

# Define streaming hours (in millions) for each genre
indie_rock_streaming = [20, 28, 35, 44, 52, 63, 75, 88, 100]
indie_pop_streaming = [15, 22, 30, 39, 45, 55, 67, 78, 92]
indie_folk_streaming = [10, 15, 22, 28, 34, 41, 49, 57, 66]

# Plot the line chart
plt.figure(figsize=(12, 7))

# Plot line for each genre
plt.plot(years, indie_rock_streaming, marker='o', label='Indie Rock', linestyle='-', linewidth=2, color='#FF6347')
plt.plot(years, indie_pop_streaming, marker='s', label='Indie Pop', linestyle='-', linewidth=2, color='#4682B4')
plt.plot(years, indie_folk_streaming, marker='^', label='Indie Folk', linestyle='-', linewidth=2, color='#3CB371')

# Annotate significant milestones
annotations = [
    {'year': 2017, 'rock_value': 35, 'pop_value': 30, 'folk_value': 22, 'note': 'Major Platform Launch'},
    {'year': 2020, 'rock_value': 63, 'pop_value': 55, 'folk_value': 41, 'note': 'Pandemic Boost'},
    {'year': 2022, 'rock_value': 100, 'pop_value': 92, 'folk_value': 66, 'note': 'Indie Awards Recognition'}
]

for ann in annotations:
    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['rock_value']), xycoords='data',
                 xytext=(-70, 30), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#FF6347'),
                 fontsize=9, color='#FF6347')

    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['pop_value']), xycoords='data',
                 xytext=(-70, -40), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#4682B4'),
                 fontsize=9, color='#4682B4')

    plt.annotate(ann['note'],
                 xy=(ann['year'], ann['folk_value']), xycoords='data',
                 xytext=(10, 50), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='#3CB371'),
                 fontsize=9, color='#3CB371')

# Set title and labels
plt.title('Growth of Indie Music Streaming\nAcross Genres (2015-2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Streaming Hours (Millions)', fontsize=14)

# Customize x-ticks
plt.xticks(years)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Legend
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()