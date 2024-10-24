import matplotlib.pyplot as plt
import numpy as np

# Define the decades and the number of films produced in each genre
decades = np.arange(1950, 2030, 10)

# Film production data by genre
drama_films = [80, 85, 90, 70, 60, 55, 50, 40]
comedy_films = [70, 75, 85, 95, 100, 80, 70, 65]
western_films = [60, 55, 50, 30, 20, 15, 10, 5]

# Create the line chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each genre with different line styles and markers
ax.plot(decades, drama_films, label='Drama', color='#2b83ba', linewidth=2, linestyle='-', marker='o')
ax.plot(decades, comedy_films, label='Comedy', color='#fdae61', linewidth=2, linestyle='--', marker='s')
ax.plot(decades, western_films, label='Western', color='#d7191c', linewidth=2, linestyle=':', marker='^')

# Set chart title and labels
ax.set_title("Rise and Fall of Classic Film Genres (1950-2020)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Decades", fontsize=12)
ax.set_ylabel("Number of Films Produced", fontsize=12)

# Set grid and legend
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Genres', fontsize=10, loc='upper left')

# Annotate key trends
ax.annotate('Comedy Boom', xy=(1980, 95), xytext=(1985, 110),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, fontweight='bold', color='green')

ax.annotate('Western Decline', xy=(1970, 50), xytext=(1975, 60),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, fontweight='bold', color='red')

# Tighten layout to fit elements neatly
plt.tight_layout()

# Show the plot
plt.show()