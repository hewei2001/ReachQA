import matplotlib.pyplot as plt
import numpy as np

# Define centuries from the 14th to the 21st
centuries = np.arange(14, 22)

# Popularity data for different art styles (in percentages)
classical = [60, 55, 45, 30, 20, 10, 5, 0]
renaissance = [20, 30, 40, 35, 25, 10, 5, 0]
baroque = [10, 10, 10, 20, 30, 40, 30, 0]
modernism = [5, 5, 10, 15, 20, 30, 40, 60]
abstract = [5, 0, 0, 0, 5, 10, 20, 40]

# Combine data into a 2D array for stackplot
data = np.array([classical, renaissance, baroque, modernism, abstract])

# Define labels and colors for the styles
styles = ['Classical', 'Renaissance', 'Baroque', 'Modernism', 'Abstract']
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#4682B4', '#5F9EA0']

# Plot the stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(centuries, data, labels=styles, colors=colors, alpha=0.8)

# Add title and labels
plt.title("Time Travelers' Artistic Evolution\nExploration of Art Styles Across Centuries", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Century', fontsize=12)
plt.ylabel('Popularity (%)', fontsize=12)

# Add a legend outside the plot area
plt.legend(title='Artistic Styles', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Annotate significant shifts in art styles
plt.text(14.5, 60, 'Classical Dominance', fontsize=10, color='darkred')
plt.text(16.5, 75, 'Renaissance Bloom', fontsize=10, color='goldenrod')
plt.text(18.5, 50, 'Modernism Rise', fontsize=10, color='navy')

# Customize grid lines
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

# Adjust the layout to avoid clipping of legend and labels
plt.tight_layout()

# Display the plot
plt.show()