import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Data for coffee beverages consumption over the years
espresso = [50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 95]
latte = [40, 45, 50, 55, 60, 66, 70, 76, 80, 85, 90]
cappuccino = [30, 35, 40, 42, 45, 50, 55, 58, 60, 65, 70]
cold_brew = [10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 70]

# Average price data (hypothetical, in dollars) for the same beverages
prices = {
    'Espresso': [2.5, 2.7, 2.8, 2.9, 3.0, 3.2, 3.3, 3.5, 3.6, 3.7, 3.8],
    'Latte': [3.0, 3.1, 3.2, 3.4, 3.5, 3.6, 3.8, 3.9, 4.0, 4.1, 4.2],
    'Cappuccino': [2.8, 2.9, 3.0, 3.1, 3.3, 3.4, 3.6, 3.7, 3.9, 4.0, 4.1],
    'Cold Brew': [3.5, 3.6, 3.7, 3.8, 4.0, 4.1, 4.3, 4.5, 4.6, 4.8, 5.0]
}

# Combine the data into a list for stacking
beverages = np.array([espresso, latte, cappuccino, cold_brew])

# Create a figure and axis for the plot
fig, ax1 = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax1.stackplot(years, beverages, labels=['Espresso', 'Latte', 'Cappuccino', 'Cold Brew'],
              colors=['#8B4513', '#D2B48C', '#DEB887', '#A52A2A'], alpha=0.8)

# Set title and labels for the consumption plot
ax1.set_title("The Rise of Coffee Beverage Consumption and Price Trends\nFrom 2013 to 2023", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Consumption (in millions)', fontsize=12, color='black')

# Add grid lines for better readability
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Create a second y-axis for the price data
ax2 = ax1.twinx()
for beverage, price_data in prices.items():
    ax2.plot(years, price_data, label=f'{beverage} Price', linestyle='--', marker='o')

# Set ylabel for the price plot
ax2.set_ylabel('Average Price (in dollars)', fontsize=12, color='black')

# Add legends
ax1.legend(loc='upper left', fontsize=10, title='Consumption Type', bbox_to_anchor=(1, 1))
ax2.legend(loc='upper left', fontsize=10, title='Price Trend', bbox_to_anchor=(1, 0.85))

# Customize x-axis tick labels to avoid overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()