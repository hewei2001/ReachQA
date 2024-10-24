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

# Hypothetical total book sales data for each year
total_sales = np.array([
    500, 520, 540, 580, 600, 650, 670, 700, 720, 750,
    780, 810, 830, 860, 880, 910, 930, 950, 980, 1000, 1030
])

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot stacked area chart
ax1.stackplot(years, fantasy, science_fiction, mystery, romance, 
              labels=['Fantasy', 'Science Fiction', 'Mystery', 'Romance'],
              colors=['#ffd700', '#4b0082', '#cd5c5c', '#ff69b4'], alpha=0.8)

# Set titles and labels for primary axis
ax1.set_title('Evolution of Literature Genres in the 21st Century\nwith Total Book Sales Overlay', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Total Book Sales', fontsize=12)

# Add a secondary y-axis for total book sales
ax2 = ax1.twinx()
ax2.plot(years, total_sales, color='green', linestyle='--', marker='o', linewidth=2, label='Total Sales')
ax2.set_ylabel('Total Book Sales (in 000s)', fontsize=12, color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Customize the legend
ax1.legend(loc='upper left', fontsize=10, title='Genres', title_fontsize='12')
ax2.legend(loc='upper right', fontsize=10)

# Customize grid lines
ax1.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()