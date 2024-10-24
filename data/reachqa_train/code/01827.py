import matplotlib.pyplot as plt
import numpy as np

# Define book genres and their allocation percentages
genres = [
    'Fiction', 'Non-fiction', 'Mystery', 'Science Fiction',
    'Fantasy', 'Biography', 'Young Adult', 'Children’s',
    'Romance', 'Graphic Novels'
]
percentages = [25, 15, 10, 12, 8, 10, 9, 6, 3, 2]

# Hypothetical total book counts for each genre
book_counts = [2500, 1500, 1000, 1200, 800, 1000, 900, 600, 300, 200]

# Define colors for each genre
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99',
    '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2',
    '#6666ff', '#ff99c2'
]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Pie chart
explode = [0.1 if genre == 'Fiction' else 0 for genre in genres]
axs[0].pie(percentages, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors,
           wedgeprops=dict(edgecolor='black'), explode=explode, textprops={'fontsize': 10})
axs[0].set_title("The Literary Landscape:\nGenre Distribution in Metroville Public Libraries", fontsize=16, fontweight='bold', pad=20)

# Bar chart
x_pos = np.arange(len(genres))
axs[1].bar(x_pos, book_counts, color=colors, edgecolor='black')
axs[1].set_xticks(x_pos)
axs[1].set_xticklabels(genres, rotation=45, ha='right')
axs[1].set_ylabel('Total Book Counts')
axs[1].set_title("Book Inventory by Genre\nin Metroville Public Libraries", fontsize=14, fontweight='bold', pad=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()