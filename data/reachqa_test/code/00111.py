import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart (in thousands of units)
colonies = ['Luna', 'Mars', 'Titan', 'Europa', 'Ceres']
milk_chocolate_sales = [25, 30, 22, 28, 20]
dark_chocolate_sales = [15, 18, 16, 14, 10]
white_chocolate_sales = [10, 8, 12, 11, 9]

# Data for the line chart (total annual sales per colony in thousands)
months = np.arange(1, 13)
luna_sales = [5, 7, 9, 8, 10, 12, 11, 10, 9, 7, 5, 6]
mars_sales = [8, 9, 11, 12, 14, 15, 16, 14, 13, 11, 10, 9]
titan_sales = [6, 7, 8, 7, 9, 11, 12, 10, 9, 8, 7, 6]
europa_sales = [7, 6, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7]
ceres_sales = [4, 5, 6, 5, 7, 8, 9, 8, 7, 6, 5, 4]

# Plot setup
fig, axes = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1.2, 1]})
fig.suptitle('The Great Galactic Chocolate Sale 2123', fontsize=16, weight='bold')

# Bar Chart
ax1 = axes[0]
x = np.arange(len(colonies))
width = 0.25

bars1 = ax1.bar(x - width, milk_chocolate_sales, width, label='Milk Chocolate', color='#f5cba7')
bars2 = ax1.bar(x, dark_chocolate_sales, width, label='Dark Chocolate', color='#6c3483')
bars3 = ax1.bar(x + width, white_chocolate_sales, width, label='White Chocolate', color='#f7f9f9')

# Annotate bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        ax1.annotate(f'{bar.get_height()}k',
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 3),
                     textcoords='offset points', ha='center', va='bottom', fontsize=9)

ax1.set_title('Sales in Space Colonies', fontsize=12)
ax1.set_xlabel('Space Colonies', fontsize=10)
ax1.set_ylabel('Units Sold (thousands)', fontsize=10)
ax1.set_xticks(x)
ax1.set_xticklabels(colonies)
ax1.legend(title='Chocolate Types')
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)

# Line Chart
ax2 = axes[1]

ax2.plot(months, luna_sales, marker='o', label='Luna', color='#e74c3c')
ax2.plot(months, mars_sales, marker='s', label='Mars', color='#3498db')
ax2.plot(months, titan_sales, marker='^', label='Titan', color='#2ecc71')
ax2.plot(months, europa_sales, marker='D', label='Europa', color='#9b59b6')
ax2.plot(months, ceres_sales, marker='x', label='Ceres', color='#f1c40f')

ax2.set_title('Monthly Sales Trends (2023)', fontsize=12)
ax2.set_xlabel('Month', fontsize=10)
ax2.set_ylabel('Total Units Sold (thousands)', fontsize=10)
ax2.set_xticks(months)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.legend(title='Space Colonies', fontsize=9)
ax2.grid(True, linestyle='--', which='major', color='grey', alpha=0.25)

# Ensure no overlaps and tidy layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the charts
plt.show()