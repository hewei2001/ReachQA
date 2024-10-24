import matplotlib.pyplot as plt
import numpy as np

# Define decades for the x-axis
decades = np.arange(1980, 2030, 10)

# Sales percentages for each book format by decade
hardcover_sales = [60, 50, 40, 30, 20]  # Gradual decline
paperback_sales = [30, 40, 50, 45, 30]  # Growth, then stabilization
ebook_sales = [0, 10, 20, 35, 50]       # Rapid rise with digital advancements

# Create the line plot
plt.figure(figsize=(12, 7))

# Plot each book format's trend line
plt.plot(decades, hardcover_sales, marker='o', label='Hardcover', linestyle='-', linewidth=2, color='#8B0000')
plt.plot(decades, paperback_sales, marker='s', label='Paperback', linestyle='-', linewidth=2, color='#FFA500')
plt.plot(decades, ebook_sales, marker='^', label='E-book', linestyle='-', linewidth=2, color='#4682B4')

# Add titles and labels
plt.title('Evolution of Book Format Popularity\nfrom 1980 to 2020', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Total Book Sales', fontsize=12)

# Customize the x and y ticks
plt.xticks(decades)
plt.yticks(np.arange(0, 101, 10))

# Add a legend to indicate which line corresponds to which format
plt.legend(title='Book Format', loc='upper left')

# Annotate key points on the graph for additional context
plt.annotate('E-books emerge', xy=(2000, 20), xytext=(2005, 40),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

plt.annotate('Paperback peak', xy=(2000, 50), xytext=(1995, 65),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Add grid for easier readability
plt.grid(linestyle='--', alpha=0.7)

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the plot
plt.show()