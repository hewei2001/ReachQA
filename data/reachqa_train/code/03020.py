import matplotlib.pyplot as plt

# Data: Genre distribution in the library
genres = [
    'Fiction', 'Non-Fiction', 'Mystery & Thriller', 'Sci-Fi & Fantasy',
    'Romance', 'Children’s Books', 'Others'
]
percentages = [35, 20, 15, 10, 8, 7, 5]

# Assign distinct colors to each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=genres,
    autopct='%1.1f%%',
    startangle=90,  # Improved orientation for readability
    colors=colors,
    wedgeprops={'width': 0.4, 'edgecolor': 'w'},
    textprops=dict(color="black", fontsize=10, weight='bold'),
    pctdistance=0.85,  # Place percentages inside segments
    shadow=True  # Add shadow for depth
)

# Adjust autotext properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Add a white circle at the center to create the donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Title and Legend Configuration
ax.set_title('Book Haven Library:\nGenre Distribution of Collection', fontsize=16, fontweight='bold', pad=30)
ax.axis('equal')  # Ensure pie chart is circular
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Automatically adjust subplot parameters to give specified padding and avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()