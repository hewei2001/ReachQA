import matplotlib.pyplot as plt

# Data for the pie chart
genres = ['Fiction', 'Non-Fiction', 'Fantasy', 'Mystery', 'Science Fiction']
market_share = [35, 25, 20, 10, 10]

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))

# Create wedges, labels, and percentages
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    explode=(0.1, 0, 0, 0, 0)  # Slightly explode the Fiction sector for emphasis
)

# Add a circular center to create the "sector" pie chart look
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie is drawn as a circle
ax.axis('equal')

# Set the title
plt.title("Global Literature Genres' Market Share\nAn Insight into Book Sales", fontsize=16, fontweight='bold', pad=20)

# Customize the texts and autotexts
plt.setp(texts, size=12, weight='bold', color='black')
plt.setp(autotexts, size=10, weight='bold', color='darkslategray')

# Add a legend outside of the pie chart
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()