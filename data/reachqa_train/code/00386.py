import matplotlib.pyplot as plt
import numpy as np

# Define decades and the popularity index of musical genres
decades = np.arange(1950, 2030, 10)
jazz_popularity = [70, 65, 55, 50, 40, 30, 25, 20]  # Popular in earlier decades
rock_popularity = [20, 60, 80, 75, 60, 50, 45, 40]  # Peaks in 70s and 80s
disco_popularity = [0, 10, 45, 70, 30, 10, 5, 0]    # Dominates late 70s
hiphop_popularity = [0, 0, 10, 30, 65, 80, 90, 85]  # Rise from the 80s
electronic_popularity = [5, 10, 15, 20, 30, 50, 60, 70]  # Steady rise over decades

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines for each genre
ax.plot(decades, jazz_popularity, label='Jazz', color='blue', marker='o', linewidth=2, linestyle='-')
ax.plot(decades, rock_popularity, label='Rock', color='green', marker='s', linewidth=2, linestyle='--')
ax.plot(decades, disco_popularity, label='Disco', color='orange', marker='^', linewidth=2, linestyle='-.')
ax.plot(decades, hiphop_popularity, label='Hip-hop', color='red', marker='D', linewidth=2, linestyle=':')
ax.plot(decades, electronic_popularity, label='Electronic', color='purple', marker='x', linewidth=2, linestyle='-.')

# Set labels and title
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('Decades of Melody:\nMusical Genre Popularity Over Time', fontsize=16, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend
ax.legend(loc='upper right', title='Music Genres', fontsize=10, title_fontsize='12')

# Customize x-axis labels
plt.xticks(decades, fontsize=10)
plt.yticks(fontsize=10)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()