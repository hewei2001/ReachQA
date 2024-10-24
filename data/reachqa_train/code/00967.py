import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

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

# Calculate percentage of total sales for annotations
total_sales = sales.sum()
percentages = (sales / total_sales) * 100

# Create a horizontal bar chart with enhanced features
fig, ax = plt.subplots(figsize=(14, 9))

# Use a categorical color palette
colors = plt.cm.tab20c(np.linspace(0, 1, len(genres)))

# Plot bars with textures
bars = ax.barh(genres, sales, color=colors, edgecolor='black', hatch='//')

# Set title and labels with a two-line title
ax.set_title("Global Book Sales by Genre in 2022\n(Units in Millions, Percentage of Total)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Sales (Millions)', fontsize=12)
ax.set_ylabel('Genre', fontsize=12)

# Set x-axis limits
ax.set_xlim(0, 160)

# Add value and percentage labels on each bar
for bar, percent in zip(bars, percentages):
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width} ({percent:.1f}%)', va='center', ha='left', color='black', fontsize=10)

# Add trend line (mocked data for demonstration)
trend_sales = [65, 90, 70, 55, 75, 60, 80, 45, 70, 85]
ax.plot(trend_sales, genres, '--k', label='Trend Line')

# Annotate special insights
ax.annotate('Top-selling Genre', xy=(150, 0), xytext=(155, 0),
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5),
            fontsize=10, color='red')

ax.annotate('Unexpected Rise', xy=(130, 9), xytext=(135, 8.5),
            arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
            fontsize=10, color='green')

ax.annotate('Lowest Sales', xy=(60, 7), xytext=(65, 6.5),
            arrowprops=dict(facecolor='blue', arrowstyle='->', lw=1.5),
            fontsize=10, color='blue')

# Add a grid and subtle 3D effect by customizing alpha and linewidth
ax.xaxis.grid(True, linestyle='--', alpha=0.5)

# Create a legend for the trend line
trend_patch = mpatches.Patch(color='grey', label='Trend', linestyle='--')
ax.legend(handles=[trend_patch], loc='lower right')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()