import matplotlib.pyplot as plt
import numpy as np

# Define genres and years
genres = ['Fantasy', 'Mystery', 'Romance', 'Science Fiction', 'Adventure']

# Construct sales data in thousands (made-up data, ensuring diversity)
sales_data = [
    [35, 45, 50, 60, 55],  # Fantasy
    [25, 30, 35, 32, 40],  # Mystery
    [40, 45, 50, 60, 65],  # Romance
    [15, 18, 20, 25, 22],  # Science Fiction
    [30, 35, 40, 38, 42]   # Adventure
]

# Create a vertical box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot
boxes = ax.boxplot(sales_data, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightcoral', color='darkred'),
                   capprops=dict(color='darkred'),
                   whiskerprops=dict(color='darkred'),
                   flierprops=dict(marker='o', color='darkorange', alpha=0.5),
                   medianprops=dict(color='darkblue'),
                   positions=range(1, len(genres) + 1))

# Set labels
ax.set_title('Annual Book Sales Distribution\nby Genre in Wonderland', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('Book Sales (thousands of units)', fontsize=12)

# Customizing X-axis
ax.set_xticks(range(1, len(genres) + 1))
ax.set_xticklabels(genres)

# Annotations to reflect fictional trends or changes
ax.annotate('Romantic Boom', xy=(3, 62), xytext=(2, 70),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

ax.annotate('Sci-Fi Resurgence', xy=(4, 25), xytext=(5, 30),
            arrowprops=dict(facecolor='grey', arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')

# Customize box colors
for patch, color in zip(boxes['boxes'], ['skyblue', 'lightgreen', 'pink', 'lightyellow', 'lightsalmon']):
    patch.set_facecolor(color)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()