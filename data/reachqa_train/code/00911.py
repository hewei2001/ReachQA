import matplotlib.pyplot as plt
import numpy as np

# Decades
decades = ['1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Data: Popularity of music genres over each decade as percentages
rock = [50, 45, 35, 30, 25, 20]
pop = [20, 25, 30, 35, 40, 45]
hip_hop = [0, 5, 15, 25, 30, 25]
classical = [10, 8, 5, 4, 3, 2]
jazz = [10, 7, 4, 3, 2, 1]
electronic = [5, 5, 5, 10, 15, 20]
country = [5, 5, 6, 6, 5, 7]

# Colors for each genre
colors = ['#8B0000', '#FF69B4', '#8A2BE2', '#FFD700', '#4682B4', '#32CD32', '#D2691E']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(decades, rock, pop, hip_hop, classical, jazz, electronic, country,
             labels=['Rock', 'Pop', 'Hip-Hop', 'Classical', 'Jazz', 'Electronic', 'Country'],
             colors=colors, alpha=0.8)

# Customize the plot
ax.set_title("The Evolution of Music Genres Over Time:\nFrom the 1970s to the 2020s", fontsize=16, weight='bold')
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Percentage of Total Music Consumption", fontsize=12)
ax.set_ylim(0, 100)  # Ensure the y-axis represents percentages
ax.legend(loc='upper left', title="Music Genres", fontsize=10, title_fontsize='13', bbox_to_anchor=(1.05, 1))

# Improve layout
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()