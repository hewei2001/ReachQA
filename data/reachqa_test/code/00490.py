import matplotlib.pyplot as plt
import numpy as np

# Film genres and their popularity percentages
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]
popularity = [25, 20, 30, 15, 10]

# Average IMDb ratings for each genre
average_ratings = [7.0, 6.5, 8.0, 6.0, 7.5]

# Define colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.05, 0, 0, 0, 0)  # Slightly explode the Action slice for emphasis

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1]})

# Ring Pie Chart
wedges, texts, autotexts = axs[0].pie(popularity, labels=genres, autopct='%1.1f%%', startangle=140,
                                   colors=colors, explode=explode, wedgeprops=dict(width=0.3, edgecolor='white'))

axs[0].axis('equal')
axs[0].set_title("Popularity of Film Genres\nin Modern Cinema (2023)", fontsize=16, weight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold", color="black")  
plt.setp(texts, size=12, weight="bold")

# Central label
axs[0].text(0, 0, "Film Genres", horizontalalignment='center', verticalalignment='center', 
            fontsize=18, weight='bold', color='darkblue')

# Legend positioning
axs[0].legend(wedges, genres, title="Genres", loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Bar Chart for Average Ratings
axs[1].bar(genres, average_ratings, color=colors)
axs[1].set_title("Average IMDb Ratings\nby Genre (2023)", fontsize=16, weight='bold', pad=20)
axs[1].set_ylabel("Average IMDb Rating")
axs[1].set_ylim(0, 10)  # Set limit for y-axis
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels on bars
for i, v in enumerate(average_ratings):
    axs[1].text(i, v + 0.1, str(v), ha='center', fontweight='bold', color='black')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()