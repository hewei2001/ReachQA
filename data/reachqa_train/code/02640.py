import matplotlib.pyplot as plt

# Define categories and monthly sales data (in thousands of units)
categories = ["Electronics", "Fashion", "Home & Kitchen", "Books", "Health & Beauty"]

# Sales data for each category in the first quarter of 2023
electronics_sales = [120, 130, 125, 140, 135, 128, 127, 132, 138, 122, 121, 133]
fashion_sales = [85, 95, 90, 89, 92, 94, 87, 88, 91, 86, 93, 90]
home_kitchen_sales = [150, 160, 155, 148, 162, 157, 151, 149, 163, 154, 158, 161]
books_sales = [60, 65, 63, 70, 68, 66, 62, 67, 69, 64, 61, 71]
health_beauty_sales = [110, 115, 118, 112, 120, 119, 117, 116, 121, 114, 113, 122]

# Assemble data into a list for boxplot
data = [
    electronics_sales,
    fashion_sales,
    home_kitchen_sales,
    books_sales,
    health_beauty_sales
]

# Create the boxplot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the boxplot with additional styling
box = ax.boxplot(data, notch=True, patch_artist=True,
                 boxprops=dict(facecolor="lightblue", color="blue"),
                 capprops=dict(color="blue"),
                 whiskerprops=dict(color="blue"),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'),
                 medianprops=dict(color="red"))

# Setting face colors of the boxes with different shades for visualization
colors = ['#A2D9CE', '#F9E79F', '#F5B7B1', '#AED6F1', '#D2B4DE']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize the plot
ax.set_title("Quarterly Sales Performance\nof E-commerce Categories: Q1 2023", fontsize=14, fontweight='bold')
ax.set_ylabel('Sales (in Thousands of Units)', fontsize=12)
ax.set_xticks(range(1, len(categories) + 1))
ax.set_xticklabels(categories, rotation=30, ha='right', fontsize=11)

# Display the grid for better readability
ax.yaxis.grid(True, linestyle='--', which='both', alpha=0.7)

# Add a legend for clarity, focused on category coloring
ax.legend([box["boxes"][i] for i in range(len(categories))], categories, loc='upper left', fontsize=9, title="Categories")

# Improve layout
plt.tight_layout()

# Show plot
plt.show()