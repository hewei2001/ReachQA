import matplotlib.pyplot as plt
import numpy as np

# Define product categories and their respective average monthly sales data
categories = ["Electronics", "Fashion", "Home & Kitchen", "Books", "Health & Beauty", "Sports & Outdoors"]
monthly_sales = np.array([120, 90, 150, 60, 70, 110])  # in thousands of dollars

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for the bars
colors = ['#FF5733', '#33FFCE', '#FF33A1', '#335BFF', '#B833FF', '#33FF57']

# Plot the bar chart
bars = ax.bar(categories, monthly_sales, color=colors)

# Set the chart title and axis labels
ax.set_title('Average Monthly Sales by Product Category\non ShopEase (in Thousands of Dollars)', fontsize=16, fontweight='bold')
ax.set_xlabel('Product Categories', fontsize=12)
ax.set_ylabel('Sales (in $K)', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Annotate each bar with the sales figure
for bar, sale in zip(bars, monthly_sales):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f"${sale}K", ha='center', va='bottom', fontsize=10, color='black')

# Add gridlines to the y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the plot
plt.show()