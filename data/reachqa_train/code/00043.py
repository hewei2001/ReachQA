import matplotlib.pyplot as plt
import numpy as np

# Define the data
genres = ["Drama", "Comedy", "Documentary", "Sci-Fi", "Thriller"]
years = ["2015", "2016", "2017", "2018", "2019", "2020"]

# Awards data for each genre by year
awards_data = np.array([
    [25, 30, 35, 30, 28, 32],  # Drama
    [15, 18, 22, 20, 18, 20],  # Comedy
    [20, 25, 28, 27, 25, 30],  # Documentary
    [5, 7, 10, 15, 18, 20],    # Sci-Fi
    [10, 12, 15, 10, 12, 15]   # Thriller
])

# Create the heat map
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.imshow(awards_data, cmap='YlOrRd', aspect='auto', interpolation='nearest')

# Add a color bar
cbar = fig.colorbar(cax, ax=ax, orientation='vertical', label='Number of Awards')

# Set the ticks and labels
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(genres)))
ax.set_xticklabels(years)
ax.set_yticklabels(genres)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Add labels to each cell
for i in range(len(genres)):
    for j in range(len(years)):
        ax.text(j, i, awards_data[i, j], ha='center', va='center', color='black')

# Set the title and labels
ax.set_title('Heat Map of Global Film Festival\nAward Trends (2015-2020)', pad=20)
ax.set_xlabel('Year')
ax.set_ylabel('Genre')

# Automatically adjust the layout to avoid overlaps
plt.tight_layout()

# Show the plot
plt.show()