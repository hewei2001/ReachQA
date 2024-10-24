import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Define the literary genres and their respective percentages
genres = [
    'Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Non-Fiction', 
    'Young Adult', 'Historical', 'Horror', 'Thriller', 'Biography',
    'Adventure', 'Self-Help', 'Graphic Novel', 'Satire'
]
percentages = [12, 10, 15, 8, 7, 5, 6, 3, 9, 4, 5, 7, 6, 3]

# Highlight the 'Romance' genre by slightly separating it
explode = [0.05 if genre == 'Romance' else 0 for genre in genres]

# Define colors for each genre
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', 
    '#ff6666', '#c2f0c2', '#e6b3cc', '#d9d9d9', '#ffcc00', '#ff99ff', 
    '#66ff99', '#c299ff'
]

# Create a subplot grid
fig = plt.figure(constrained_layout=True, figsize=(12, 8))
spec = GridSpec(ncols=2, nrows=1, figure=fig)

# Create a pie chart subplot
ax1 = fig.add_subplot(spec[0, 0])
wedges, texts, autotexts = ax1.pie(
    percentages, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
    pctdistance=0.85, explode=explode, textprops={'fontsize': 8}
)

# Format the text on the wedges
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Draw a circle at the center to make it look like a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
ax1.axis('equal')

# Title for the pie chart
ax1.set_title('Distribution of Literary Genres\nin Contemporary Publishing', fontsize=12, color='navy', weight='bold')

# Create a bar chart subplot for comparison
ax2 = fig.add_subplot(spec[0, 1], polar=True)
angles = [n / float(len(genres)) * 2 * 3.14159 for n in range(len(genres))]
percentages.append(percentages[0])
angles.append(angles[0])

# Create the radar plot (polar bar chart)
ax2.bar(angles, percentages, color=colors, alpha=0.7, width=0.3)

# Set titles and formatting for radar chart
ax2.set_yticklabels([])
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(genres, fontsize=8)
ax2.set_title('Polar Representation of Genre\nPercentages', fontsize=12, color='navy', weight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()