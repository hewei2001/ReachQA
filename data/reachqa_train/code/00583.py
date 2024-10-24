import matplotlib.pyplot as plt

# Data representing average annual revenue in million USD for each genre
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Science Fiction']
revenues = [550, 400, 300, 200, 450]

# Colors for each genre
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFA833']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(genres, revenues, color=colors, edgecolor='black', height=0.6)

# Customizing the plot
ax.set_title('Annual Revenue Distribution of Movie Genres\nA Look at the 2020s Film Industry', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Average Annual Revenue (Million USD)', fontsize=12)
ax.set_ylabel('Movie Genres', fontsize=12)

# Add value labels to each bar
for i, (genre, revenue) in enumerate(zip(genres, revenues)):
    ax.text(revenue + 10, i, f'{revenue}M', va='center', fontsize=10, color='black', fontweight='bold')

# Adding a legend to differentiate genres clearly
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
ax.legend(handles, genres, loc='lower right', title='Genres', frameon=False)

# Set grid lines for better readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Tweak layout for better readability
plt.tight_layout()

# Display the plot
plt.show()