import matplotlib.pyplot as plt
import numpy as np

# Expanded data with multiple years and more genres
years = [2021, 2022, 2023]
genres = [
    'Fiction', 'Non-Fiction', 'Fantasy', 'Science Fiction', 
    'Mystery', 'Historical', 'Biography', 'Romance', 'Horror'
]
sales_data = {
    2021: [1400, 1100, 750, 950, 1050, 550, 300, 800, 400],
    2022: [1500, 1200, 800, 1000, 1100, 600, 400, 900, 500],
    2023: [1600, 1300, 850, 1050, 1150, 650, 500, 950, 600]
}

# Define a color map for consistent genre coloring across years
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33C4', '#33FFC4', '#FFC300', '#C70039', '#900C3F']

# Create a bar chart for each year
fig, ax = plt.subplots(figsize=(14, 10))
width = 0.25
x = np.arange(len(genres))

for i, year in enumerate(years):
    sales = sales_data[year]
    ax.bar(x + i*width, sales, width=width, color=colors, label=f'{year}', edgecolor='black')

# Annotate the bars with the number of books sold
for i, year in enumerate(years):
    sales = sales_data[year]
    for j, books in enumerate(sales):
        ax.text(j + i*width, books + 30, f'{books}', ha='center', fontsize=9, fontweight='bold', color='black')

# Title and labels
ax.set_title('Annual Grand Book Festival\nGenre Sales Comparison (2021-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Genres', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Books Sold', fontsize=12, labelpad=10)

# Customize ticks
ax.set_xticks(x + width)
ax.set_xticklabels(genres, rotation=45, ha='right', fontsize=11)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Legend
ax.legend(title='Year', title_fontsize='13', fontsize='11', loc='upper left', bbox_to_anchor=(1, 1))

# Set a tighter layout for the plot
plt.tight_layout()

# Display the chart
plt.show()