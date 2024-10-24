import matplotlib.pyplot as plt

# Data preparation
genres = [
    'Fiction', 
    'Non-Fiction', 
    'Mystery/Thriller', 
    'Science Fiction/Fantasy', 
    'Romance', 
    'Historical', 
    'Young Adult'
]

popularity = [25, 20, 15, 15, 10, 8, 7]

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C4E17F', '#FADADD', '#B0E0E6']

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=genres, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3),
    textprops={'fontsize': 10, 'weight': 'bold', 'color': 'black'}
)

# Draw circle for the donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Set title and layout
ax.set_title('Global Book Genre Popularity in 2023', fontsize=14, weight='bold', pad=20, loc='center')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle

# Adjust the legend
ax.legend(
    wedges, 
    genres, 
    title="Genres", 
    title_fontsize='13', 
    fontsize='11', 
    loc='center left', 
    bbox_to_anchor=(1, 0.5),
    frameon=False
)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()