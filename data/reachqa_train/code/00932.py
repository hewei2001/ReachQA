import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import MaxNLocator

# Data setup
years = np.arange(2010, 2021)
fiction_sales = [24, 26, 27, 30, 29, 31, 33, 34, 35, 37, 39]
non_fiction_sales = [19, 20, 22, 24, 23, 22, 24, 25, 27, 29, 30]
mystery_sales = [15, 16, 15, 14, 16, 18, 17, 19, 20, 22, 23]
sci_fi_sales = [12, 13, 13, 14, 15, 16, 17, 19, 18, 19, 20]
fantasy_sales = [10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 20]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Define colors and styles for each genre
colors = cm.viridis(np.linspace(0.1, 0.9, 5))
markers = ['o', 's', '^', 'd', 'x']
linestyles = ['-', '--', '-.', ':', '-']

# Plot sales data with color gradients
for idx, (sales, label) in enumerate(zip(
    [fiction_sales, non_fiction_sales, mystery_sales, sci_fi_sales, fantasy_sales],
    ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Fantasy'])):
    ax1.plot(years, sales, marker=markers[idx], linestyle=linestyles[idx], 
             linewidth=2, label=label, color=colors[idx])

# Customize the chart
ax1.set_title("Trends in Book Sales by Genre\nFrom 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (Millions of Copies)", fontsize=12)
ax1.set_xticks(years)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_xlim(2010, 2020)
ax1.set_ylim(0, 45)
ax1.legend(title="Genres", loc="upper left", fontsize=10, title_fontsize='13', frameon=False)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight specific trend points
highlight_years = [2014, 2018]
highlight_sales = [fiction_sales[highlight_years[0] - 2010], fiction_sales[highlight_years[1] - 2010]]
annotations = ['Mid-Year Dip', 'Fiction Peaks']
for year, sales, ann in zip(highlight_years, highlight_sales, annotations):
    ax1.annotate(
        ann,
        xy=(year, sales),
        xytext=(year, sales + 5),
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        fontsize=10,
        fontweight='bold'
    )

# Secondary Y-axis for percentage growth
ax2 = ax1.twinx()
fiction_growth = [0] + [((fiction_sales[i] - fiction_sales[i-1]) / fiction_sales[i-1]) * 100 if fiction_sales[i-1] > 0 else 0 for i in range(1, len(fiction_sales))]
ax2.plot(years, fiction_growth, color='grey', linestyle='--', marker='o', label='Fiction Growth %', alpha=0.5)
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='grey')
ax2.set_ylim(-10, 20)
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.spines['right'].set_color('grey')
ax2.tick_params(axis='y', colors='grey')

# Sync legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='lower right', fontsize=10, frameon=False)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()