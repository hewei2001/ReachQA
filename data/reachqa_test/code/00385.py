import numpy as np
import matplotlib.pyplot as plt

# Age groups
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']

# Book genres
genres = ['Romance', 'Mystery', 'Science Fiction', 'Fantasy', 'Non-Fiction', 'Horror', 'Historical Fiction']

# Reading frequency data (normalized to 0-1 range)
reading_frequency_data = np.array([
    [0.7, 0.5, 0.3, 0.4, 0.5, 0.2, 0.3],  # 18-24
    [0.6, 0.7, 0.4, 0.5, 0.6, 0.3, 0.4],  # 25-34
    [0.5, 0.6, 0.5, 0.6, 0.7, 0.4, 0.5],  # 35-44
    [0.4, 0.5, 0.6, 0.7, 0.8, 0.5, 0.6],  # 45-54
    [0.3, 0.4, 0.7, 0.8, 0.9, 0.6, 0.7],  # 55-64
    [0.2, 0.3, 0.8, 0.9, 1.0, 0.7, 0.8]   # 65+
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the heat map
im = ax.imshow(reading_frequency_data, cmap='coolwarm', interpolation='nearest', aspect='auto')

# Annotate the heat map with values
for i in range(len(age_groups)):
    for j in range(len(genres)):
        ax.text(j, i, f'{reading_frequency_data[i, j]:.1f}', ha='center', va='center', color='w')

# Set title and labels
ax.set_title("Reading Habits Across Age Groups:\nFavorite Book Genres Heat Map", fontsize=16, pad=20)
ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Age Groups', fontsize=12)
ax.set_xticks(np.arange(len(genres)))
ax.set_yticks(np.arange(len(age_groups)))
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(age_groups, fontsize=10)

# Create a color bar
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
cbar.ax.set_ylabel('Reading Frequency (Normalized)', fontsize=12)

# Highlight the highest reading frequency
max_idx = np.unravel_index(np.argmax(reading_frequency_data), reading_frequency_data.shape)
ax.text(max_idx[1], max_idx[0], '*', ha='center', va='center', color='black', fontsize=18)

# Layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()