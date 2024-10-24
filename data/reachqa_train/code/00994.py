import matplotlib.pyplot as plt
import numpy as np

# Data: Book titles and their publication years
books = [
    "The Great Gatsby", "1984", "To Kill a Mockingbird", 
    "The Catcher in the Rye", "Lord of the Rings", 
    "Pride and Prejudice", "Brave New World", 
    "Catch-22", "Fahrenheit 451", "Moby-Dick"
]
publishing_years = [1925, 1949, 1960, 1951, 1954, 1813, 1932, 1961, 1953, 1851]
average_pages = [218, 328, 281, 277, 1216, 432, 311, 453, 256, 635]  # Additional data for complexity

# Plot settings
fig, ax = plt.subplots(figsize=(16, 10))
y_pos = np.arange(len(books))

# Colors for the bars using a sequential colormap with more contrast
colors = plt.cm.plasma(np.linspace(0, 1, len(books)))

# Create horizontal bars
bars = ax.barh(y_pos, publishing_years, color=colors, edgecolor='black', height=0.6)

# Add labels and title
ax.set_yticks(y_pos)
ax.set_yticklabels(books, fontsize=12)
ax.set_xlabel('Year of Publication', fontsize=14)
ax.set_title('Top 10 Influential Fictional Books\nand Their Publishing Years', fontsize=18, fontweight='bold')

# Annotate the publication years on each bar
for bar, year in zip(bars, publishing_years):
    ax.text(year + 1, bar.get_y() + bar.get_height() / 2, f'{year}', va='center', ha='left', fontsize=10, color='black')

# Add a line plot for average pages to add another layer of information
ax.plot(average_pages, y_pos, marker='o', color='red', label='Average Pages')

# Create a legend for the line plot
ax.legend(loc='lower right', fontsize=12)

# Add a color bar to explain the color gradient
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=min(publishing_years), vmax=max(publishing_years)))
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Year Gradient', fontsize=12)

# Add grid lines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()