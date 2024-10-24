import matplotlib.pyplot as plt
import numpy as np

# Years for our observation
years = np.arange(2000, 2021)

# Percentage data for each genre per year
fantasy = np.array([
    10, 12, 15, 18, 20, 22, 24, 25, 27, 30, 
    35, 38, 40, 42, 45, 47, 48, 50, 52, 55, 58
])
science_fiction = np.array([
    20, 18, 17, 17, 18, 20, 21, 23, 24, 25, 
    26, 28, 29, 31, 33, 35, 36, 37, 38, 40, 42
])
mystery = np.array([
    30, 28, 28, 28, 29, 30, 30, 31, 32, 33, 
    35, 36, 35, 34, 34, 33, 32, 32, 31, 30, 29
])
romance = np.array([
    40, 42, 40, 37, 33, 28, 25, 21, 17, 12, 
    4, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1
])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot stacked area chart
ax.stackplot(years, fantasy, science_fiction, mystery, romance, 
             labels=['Fantasy', 'Science Fiction', 'Mystery', 'Romance'],
             colors=['#ffd700', '#4b0082', '#cd5c5c', '#ff69b4'],
             alpha=0.8)

# Set titles and labels
ax.set_title('Evolution of Literature Genres\nin the 21st Century', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Total Book Sales', fontsize=12)

# Customize the legend
ax.legend(loc='upper left', fontsize=10, title='Genres', title_fontsize='12')

# Customize grid lines
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()