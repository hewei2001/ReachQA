import matplotlib.pyplot as plt
import numpy as np

# Shipping times data (in days)
standard_shipping_times = [5, 5, 6, 7, 5, 6, 7, 7, 8, 5, 6, 5, 7, 6, 8, 5, 6, 7, 5, 6, 8, 9, 5, 6, 7, 7, 6, 5, 6, 8, 5, 6, 7, 8, 6]
express_shipping_times = [1, 2, 1, 1, 2, 1, 2, 3, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 3, 1, 1, 2, 2, 1, 1, 1, 2, 1, 3, 1]

# Plotting the histogram
fig, ax = plt.subplots(figsize=(12, 7))

# Define the number of bins and range for the histogram
bins = np.arange(0, 11) - 0.5  # Creates bins centered on integers

# Plot the histograms for each delivery type
ax.hist(standard_shipping_times, bins=bins, alpha=0.7, label='Standard Shipping', color='#3498db', edgecolor='black')
ax.hist(express_shipping_times, bins=bins, alpha=0.7, label='Express Shipping', color='#e74c3c', edgecolor='black')

# Title and labels
ax.set_title('Distribution of E-commerce Shipping Times\n(Orders from Last Month)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Shipping Time (Days)', fontsize=12)
ax.set_ylabel('Number of Orders', fontsize=12)

# Customize the x-ticks to show days
ax.set_xticks(range(0, 11))
ax.set_xlim([0, 10])

# Add a legend to differentiate between shipping methods
ax.legend(loc='upper right', fontsize=12)

# Grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()