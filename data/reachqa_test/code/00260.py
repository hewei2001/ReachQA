import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2015, 2026)
fiction_sales = [20, 25, 27, 30, 35, 33, 40, 45, 47, 50, 52]
nonfiction_sales = [15, 18, 20, 22, 25, 28, 32, 35, 37, 39, 42]
sci_tech_sales = [10, 12, 15, 18, 21, 23, 26, 28, 30, 34, 37]

# Total sales for each year
total_sales = np.array(fiction_sales) + np.array(nonfiction_sales) + np.array(sci_tech_sales)

# Plot setup
plt.style.use('ggplot')  # Use a valid Matplotlib style name
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Subplot 1: Line chart for individual genres
axes[0].plot(years, fiction_sales, marker='o', linestyle='-', color='c', linewidth=2, label='Fiction')
axes[0].plot(years, nonfiction_sales, marker='s', linestyle='-', color='m', linewidth=2, label='Non-Fiction')
axes[0].plot(years, sci_tech_sales, marker='^', linestyle='-', color='y', linewidth=2, label='Science & Technology')

# Annotate significant points only
for year, fiction, nonfiction, sci_tech in zip(years, fiction_sales, nonfiction_sales, sci_tech_sales):
    if year == 2025:  # Example condition for significant points
        axes[0].annotate(f"{fiction}", (year, fiction + 0.5), fontsize=9, color='c', ha='center')
        axes[0].annotate(f"{nonfiction}", (year, nonfiction + 0.5), fontsize=9, color='m', ha='center')
        axes[0].annotate(f"{sci_tech}", (year, sci_tech + 0.5), fontsize=9, color='y', ha='center')

axes[0].set_title('E-book Sales by Genre (2015-2025)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Sales (Millions)', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].legend(title="Genres", fontsize=11, title_fontsize='13')
axes[0].set_xticks(years)
axes[0].tick_params(axis='x', rotation=45)

# Subplot 2: Bar chart for total sales
axes[1].bar(years, total_sales, color='skyblue', edgecolor='black')
for year, total in zip(years, total_sales):
    axes[1].annotate(f"{total}", (year, total + 2), fontsize=9, ha='center', color='blue')

axes[1].set_title('Total E-book Sales (2015-2025)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Total Sales (Millions)', fontsize=12)
axes[1].grid(True, linestyle='--', alpha=0.6)
axes[1].set_xticks(years)
axes[1].tick_params(axis='x', rotation=45)

plt.suptitle('E-book Sales Trends and Insights (2015-2025)', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()