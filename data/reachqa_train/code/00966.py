import matplotlib.pyplot as plt
import numpy as np

# Define book genres and their corresponding sales in millions
genres = [
    'Fiction',
    'Non-Fiction',
    'Fantasy',
    'Science Fiction',
    'Romance',
    'Thriller',
    'Mystery',
    'Biography',
    'Self-help',
    'Children'
]

# Sales data in millions
sales = np.array([
    150,  # Fiction
    120,  # Non-Fiction
    95,   # Fantasy
    70,   # Science Fiction
    105,  # Romance
    85,   # Thriller
    110,  # Mystery
    60,   # Biography
    90,   # Self-help
    130   # Children
])

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(genres)))
bars = ax.barh(genres, sales, color=colors, edgecolor='black')

# Set title and labels
ax.set_title("Global Book Sales by Genre in 2022\n(Units in Millions)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Sales (Millions)', fontsize=14)
ax.set_ylabel('Genre', fontsize=14)

# Set x-axis limits
ax.set_xlim(0, 160)

# Add value labels on each bar
for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', color='black', fontsize=12)

# Annotate special insights
ax.annotate('Top-selling Genre', xy=(150, 0), xytext=(155, 0),
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5),
            fontsize=12, color='red')

ax.annotate('Unexpected Rise', xy=(130, 9), xytext=(135, 8.5),
            arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
            fontsize=12, color='green')

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()