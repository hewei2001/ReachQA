import matplotlib.pyplot as plt

# Define the literary genres and their respective percentages
genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Non-Fiction', 'Young Adult', 'Historical', 'Horror']
percentages = [20, 15, 25, 10, 12, 8, 6, 4]

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2']

# Highlight the 'Romance' genre by slightly separating it
explode = (0, 0, 0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
    pctdistance=0.85, explode=explode, textprops={'fontsize': 10}
)

# Format the text on the wedges
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Draw a circle at the center to make it look like a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Set the title with line breaks for readability
plt.title('Distribution of Literary Genres\nin Contemporary Publishing', pad=20, fontsize=14, color='navy', weight='bold')

# Add a legend outside the plot
plt.legend(wedges, genres, title="Genres", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to ensure everything fits without overlap
plt.tight_layout()

# Display the pie chart
plt.show()