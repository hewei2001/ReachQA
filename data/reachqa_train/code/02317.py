import matplotlib.pyplot as plt
import numpy as np

# Data: Genres and their representation as a percentage of total preferences
genres = ['Fantasy', 'Historical Fiction', 'Science Fiction', 'Mystery', 'Non-Fiction', 'Romance', 'Thriller']
preferences_percentage = [25, 15, 20, 10, 12, 8, 10]

# Colors for each genre slice using a vibrant colormap
colors = plt.cm.Paired(np.linspace(0, 1, len(genres)))

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Pie chart, where slices will be separated for emphasis on larger segments
wedges, texts, autotexts = ax.pie(preferences_percentage, labels=genres, colors=colors, autopct='%1.1f%%',
                                  startangle=140, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'),
                                  explode=[0.05 if genre == 'Fantasy' else 0 for genre in genres])

# Draw circle for the donut hole effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Adjust text properties for better visibility
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# Title of the chart
ax.set_title('Literary Preferences in the Kingdom of Booklandia\n(A Genre Distribution Analysis)', fontsize=14, fontweight='bold', pad=20)

# Customize legend
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()