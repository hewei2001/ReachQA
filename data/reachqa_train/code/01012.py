import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional popularity scores for each genre
space_opera = np.array([30, 35, 40, 60, 80, 100, 120, 150, 180, 200, 220])
alien_encounters = np.array([20, 25, 30, 35, 45, 55, 70, 90, 110, 130, 150])
cosmic_adventure = np.array([10, 15, 20, 25, 35, 50, 70, 95, 120, 140, 160])
space_thriller = np.array([5, 10, 15, 20, 30, 40, 60, 80, 100, 120, 140])
time_travel_epic = np.array([8, 12, 18, 25, 35, 50, 75, 100, 125, 150, 175])

# Stack the data for the area chart
genre_data = np.vstack([space_opera, alien_encounters, cosmic_adventure, space_thriller, time_travel_epic])

# Calculate average popularity per year
average_popularity = np.mean(genre_data, axis=0)

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stackplot for Genre Popularity
ax1.stackplot(years, genre_data, labels=['Space Opera', 'Alien Encounters', 'Cosmic Adventure', 'Space Thriller', 'Time Travel Epic'], colors=colors, alpha=0.8)
ax1.set_title('Celestial Cinema: Evolution of Popular Genres\nin Space Movies (2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Popularity Score', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Genres', frameon=False)
ax1.grid(linestyle='--', alpha=0.6)
ax1.annotate('Rise of Time Travel Epics', xy=(2017, 150), xytext=(2014.5, 200),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=10, color='purple')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.set_yticks(np.arange(0, 301, 50))

# Line plot for Average Popularity
ax2.plot(years, average_popularity, color='darkblue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Average Popularity')
ax2.set_title('Average Popularity Score\nAcross All Genres (2010-2020)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Average Popularity Score', fontsize=12)
ax2.grid(linestyle='--', alpha=0.6)
ax2.legend(loc='upper left', fontsize=10, frameon=False)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.set_yticks(np.arange(0, 201, 25))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()