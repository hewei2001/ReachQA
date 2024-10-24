import matplotlib.pyplot as plt
import numpy as np

# Define the clothing categories
categories = ['Tops', 'Bottoms', 'Dresses', 'Outerwear', 'Accessories']

# Define the sales seasons
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# Create a 2D array for sales data
sales_data = np.array([
    [200, 250, 180, 150],  # Tops
    [180, 200, 220, 250],  # Bottoms
    [150, 180, 200, 220],  # Dresses
    [100, 120, 150, 180],  # Outerwear
    [80, 100, 120, 150]   # Accessories
])

# Calculate total sales by season
total_sales = np.sum(sales_data, axis=0)

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})

# Plot the heatmap in the first subplot
im = axs[0].imshow(sales_data, cmap='RdYlGn', aspect='auto', interpolation='nearest')
axs[0].set_title('Sales Trends Across Clothing Categories and Seasons')
axs[0].set_xlabel('Seasons')
axs[0].set_ylabel('Clothing Categories')
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_xticklabels(seasons, rotation=45, ha='right')
axs[0].set_yticks(np.arange(len(categories)))
axs[0].set_yticklabels(categories)
for i in range(len(categories)):
    for j in range(len(seasons)):
        axs[0].text(j, i, sales_data[i, j], ha='center', va='center', color='black')
fig.colorbar(im, ax=axs[0], shrink=0.6, label='Sales Figures')

# Plot the line plot in the second subplot
axs[1].plot(seasons, total_sales, marker='o')
axs[1].set_title('Total Sales by Season')
axs[1].set_xlabel('Seasons')
axs[1].set_ylabel('Total Sales')
axs[1].grid(True)

# Adjust layout to avoid overlap
fig.tight_layout()

# Show the plot
plt.show()