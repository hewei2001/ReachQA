import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Sales data (in millions of copies) for different book genres
fiction_sales = [24, 26, 27, 30, 29, 31, 33, 34, 35, 37, 39]
non_fiction_sales = [19, 20, 22, 24, 23, 22, 24, 25, 27, 29, 30]
mystery_sales = [15, 16, 15, 14, 16, 18, 17, 19, 20, 22, 23]
sci_fi_sales = [12, 13, 13, 14, 15, 16, 17, 19, 18, 19, 20]
fantasy_sales = [10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 20]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each genre's sales data
ax.plot(years, fiction_sales, marker='o', linestyle='-', linewidth=2, label='Fiction', color='skyblue')
ax.plot(years, non_fiction_sales, marker='s', linestyle='--', linewidth=2, label='Non-Fiction', color='orange')
ax.plot(years, mystery_sales, marker='^', linestyle='-.', linewidth=2, label='Mystery', color='green')
ax.plot(years, sci_fi_sales, marker='d', linestyle=':', linewidth=2, label='Sci-Fi', color='purple')
ax.plot(years, fantasy_sales, marker='x', linestyle='-', linewidth=2, label='Fantasy', color='red')

# Customize the chart
ax.set_title("Trends in Book Sales by Genre\nFrom 2010 to 2020", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Sales (Millions of Copies)", fontsize=12)
ax.set_xticks(years)
ax.set_xlim(2010, 2020)
ax.set_ylim(0, 45)
ax.legend(title="Genres", loc="upper left", fontsize=10, title_fontsize='13')

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Highlight a specific point to draw attention
highlight_year = 2018
highlight_fiction = fiction_sales[highlight_year - 2010]
ax.annotate(
    'Fiction peaks',
    xy=(highlight_year, highlight_fiction),
    xytext=(highlight_year-2, highlight_fiction+5),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=10,
    fontweight='bold'
)

# Make layout tight
plt.tight_layout()

# Show the plot
plt.show()