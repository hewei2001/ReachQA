import matplotlib.pyplot as plt
import squarify  # Required for plotting treemaps

# Data representing the market share of video game genres
genres = [
    "Action", "Role-Playing", "Sports", "Simulation",
    "Strategy", "Adventure", "Puzzle", "Racing", "Fighting"
]
market_share = [22, 18, 15, 12, 10, 8, 6, 5, 4]  # In percentages

# Distinct colors for each genre for better visualization
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
    '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#6666ff'
]

# Create the tree map with the defined sizes and labels
plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_share, label=[f'{genre}\n{share}%' for genre, share in zip(genres, market_share)], 
              color=colors, alpha=0.8, edgecolor="white", text_kwargs={'fontsize': 10, 'weight': 'bold'})

# Add a meaningful title, breaking it into two lines for clarity
plt.title("Global Video Game Market Share by Genre\nYear 2023", fontsize=16, fontweight='bold')

# Remove axes since they don't provide relevant context for a treemap
plt.axis('off')

# Optimize the layout to prevent overlap and improve clarity
plt.tight_layout()

# Display the treemap
plt.show()