import matplotlib.pyplot as plt
import numpy as np

# Define categories and monthly sales data (in thousands of units)
categories = ["Electronics", "Fashion", "Home & Kitchen", "Books", "Health & Beauty"]

# Sales data for each category in the first quarter of 2023
electronics_sales = [120, 130, 125, 140, 135, 128, 127, 132, 138, 122, 121, 133]
fashion_sales = [85, 95, 90, 89, 92, 94, 87, 88, 91, 86, 93, 90]
home_kitchen_sales = [150, 160, 155, 148, 162, 157, 151, 149, 163, 154, 158, 161]
books_sales = [60, 65, 63, 70, 68, 66, 62, 67, 69, 64, 61, 71]
health_beauty_sales = [110, 115, 118, 112, 120, 119, 117, 116, 121, 114, 113, 122]

# Assemble data for boxplot
data = [
    electronics_sales,
    fashion_sales,
    home_kitchen_sales,
    books_sales,
    health_beauty_sales
]

# Create cumulative sales data for line plot
cumulative_sales = {
    "Electronics": np.cumsum(electronics_sales),
    "Fashion": np.cumsum(fashion_sales),
    "Home & Kitchen": np.cumsum(home_kitchen_sales),
    "Books": np.cumsum(books_sales),
    "Health & Beauty": np.cumsum(health_beauty_sales)
}

# Create the subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Boxplot
box = axs[0].boxplot(data, notch=True, patch_artist=True,
                     boxprops=dict(facecolor="lightblue", color="blue"),
                     capprops=dict(color="blue"),
                     whiskerprops=dict(color="blue"),
                     flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'),
                     medianprops=dict(color="red"))

colors = ['#A2D9CE', '#F9E79F', '#F5B7B1', '#AED6F1', '#D2B4DE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

axs[0].set_title("Quarterly Sales Performance\nof E-commerce Categories: Q1 2023", fontsize=12, fontweight='bold')
axs[0].set_ylabel('Sales (in Thousands of Units)', fontsize=10)
axs[0].set_xticks(range(1, len(categories) + 1))
axs[0].set_xticklabels(categories, rotation=30, ha='right', fontsize=9)
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

axs[0].legend([box["boxes"][i] for i in range(len(categories))], categories, loc='upper left', fontsize=8, title="Categories")

# Line Plot
months = np.arange(1, 13)
for category, sales in cumulative_sales.items():
    axs[1].plot(months, sales, label=category, marker='o')

axs[1].set_title("Cumulative Sales Trends in Q1 2023", fontsize=12, fontweight='bold')
axs[1].set_xlabel('Month', fontsize=10)
axs[1].set_ylabel('Cumulative Sales (in Thousands)', fontsize=10)
axs[1].set_xticks(months)
axs[1].set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=45, ha='right')
axs[1].grid(True, linestyle='--', alpha=0.7)
axs[1].legend(loc='upper left', fontsize=8)

# Improve layout
plt.tight_layout()

# Show plot
plt.show()