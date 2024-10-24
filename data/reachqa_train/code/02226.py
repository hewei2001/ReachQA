import matplotlib.pyplot as plt
import numpy as np

# Data for the number of books sold by genre
genres = ['Fiction', 'Non-Fiction', 'Fantasy', 'Science Fiction', 'Mystery', 'Historical']
books_sold = [1500, 1200, 800, 1000, 1100, 600]

# Define colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33C4', '#33FFC4']

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(genres, books_sold, color=colors, edgecolor='black')

# Annotate the bars with the number of books sold
for bar, books in zip(bars, books_sold):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 30, f'{books}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Title and labels
ax.set_title('Annual Grand Book Festival 2023\nGenre Sales Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Genres', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Sold', fontsize=12, labelpad=10)

# Customize ticks
ax.set_xticks(np.arange(len(genres)))
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=11)

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Set a tighter layout for the plot
plt.tight_layout()

# Display the chart
plt.show()