import matplotlib.pyplot as plt
import numpy as np

# Define the book genres and expanded years for analysis
genres = [
    'Fiction', 'Non-Fiction', 'Science Fiction', 
    'Mystery', 'Fantasy', 'Biography', 'Thriller'
]

# Expanded sales data for each genre in each year (in thousands)
sales_data = [
    [50, 52, 55, 60, 64, 68, 70, 73, 76, 82, 90, 95, 100, 102, 105],   # Fiction
    [72, 74, 77, 79, 83, 87, 91, 94, 98, 103, 110, 116, 120, 125, 130], # Non-Fiction
    [30, 32, 34, 38, 41, 45, 50, 54, 58, 65, 70, 75, 80, 85, 90],      # Science Fiction
    [45, 47, 50, 52, 55, 58, 60, 63, 66, 70, 73, 76, 80, 82, 85],      # Mystery
    [62, 65, 69, 72, 75, 78, 81, 85, 89, 92, 97, 102, 105, 110, 115],  # Fantasy
    [55, 58, 60, 63, 66, 70, 74, 76, 79, 82, 86, 90, 95, 100, 105],    # Biography
    [40, 42, 44, 47, 50, 53, 56, 59, 63, 67, 71, 76, 82, 85, 90]       # Thriller
]

# Set up the figure and axis for box plot
fig, ax = plt.subplots(figsize=(14, 10))

# Create horizontal box plots
bp = ax.boxplot(sales_data, vert=False, patch_artist=True, notch=True, labels=genres, flierprops=dict(markerfacecolor='red', marker='o'))

# Customize boxplot colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#B3B3CC', '#F2B6B6', '#CCFF66']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Annotate the median sales
for line in bp['medians']:
    x, y = line.get_xdata(), line.get_ydata()
    ax.annotate(f'{x.mean():.0f}', xy=(x.mean(), y.mean()), textcoords='offset points', xytext=(10, -5), ha='center', fontsize=8, color='black')

# Titles and labels
ax.set_title('The Evolution of Book Publishing Genres\nExtended Annual Sales Distribution in Thousands', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Annual Sales (in thousands)', fontsize=12)
ax.set_ylabel('Book Genres', fontsize=12)

# Add grid for better readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a trend line (average line) for each genre
for i, data in enumerate(sales_data, start=1):
    avg_sales = np.mean(data)
    ax.plot([avg_sales, avg_sales], [i-0.4, i+0.4], color='gray', linestyle='--', linewidth=1.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()