import matplotlib.pyplot as plt

# Define film genres and their global viewership preferences
genres = [
    'Action/Adventure', 'Drama', 'Comedy', 'Horror',
    'Romantic', 'Science Fiction', 'Animation', 'Documentary'
]
preferences = [22, 20, 18, 10, 12, 8, 5, 5]  # Proportions sum to 100%

# Colors for the pie chart, each genre assigned a distinct color
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', 
          '#92A8D1', '#F4A460', '#E0BBE4', '#FFD700']

# Explode a few slices for emphasis
explode = (0.1, 0, 0, 0, 0, 0.1, 0, 0)

# Create the figure and axis
plt.figure(figsize=(10, 7))

# Plot pie chart
wedges, texts, autotexts = plt.pie(
    preferences, 
    labels=genres, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="white"),
    wedgeprops=dict(edgecolor='w', linewidth=2)
)

# Enhancements: title and autotext adjustments
plt.title("Favorite Film Genres: \nA Global Snapshot", fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold")

# Add a legend with a title
plt.legend(wedges, genres, title="Film Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent text from overlapping
plt.tight_layout()

# Display the plot
plt.show()