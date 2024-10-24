import matplotlib.pyplot as plt
import numpy as np

# Define coffee beverage types and corresponding cups sold
beverages = ['Espresso', 'Cappuccino', 'Latte', 'Americano', 'Mocha', 'Flat White', 'Macchiato', 'Affogato']
cups_sold = [150, 120, 180, 90, 110, 95, 75, 60]

# Define colors, with a distinctive color for the top-selling beverage
colors = ['#b5651d', '#d2691e', '#ff7f50', '#deb887', '#cd853f', '#f4a460', '#8b4513', '#d2b48c']

# Set the color for the top-selling beverage to make it stand out
colors[np.argmax(cups_sold)] = '#ff4500'

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
bars = ax.barh(beverages, cups_sold, color=colors, edgecolor='black', height=0.6)

# Add grid lines for better readability
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, color='gray', alpha=0.7)

# Set title and labels
ax.set_title('Popular Coffee Beverages at The Urban Grind Café', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Number of Cups Sold', fontsize=12)
ax.set_ylabel('Coffee Beverage Type', fontsize=12)

# Annotate each bar with the number of cups sold
for bar in bars:
    ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2, 
            f'{int(bar.get_width())}', va='center', fontsize=10)

# Ensure labels and titles do not overlap
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()