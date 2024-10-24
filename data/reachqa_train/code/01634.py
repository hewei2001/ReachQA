import matplotlib.pyplot as plt
import squarify

# Data for the treemap: market share of video game genres
genres = [
    "Action", "Role-Playing", "Sports", "Simulation",
    "Strategy", "Adventure", "Puzzle", "Racing", "Fighting"
]
market_share = [22, 18, 15, 12, 10, 8, 6, 5, 4]  # In percentages
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
    '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#6666ff'
]

# Data for the bar chart: number of new releases per genre
new_releases = [150, 130, 110, 80, 75, 60, 50, 45, 35]

# Create a figure and a set of subplots (1 row, 2 columns)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Treemap plot
squarify.plot(sizes=market_share, label=[f'{genre}\n{share}%' for genre, share in zip(genres, market_share)], 
              color=colors, alpha=0.8, ax=axes[0], edgecolor="white", text_kwargs={'fontsize': 10, 'weight': 'bold'})
axes[0].set_title("Video Game Market Share by Genre\nYear 2023", fontsize=14, fontweight='bold')
axes[0].axis('off')

# Bar chart plot
axes[1].barh(genres, new_releases, color=colors, alpha=0.7, edgecolor='black')
axes[1].set_title("New Video Game Releases by Genre\nYear 2023", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Number of New Releases", fontsize=12)
axes[1].invert_yaxis()  # Invert y-axis for better readability
# Annotate bars with the number of releases
for index, value in enumerate(new_releases):
    axes[1].text(value, index, f' {value}', va='center', fontsize=10, weight='bold')

# Adjust layout
plt.tight_layout()

# Display both plots
plt.show()