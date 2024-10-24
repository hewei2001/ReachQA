import matplotlib.pyplot as plt
import squarify

# Define data for the treemap
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Science Fiction', 'Romance', 'Horror']
market_shares = [35, 25, 12, 10, 8, 6, 4]  # Market share percentages
colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FF69B4', '#FFA07A', '#8A2BE2']

# Define related data for the bar chart (growth rate)
growth_rates = [5, 3, 4, 6, 2, 3, 1]  # Fictional growth rates over the last year

# Set up the plot layout
fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Plot the treemap
squarify.plot(
    sizes=market_shares,
    label=[f'{genre}\n{share}%' for genre, share in zip(genres, market_shares)],
    color=colors,
    alpha=0.8,
    pad=3,
    ax=ax[0],
    text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'black'}
)

ax[0].set_title(
    "Global Literary Genres:\nMarket Share in 2023",
    fontsize=14,
    fontweight='bold',
    color='darkgreen'
)

# Hide the axes for the treemap
ax[0].axis('off')

# Plot the bar chart
ax[1].bar(genres, growth_rates, color=colors, alpha=0.8)
ax[1].set_title("Genre Growth Rates in 2023", fontsize=14, fontweight='bold', color='darkgreen')
ax[1].set_ylabel('Growth Rate (%)', fontsize=12)
ax[1].set_xlabel('Genres', fontsize=12)
ax[1].tick_params(axis='x', rotation=45)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()