import matplotlib.pyplot as plt

# Data for video game genres and their market share percentages
genres = ['Action', 'RPG', 'Strategy', 'Sports', 'Shooter', 'Simulation', 'Adventure']
market_shares = [25, 20, 15, 15, 12, 8, 5]

# Colors for each genre in the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']

# Explode parameter to highlight the 'Action' genre
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(market_shares, explode=explode, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors)

# Styling the text
plt.setp(texts, size=11)
plt.setp(autotexts, size=11, color='white')

# Title with multiple lines for better readability
ax.set_title('Video Game Genre Market Share in 2023\nHighlighting Dominant Genres', fontsize=16, pad=20)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Adding a legend outside the pie chart for additional information
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()