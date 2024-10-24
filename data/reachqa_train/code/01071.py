import matplotlib.pyplot as plt
import numpy as np

# Define the decades and genres
decades = ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
genres = ['Mystery', 'Romance', 'Historical Fiction', 'Science Fiction', 'Fantasy']

# Popularity data (as fictional values)
mystery = [30, 35, 40, 45, 35, 30, 25, 20, 15, 15, 10]
romance = [20, 25, 30, 40, 45, 50, 55, 50, 45, 40, 35]
historical_fiction = [25, 20, 20, 25, 30, 35, 30, 25, 20, 15, 10]
science_fiction = [5, 10, 15, 15, 20, 25, 30, 40, 50, 55, 60]
fantasy = [20, 10, 5, 5, 10, 15, 20, 35, 40, 50, 55]

# Stack the data for the stacked area chart
data = np.vstack([mystery, romance, historical_fiction, science_fiction, fantasy])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the stacked area chart
ax.stackplot(decades, data, labels=genres, colors=['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974'], alpha=0.85)

# Title and labels
ax.set_title("Evolution of Literary Genres:\nA Century of Influence (1920 - 2020)", fontsize=16, pad=20)
ax.set_xlabel("Decade", fontsize=12)
ax.set_ylabel("Popularity (Imaginary Units)", fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title="Genres", fontsize=10, bbox_to_anchor=(1.05, 1))

# Enhancing the aesthetics with gridlines and layout
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Adjust x-axis labels to avoid overlap
plt.xticks(rotation=45, ha='right')

# Ensure layout is adjusted to fit everything nicely
plt.tight_layout()

# Display the chart
plt.show()