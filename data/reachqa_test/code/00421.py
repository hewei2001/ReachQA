import matplotlib.pyplot as plt

# Define music genres and the number of new releases in 2023
genres = [
    "Pop",
    "Rock",
    "Hip-Hop",
    "EDM",
    "R&B",
    "Country",
    "Folk",
    "Jazz",
    "Metal",
    "Classical",
]
releases_2023 = [
    21000,   # Pop
    18000,   # Rock
    16000,   # Hip-Hop
    14000,   # EDM
    12000,   # R&B
    11000,   # Country
    9000,    # Folk
    7000,    # Jazz
    5000,    # Metal
    3000     # Classical
]

# Calculate percentage of each genre's releases
total_releases = sum(releases_2023)
percentage_releases = [(genre, releases, (releases/total_releases)*100) for genre, releases in zip(genres, releases_2023)]
percentage_releases.sort(key=lambda x: x[2], reverse=True)  # Sort genres by percentage of releases

# Create horizontal bar chart
plt.figure(figsize=(12, 8))

# Bars with individual colors
colors = ['royalblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
bars = plt.barh([genre for genre, _, _ in percentage_releases], [releases for _, releases, _ in percentage_releases], color=colors)

# Annotate each bar with the release number and percentage for enhanced readability
for bar, (_, releases, percentage) in zip(bars, percentage_releases):
    plt.text(bar.get_width() + 1000, bar.get_y() + bar.get_height()/2,
             f'{releases} ({percentage:.1f}%)', va='center', color='black', fontsize=10)

# Add error bars to each bar
yerr = [releases * 0.05 for _, releases, _ in percentage_releases]
plt.barh([genre for genre, _, _ in percentage_releases], [releases for _, releases, _ in percentage_releases],
         xerr=yerr, color=colors, ecolor='lightgray', capsize=10, alpha=0.8)

# Adjust the layout for titles and labels
plt.xlabel('Number of New Releases in 2023')
plt.title('Top 10 Music Genres by New Releases\nin 2023')

# Add a grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ensure that the labels fit perfectly without any clipping
plt.margins(x=0.1)

# Invert y-axis to make the top genre appear at the top
plt.gca().invert_yaxis()

# Custom legend
plt.legend([plt.Rectangle((0,0),1,1,fc=color) for color in colors],
           genres, title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')

# Customize plot background and grid
plt.gca().set_facecolor('lightgrey')
plt.gca().grid(color='white', linestyle='--', linewidth=0.5)

# Apply tight layout to prevent overlapping text and labels
plt.tight_layout()

# Show the final chart
plt.show()