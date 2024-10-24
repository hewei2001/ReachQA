import matplotlib.pyplot as plt
import numpy as np

# Define the years and genres
years = ['2017', '2018', '2019', '2020', '2021']
genres = ['Mystery', 'Science Fiction', 'Romance', 'Non-fiction']

# Number of digital readers (in thousands) per genre each year
data = {
    'Mystery': [15, 18, 20, 22, 24],
    'Science Fiction': [10, 12, 15, 18, 20],
    'Romance': [25, 28, 30, 34, 37],
    'Non-fiction': [30, 32, 35, 40, 42]
}

# Colors for each genre
colors = {
    'Mystery': '#6a0dad',
    'Science Fiction': '#1e90ff',
    'Romance': '#ff69b4',
    'Non-fiction': '#32cd32'
}

# Calculate the total number of readers per year
total_readers = np.sum([data[genre] for genre in genres], axis=0)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Initialize the bottom position for the first stack
bottom = np.zeros(len(years))

# Plot stacked bars for each genre
for genre in genres:
    ax.bar(years, data[genre], label=genre, color=colors[genre], bottom=bottom)
    bottom += np.array(data[genre])

# Overlay line plot for total readers
ax.plot(years, total_readers, color='black', marker='o', linestyle='--', linewidth=2, label='Total Readers')

# Set title and labels
ax.set_title('Digital Reading Trends in\nGlobal Literary Genres (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Digital Readers (Thousands)', fontsize=12)

# Rotate x-ticks to prevent overlap
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add legend with title
ax.legend(title='Literary Genres', loc='upper left', bbox_to_anchor=(1, 1))

# Add data labels for the line plot
for i, total in enumerate(total_readers):
    ax.text(years[i], total + 3, f'{total}', ha='center', va='bottom', fontweight='bold')

# Enhance layout
plt.tight_layout()

# Show the plot
plt.show()