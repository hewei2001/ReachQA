import matplotlib.pyplot as plt

# Data Inputs for line chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fiction_sales = [1000, 1100, 1300, 1500, 1600, 1400, 
                 1300, 1450, 1600, 1700, 1900, 2000]
non_fiction_sales = [600, 650, 800, 900, 950, 850, 
                     800, 900, 1000, 1100, 1200, 1300]
childrens_books_sales = [300, 350, 450, 550, 600, 500, 
                         550, 600, 650, 750, 850, 950]
comics_sales = [400, 450, 550, 650, 700, 650, 
                700, 750, 800, 850, 1000, 1100]

# Calculating total sales per month for bar chart
total_sales = [fiction_sales[i] + non_fiction_sales[i] + childrens_books_sales[i] + comics_sales[i] 
               for i in range(len(months))]

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Plotting the line chart on ax1
ax1.plot(months, fiction_sales, marker='o', linestyle='-', label='Fiction', color='blue', linewidth=2)
ax1.plot(months, non_fiction_sales, marker='s', linestyle='--', label='Non-Fiction', color='green', linewidth=2)
ax1.plot(months, childrens_books_sales, marker='^', linestyle=':', label='Children\'s Books', color='red', linewidth=2)
ax1.plot(months, comics_sales, marker='*', linestyle='-.', label='Comics', color='magenta', linewidth=2)

# Annotating data points on line chart
for i, txt in enumerate(fiction_sales):
    ax1.text(months[i], txt, str(txt), ha='left', va='bottom')

for i, txt in enumerate(non_fiction_sales):
    ax1.text(months[i], txt, str(txt), ha='left', va='bottom')

for i, txt in enumerate(childrens_books_sales):
    ax1.text(months[i], txt, str(txt), ha='left', va='bottom')

for i, txt in enumerate(comics_sales):
    ax1.text(months[i], txt, str(txt), ha='left', va='bottom')

# Bar chart on ax2
bar_rects = ax2.bar(months, total_sales, color='skyblue')

# Annotating bar chart with total sales
for rect in bar_rects:
    height = rect.get_height()
    ax2.text(rect.get_x() + rect.get_width() / 2., 1.01 * height,
             '%d' % int(height),
             ha='center', va='bottom')

# Setting labels and title for the first subplot (line chart)
ax1.set_title('Monthly Sales Trends for an Online Bookstore\n(2023)', linespacing=2)
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (Units)')

# Setting grid for the first subplot (line chart)
ax1.grid(True)

# Enabling minor ticks for better readability in the first subplot
ax1.minorticks_on()

# Setting major and minor grid styles for the first subplot
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Rotating the x-axis labels for better readability in the first subplot
ax1.set_xticklabels(months, rotation=45)

# Setting labels and title for the second subplot (bar chart)
ax2.set_title('Total Sales by Month')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales (Units)')

# Adjusting layout to prevent labels from overlapping
plt.tight_layout()

# Displaying the legend for the first subplot
ax1.legend()

# Show the plot
plt.show()