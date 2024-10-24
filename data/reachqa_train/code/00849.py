import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define genres and thematic elements
genres = ['Science Fiction', 'Mystery', 'Romance']
themes = ['Technology', 'Emotion', 'Social Issues', 'Adventure', 'Relationships']

# Focus index for each genre (out of 100)
scifi_data = [90, 40, 60, 80, 50]
mystery_data = [30, 50, 70, 60, 40]
romance_data = [20, 85, 50, 30, 90]

# Arrange data into a list
data = [scifi_data, mystery_data, romance_data]

# Number of variables
N = len(themes)

# Compute angle for each axis
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]  # complete the loop

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Function to plot each genre
def plot_genre(data, color, label, marker):
    values = data + data[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=color, label=label, marker=marker)
    ax.fill(angles, values, color=color, alpha=0.15)

# Plot each genre's data with unique attributes
plot_genre(scifi_data, '#1f78b4', 'Science Fiction', 'o')
plot_genre(mystery_data, '#33a02c', 'Mystery', 's')
plot_genre(romance_data, '#e31a1c', 'Romance', '^')

# Add labels and grid enhancements
plt.xticks(angles[:-1], themes, color='grey', size=10)
ax.set_rlabel_position(30)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
plt.ylim(0, 100)

# Add annotations for clarity
for i, theme in enumerate(themes):
    ax.annotate(f'{scifi_data[i]}', xy=(angles[i], scifi_data[i]), textcoords='offset points', xytext=(0, 10), ha='center', color='blue', fontsize=8)
    ax.annotate(f'{mystery_data[i]}', xy=(angles[i], mystery_data[i]), textcoords='offset points', xytext=(0, -10), ha='center', color='green', fontsize=8)
    ax.annotate(f'{romance_data[i]}', xy=(angles[i], romance_data[i]), textcoords='offset points', xytext=(0, -20), ha='center', color='red', fontsize=8)

# Set title and legend
plt.title("Literature Genres: Comparative Focus Areas\nAcross Key Themes", size=14, color='darkblue', weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), title='Genres', frameon=False)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()