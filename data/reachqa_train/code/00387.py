import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Define decades and the popularity index of musical genres
decades = np.arange(1950, 2030, 10)
jazz_popularity = [70, 65, 55, 50, 40, 30, 25, 20]
rock_popularity = [20, 60, 80, 75, 60, 50, 45, 40]
disco_popularity = [0, 10, 45, 70, 30, 10, 5, 0]
hiphop_popularity = [0, 0, 10, 30, 65, 80, 90, 85]
electronic_popularity = [5, 10, 15, 20, 30, 50, 60, 70]

# Create the line chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each genre with enhancements
ax.plot(decades, jazz_popularity, label='Jazz', color='navy', marker='o', linewidth=2, linestyle='-', alpha=0.8)
ax.plot(decades, rock_popularity, label='Rock', color='forestgreen', marker='s', linewidth=2, linestyle='--', alpha=0.8)
ax.plot(decades, disco_popularity, label='Disco', color='darkorange', marker='^', linewidth=2, linestyle='-.', alpha=0.8)
ax.plot(decades, hiphop_popularity, label='Hip-hop', color='darkred', marker='D', linewidth=2, linestyle=':', alpha=0.8)
ax.plot(decades, electronic_popularity, label='Electronic', color='indigo', marker='x', linewidth=2, linestyle='-.', alpha=0.8)

# Add background gradient
ax.set_facecolor('whitesmoke')
ax.grid(True, linestyle='--', alpha=0.5)

# Annotate significant points
for i, (x, y) in enumerate(zip(decades, disco_popularity)):
    if y == 70:
        ax.annotate('Peak Disco', xy=(x, y), xytext=(x-5, y+15), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

for i, (x, y) in enumerate(zip(decades, hiphop_popularity)):
    if y == 90:
        ax.annotate('Hip-hop Dominates', xy=(x, y), xytext=(x+5, y-20), arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Set labels and title with adjusted fontsize and title wrapping
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Popularity Index', fontsize=12)
ax.set_title('Decades of Melody:\nMusical Genre Popularity Over Time', fontsize=18, fontweight='bold', loc='left')

# Customizing ticks and adding minor ticks
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='gray')

# Add a legend with dynamic placement
ax.legend(loc='upper right', title='Music Genres', fontsize=11, title_fontsize='12', shadow=True, fancybox=True)

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()