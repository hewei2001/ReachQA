import numpy as np
import matplotlib.pyplot as plt

# Define the music genres
genres = ['Pop', 'Hip-Hop', 'Classical', 'Electronic', 'Rock']

# Attributes to be compared
categories = ['Popularity', 'Streaming\nGrowth', 'Lyrical\nComplexity', 'Social Media\nEngagement', 'Global Reach']

# Data representing scores in each category for each genre
# Scores are out of 10 for simplicity
data = np.array([
    [8, 9, 5, 7, 8],  # Pop
    [7, 8, 8, 9, 6],  # Hip-Hop
    [5, 4, 9, 3, 5],  # Classical
    [6, 7, 5, 8, 7],  # Electronic
    [8, 6, 7, 6, 7]   # Rock
])

# Close the loop by appending the first value to the end of each data set
data = np.concatenate((data, data[:, [0]]), axis=1)

# Number of variables we're comparing
num_vars = len(categories)

# Create angle values for the radar chart (one for each category)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Plot each genre's data on the radar chart
for i, genre in enumerate(genres):
    ax.plot(angles, data[i], linewidth=2, linestyle='solid', label=genre)
    ax.fill(angles, data[i], alpha=0.25)

# Add labels for each category, with adjustments to avoid overlap
plt.xticks(angles[:-1], categories, fontsize=12, color='black', ha='center')

# Set title for the radar chart
plt.title("The Dynamic Soundscape:\nComparing Music Genres in 2023", size=16, color='darkblue', pad=20)

# Add a legend to differentiate between genres
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Automatically adjust layout to prevent overlap and ensure elements are well-spaced
plt.tight_layout()

# Display the radar chart
plt.show()