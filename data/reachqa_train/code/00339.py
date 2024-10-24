import matplotlib.pyplot as plt
import numpy as np

# Define decades for the x-axis
decades = np.arange(1980, 2030, 10)

# Sales percentages for each book format by decade
hardcover_sales = [60, 50, 40, 30, 20]  # Gradual decline
paperback_sales = [30, 40, 50, 45, 30]  # Growth, then stabilization
ebook_sales = [0, 10, 20, 35, 50]       # Rapid rise with digital advancements

# Total book sales volume (in millions) for each decade
total_sales_volume = [150, 180, 220, 270, 250]  # Sample data showing growth and saturation

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each book format's trend line
ax1.plot(decades, hardcover_sales, marker='o', label='Hardcover', linestyle='-', linewidth=2, color='#8B0000')
ax1.plot(decades, paperback_sales, marker='s', label='Paperback', linestyle='-', linewidth=2, color='#FFA500')
ax1.plot(decades, ebook_sales, marker='^', label='E-book', linestyle='-', linewidth=2, color='#4682B4')

# Add titles and labels
ax1.set_title('Evolution of Book Format Popularity and Total Sales Volume\nfrom 1980 to 2020', fontsize=16, pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Total Book Sales', fontsize=12)

# Customize the x and y ticks
ax1.set_xticks(decades)
ax1.set_yticks(np.arange(0, 101, 10))

# Add a legend for the line plot
ax1.legend(title='Book Format', loc='upper left')

# Annotate key points on the graph for additional context
ax1.annotate('E-books emerge', xy=(2000, 20), xytext=(2005, 40),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')
ax1.annotate('Paperback peak', xy=(2000, 50), xytext=(1995, 65),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='black')

# Add grid to the line plot for easier readability
ax1.grid(linestyle='--', alpha=0.7)

# Create a second y-axis for the total sales volume
ax2 = ax1.twinx()
ax2.bar(decades, total_sales_volume, width=5, alpha=0.3, color='gray', label='Total Sales Volume')

# Set the label for the second y-axis
ax2.set_ylabel('Total Book Sales (Millions)', fontsize=12)

# Ensure the legends do not overlap
fig.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# Automatically adjust layout to fit everything neatly
plt.tight_layout()

# Display the plot
plt.show()