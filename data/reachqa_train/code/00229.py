import matplotlib.pyplot as plt

# Define the book genres and their corresponding market share percentages
genres = [
    "Mystery/Thriller", "Romance", "Science Fiction", "Fantasy",
    "Non-fiction", "Self-help", "Historical", "Young Adult"
]
market_shares = [15, 20, 12, 18, 10, 8, 9, 8]

# Define colors for each genre for aesthetic appeal
colors = [
    "#ff9999", "#66b3ff", "#99ff99", "#ffcc99",
    "#c2c2f0", "#ffb3e6", "#ff6666", "#c4e17f"
]

# Choose a genre to explode for emphasis, here we highlight 'Romance'
explode = (0, 0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    market_shares,
    labels=genres,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'black'}
)

# Set text properties for better readability
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=10, weight="bold")

# Title with multi-line formatting for balance and emphasis
ax.set_title("Market Share of Popular Book Genres\nin 2023", fontsize=16, weight='bold', pad=20)

# Add a legend outside the pie chart to avoid overlapping
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the plot is displayed with an equal aspect ratio
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()