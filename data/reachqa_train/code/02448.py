import matplotlib.pyplot as plt

# Define video game genres and their market shares
genres = ['Action', 'RPG', 'Sports', 'Strategy', 'Simulation', 'Puzzle']
market_shares = [35, 25, 15, 10, 8, 7]

# Define distinct colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33FF', '#33FFFF', '#FFD700']

# Explode the Action genre for emphasis
explode = (0.1, 0, 0, 0, 0, 0)  # Highlight the Action genre

# Create a pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    market_shares, labels=genres, colors=colors, explode=explode, shadow=True,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85
)

# Enhance text visibility and style
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add a circle at the center for a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Maintain equal aspect ratio
plt.axis('equal')

# Add a title with line breaks for readability
plt.title('Video Game Genre Market Share in 2023:\nA Snapshot of Industry Trends', fontsize=16, fontweight='bold', ha='center')

# Position the legend outside the pie chart
plt.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust subplot parameters for optimal layout
plt.tight_layout()

# Display the pie chart
plt.show()