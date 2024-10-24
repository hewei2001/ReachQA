import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = [str(year) for year in range(2011, 2021)]

# E-book sales data (in millions) for each genre over the years
fiction_sales = np.array([10, 12, 13, 15, 17, 19, 21, 24, 26, 28])
non_fiction_sales = np.array([8, 9, 11, 13, 15, 18, 21, 25, 28, 32])
sci_fi_sales = np.array([3, 4, 6, 9, 12, 16, 21, 27, 34, 42])
mystery_sales = np.array([5, 6, 7, 9, 10, 12, 15, 18, 22, 25])
romance_sales = np.array([6, 7, 8, 10, 13, 15, 18, 22, 25, 30])

# Stack the data
sales_data = np.array([fiction_sales, non_fiction_sales, sci_fi_sales, mystery_sales, romance_sales])

# Define genre labels and colors
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Mystery', 'Romance']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Position of bars on x-axis
ind = np.arange(len(years))

# Define the width of bars
width = 0.65

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each genre's data as stacked bars
p1 = ax.bar(ind, fiction_sales, width, label='Fiction', color=colors[0])
p2 = ax.bar(ind, non_fiction_sales, width, bottom=fiction_sales, label='Non-Fiction', color=colors[1])
p3 = ax.bar(ind, sci_fi_sales, width, bottom=fiction_sales + non_fiction_sales, label='Science Fiction', color=colors[2])
p4 = ax.bar(ind, mystery_sales, width, bottom=fiction_sales + non_fiction_sales + sci_fi_sales, label='Mystery', color=colors[3])
p5 = ax.bar(ind, romance_sales, width, bottom=fiction_sales + non_fiction_sales + sci_fi_sales + mystery_sales, label='Romance', color=colors[4])

# Calculate total sales for each year
total_sales = fiction_sales + non_fiction_sales + sci_fi_sales + mystery_sales + romance_sales

# Overlay line plot for total sales
ax.plot(ind, total_sales, color='red', marker='o', linewidth=2, label='Total Sales')

# Titles and labels
ax.set_title('E-Book Sales Growth in Various Genres\nand Overall Trend (2011-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('E-book Sales (Millions)', fontsize=14)

# x-axis ticks and labels
ax.set_xticks(ind)
ax.set_xticklabels(years, fontsize=12, rotation=45)

# Add a legend to the chart
ax.legend(title='Genres & Total', loc='upper left', fontsize=12)

# Add value labels on the bars
for i in range(len(years)):
    ax.text(i, fiction_sales[i]/2, str(fiction_sales[i]), ha='center', va='center', color='black', fontsize=10)
    ax.text(i, fiction_sales[i] + non_fiction_sales[i]/2, str(non_fiction_sales[i]), ha='center', va='center', color='black', fontsize=10)
    ax.text(i, fiction_sales[i] + non_fiction_sales[i] + sci_fi_sales[i]/2, str(sci_fi_sales[i]), ha='center', va='center', color='black', fontsize=10)
    ax.text(i, fiction_sales[i] + non_fiction_sales[i] + sci_fi_sales[i] + mystery_sales[i]/2, str(mystery_sales[i]), ha='center', va='center', color='black', fontsize=10)
    ax.text(i, fiction_sales[i] + non_fiction_sales[i] + sci_fi_sales[i] + mystery_sales[i] + romance_sales[i]/2, str(romance_sales[i]), ha='center', va='center', color='black', fontsize=10)
    ax.text(i, total_sales[i] + 1, str(total_sales[i]), ha='center', va='center', color='red', fontsize=10, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()