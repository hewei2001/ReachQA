import matplotlib.pyplot as plt
import numpy as np

# Define the genres and components
genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Horror']
components = ['Plot\nComplexity', 'Character\nDevelopment', 'Setting\nDetail', 
              'Emotional\nDepth', 'Thematic\nRichness', 'Dialogue\nQuality']

# Data for each genre
data = {
    'Fantasy': [8, 7, 9, 6, 7, 6],
    'Mystery': [9, 6, 5, 6, 7, 8],
    'Romance': [5, 9, 5, 8, 7, 6],
    'Science Fiction': [8, 6, 8, 6, 9, 5],
    'Horror': [6, 6, 7, 9, 5, 7]
}

# Create a 2D array of the data, with a repeated first value to close the plot
data_values = np.array([data[genre] + [data[genre][0]] for genre in genres])

# Number of variables we're plotting
num_vars = len(components)

# Compute angle for each variable
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Draw one line per genre and fill the area
for i, genre in enumerate(genres):
    ax.plot(angles, data_values[i], linewidth=2, label=genre)
    ax.fill(angles, data_values[i], alpha=0.25)

# Set labels for each component
ax.set_xticks(angles[:-1])
ax.set_xticklabels(components, fontsize=11)

# Set the title of the chart
ax.set_title('Key Components of Fiction Writing by Genre', fontsize=16, pad=20)

# Add a legend with appropriate settings
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Remove y-ticks and labels for a cleaner look
ax.set_yticklabels([])

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()