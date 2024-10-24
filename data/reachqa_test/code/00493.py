import matplotlib.pyplot as plt

# Data for the donut pie chart (genre popularity)
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
percentages = [30, 25, 20, 15, 10]

# Data for the bar chart (number of films released in 2023)
film_counts = [50, 40, 30, 20, 15]

# Define colors for each genre
colors = ['#FF5733', '#FFBD33', '#33FF57', '#3357FF', '#8333FF']

# Explode the 'Action' slice slightly for emphasis
explode = (0.1, 0, 0, 0, 0)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Create the donut pie chart
wedges, texts, autotexts = ax1.pie(
    percentages,
    labels=genres,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Draw center circle for the donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax1.axis('equal')

# Customize text for readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Title for the donut chart
ax1.set_title("Favorite Movie Genres of 2023\nA Deep Dive into Cinematic Preferences", fontsize=16, fontweight='bold', pad=20)

# Add a legend to identify colors with genres
ax1.legend(wedges, genres, title="Movie Genres", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

# Create the bar chart
ax2.bar(genres, film_counts, color=colors)
ax2.set_ylabel('Number of Films', fontsize=12)
ax2.set_title("Number of Films Released by Genre in 2023", fontsize=16, fontweight='bold', pad=20)
ax2.set_ylim(0, 60)  # Set y-limits for better visualization

# Add value labels on top of the bars
for i, count in enumerate(film_counts):
    ax2.text(i, count + 1, str(count), ha='center', fontsize=10)

# Automatically adjust layout to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()