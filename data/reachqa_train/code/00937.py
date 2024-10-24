import matplotlib.pyplot as plt
import numpy as np

# Define genres and years
genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Adventure', 
          'Thriller', 'Non-Fiction', 'Historical', 'Biography', 'Horror']

# Construct sales data in thousands (fictional data for complexity)
sales_data = [
    [35, 45, 50, 60, 55, 52, 53, 57, 60, 62],  # Fantasy
    [25, 30, 35, 32, 40, 38, 41, 43, 44, 46],  # Mystery
    [40, 45, 50, 60, 65, 67, 66, 70, 75, 77],  # Romance
    [15, 18, 20, 25, 22, 23, 24, 26, 28, 30],  # Science Fiction
    [30, 35, 40, 38, 42, 44, 46, 45, 48, 50],  # Adventure
    [50, 55, 60, 58, 63, 65, 68, 70, 72, 75],  # Thriller
    [28, 32, 30, 33, 37, 35, 39, 40, 43, 45],  # Non-Fiction
    [20, 22, 25, 27, 29, 30, 32, 35, 37, 40],  # Historical
    [18, 20, 23, 24, 26, 28, 30, 31, 33, 36],  # Biography
    [10, 15, 18, 20, 22, 23, 24, 26, 28, 30]   # Horror
]

# Create a vertical box plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot
boxes = ax.boxplot(sales_data, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightcoral', color='darkred'),
                   capprops=dict(color='darkred'),
                   whiskerprops=dict(color='darkred'),
                   flierprops=dict(marker='o', color='darkorange', alpha=0.5),
                   medianprops=dict(color='darkblue'),
                   positions=range(1, len(genres) + 1))

# Set labels
ax.set_title('Annual Book Sales Distribution\nby Genre in the Wonderland Publishing Market', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('Book Sales (thousands of units)', fontsize=12)

# Customizing X-axis
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres, rotation=45, ha="right")

# Annotations to reflect fictional trends or changes
ax.annotate('Romantic Boom', xy=(3, 77), xytext=(2, 85),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

ax.annotate('Sci-Fi Resurgence', xy=(4, 30), xytext=(5, 35),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')

# Customize box colors
colors = ['skyblue', 'lightgreen', 'pink', 'lightyellow', 'lightsalmon', 
          'plum', 'lightcyan', 'navajowhite', 'lavender', 'lightgrey']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Display mean as a point
means = [np.mean(sales) for sales in sales_data]
ax.plot(range(1, len(genres) + 1), means, 'D', color='purple', label='Mean Sales')

# Add legend
ax.legend(loc='upper left')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()