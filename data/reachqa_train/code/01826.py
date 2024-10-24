import matplotlib.pyplot as plt

# Define book genres and their allocation percentages
genres = [
    'Fiction', 'Non-fiction', 'Mystery', 'Science Fiction',
    'Fantasy', 'Biography', 'Young Adult', 'Children’s',
    'Romance', 'Graphic Novels'
]
percentages = [
    25, 15, 10, 12,
    8, 10, 9, 6,
    3, 2
]

# Define colors for each genre
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99',
    '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2',
    '#6666ff', '#ff99c2'
]

# Highlight 'Fiction' by separating it slightly
explode = [0.1 if genre == 'Fiction' else 0 for genre in genres]

# Plotting the pie chart
plt.figure(figsize=(10, 8))
plt.pie(percentages, labels=genres, autopct='%1.1f%%', startangle=140, colors=colors,
        wedgeprops=dict(edgecolor='black'), explode=explode, textprops={'fontsize': 10})

# Title and layout adjustments
plt.title("The Literary Landscape:\nGenre Distribution in Metroville Public Libraries", fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()