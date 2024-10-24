import matplotlib.pyplot as plt
import squarify  # Required for generating treemaps

# Define data for the treemap
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Science Fiction', 'Romance', 'Horror']
market_shares = [35, 25, 12, 10, 8, 6, 4]  # Market share percentages
colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FF69B4', '#FFA07A', '#8A2BE2']

# Set up the plot
plt.figure(figsize=(12, 8))

# Plot the treemap with custom settings
squarify.plot(
    sizes=market_shares,
    label=[f'{genre}\n{share}%' for genre, share in zip(genres, market_shares)],
    color=colors,
    alpha=0.8,
    pad=3,
    text_kwargs={'fontsize': 12, 'weight': 'bold', 'color': 'black'}
)

# Set the title for the treemap
plt.title(
    "Global Literary Genres:\nMarket Share and Popularity in 2023",
    fontsize=18,
    fontweight='bold',
    color='darkgreen'
)

# Hide axes for a cleaner look
plt.axis('off')

# Adjust layout for better fitting
plt.tight_layout()

# Display the plot
plt.show()