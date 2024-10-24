import numpy as np
import matplotlib.pyplot as plt

# Define months and product categories
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
categories = ['Electronics', 'Clothing', 'Home Goods', 'Toys', 'Groceries']

# Sales data: rows are product categories, columns are months
sales_data = np.array([
    [200, 150, 250, 300, 350, 400],  # Electronics
    [300, 400, 350, 250, 200, 150],  # Clothing
    [100, 200, 300, 250, 150, 100],  # Home Goods
    [50, 100, 200, 150, 300, 350],   # Toys
    [500, 450, 400, 500, 550, 600]   # Groceries
])

# Create a heatmap using imshow
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(sales_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add color bar
cbar = fig.colorbar(cax)
cbar.set_label('Sales (Units)', fontsize=12)

# Set title and labels
ax.set_title('Retail Heatmap:\nMonthly Sales Distribution Across Categories', fontsize=14, pad=20)
ax.set_xticks(np.arange(len(months)))
ax.set_yticks(np.arange(len(categories)))
ax.set_xticklabels(months, fontsize=10)
ax.set_yticklabels(categories, fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display data values on the heatmap
for i in range(len(categories)):
    for j in range(len(months)):
        ax.text(j, i, str(sales_data[i, j]), ha='center', va='center', color='black', fontsize=9, fontweight='bold')

# Enhance layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()