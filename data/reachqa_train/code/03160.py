import matplotlib.pyplot as plt
import numpy as np

# Define the genres and their market share percentages
genres = ['Strategy', 'Family', 'Party', 'Cooperative', 'Thematic', 'Abstract']
market_share = np.array([25, 20, 15, 18, 12, 10])

# Define colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#F3FF33', '#33FFF9']

# Define explode to highlight the Strategy genre
explode = (0.1, 0, 0, 0, 0, 0)

# Create a pie chart with the specified parameters
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    market_share, 
    labels=genres, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    explode=explode, 
    shadow=True, 
    textprops={'fontsize': 12, 'fontweight': 'bold'}
)

# Draw a circle at the center to turn the pie into a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Title with a description, broken into two lines
ax.set_title('Board Game Genres Market Share\nWorldwide in 2023', fontsize=16, fontweight='bold', pad=20)

# Add a legend outside the plot
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to fit everything nicely
plt.tight_layout()

# Display the plot
plt.show()