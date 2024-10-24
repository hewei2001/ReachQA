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

# Plot settings
plt.figure(figsize=(14, 8))
y_pos = np.arange(len(books))

# Colors for the bars
colors = plt.cm.viridis(np.linspace(0, 1, len(books)))

# Create horizontal bars
bars = plt.barh(y_pos, publishing_years, color=colors, edgecolor='black', height=0.5)

# Add labels and title
plt.yticks(y_pos, books, fontsize=10)
plt.xlabel('Year of Publication', fontsize=12)
plt.title('Top 10 Influential Fictional Books\nand Their Publishing Years', fontsize=16, fontweight='bold')

# Annotate the publication years on each bar
for bar, year in zip(bars, publishing_years):
    plt.text(year + 2, bar.get_y() + bar.get_height() / 2, f'{year}', va='center', ha='left', fontsize=10, color='black')

# Add grid lines for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()