import matplotlib.pyplot as plt

# Define the data
genres = ['Pop', 'Rock', 'Hip Hop', 'EDM', 'Jazz', 'Classical', 'Country', 'R&B']
market_share = [25, 18, 20, 15, 7, 5, 6, 4]

# Color palette for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#f0e442', '#ffb3e6', '#c2f0c2', '#ff6666']

# Explode slices for emphasis on 'Pop' and 'Hip Hop'
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    market_share, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140,
    explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 10}
)

# Style for improved readability
for text in texts + autotexts:
    text.set_color('black')

# Chart title with multiple lines for clarity
ax.set_title(
    "Distribution of Popular Music Genres\nin Streaming Services (2023)",
    fontsize=14, fontweight='bold', pad=20
)

# Legend configuration for clarity
ax.legend(genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Adjust layout to avoid overlapping elements
plt.tight_layout()

# Show plot
plt.show()