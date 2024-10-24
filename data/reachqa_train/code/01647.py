import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the years for the x-axis
years = np.arange(2012, 2023)

# Artificial data representing the popularity (percentage) of each music genre over the years
pop = [35, 36, 35, 34, 33, 32, 31, 29, 28, 27, 26]
rock = [25, 24, 23, 22, 21, 20, 19, 20, 21, 22, 22]
hip_hop = [10, 11, 14, 16, 19, 22, 25, 27, 28, 29, 30]
electronic = [5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14]
indie = [25, 23, 21, 20, 18, 16, 14, 12, 10, 9, 8]

# Combine datasets for the stackplot
genre_preferences = np.array([pop, rock, hip_hop, electronic, indie])

# Create the figure and axis for the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Using a Seaborn color palette for clear distinction
palette = sns.color_palette("Set2", 5)

# Create the stacked area chart
ax.stackplot(years, genre_preferences, labels=['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Indie'],
             colors=palette, alpha=0.85)

# Add titles and axis labels
ax.set_title("Evolving Popularity of Music Genres (2012-2022)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage of Total Music Consumption (%)", fontsize=14)

# Customize the legend
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Music Genre', fontsize=12)

# Enhance gridlines for better readability
ax.grid(alpha=0.4, linestyle='--')

# Add trend lines for each genre for clarity
for i, genre in enumerate(genre_preferences):
    ax.plot(years, genre, color=palette[i], linewidth=1.5, linestyle='dashed')

# Annotate the most dominant genre at the start and end years
dominant_2012 = np.argmax(genre_preferences[:, 0])
dominant_2022 = np.argmax(genre_preferences[:, -1])

ax.text(2012, genre_preferences[dominant_2012, 0] + 2,
        f"Dominant: {['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Indie'][dominant_2012]}",
        fontsize=10, fontweight='bold', color=palette[dominant_2012])

ax.text(2022, genre_preferences[dominant_2022, -1] + 2,
        f"Dominant: {['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Indie'][dominant_2022]}",
        fontsize=10, fontweight='bold', color=palette[dominant_2022])

# Adjust layout to prevent overlaps and ensure the chart is neat
plt.tight_layout()

# Display the plot
plt.show()