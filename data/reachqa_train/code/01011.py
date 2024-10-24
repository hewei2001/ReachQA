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

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the area chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, genre_data, labels=['Space Opera', 'Alien Encounters', 'Cosmic Adventure', 'Space Thriller', 'Time Travel Epic'], colors=colors, alpha=0.8)

# Customize the plot
ax.set_title('Celestial Cinema: Evolution of Popular Genres\nin Space Movies (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Popularity Score', fontsize=12)

# Add legend and grid
ax.legend(loc='upper left', fontsize=10, title='Genres', frameon=False)
ax.grid(linestyle='--', alpha=0.6)

# Adjust x-axis labels to prevent overlap
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 301, 50))

# Annotate a significant rise in popularity
ax.annotate('Rise of Time Travel Epics', xy=(2017, 150), xytext=(2014.5, 200),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'), fontsize=10, color='purple')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()