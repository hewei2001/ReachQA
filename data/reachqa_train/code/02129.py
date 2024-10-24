import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2013 to 2023
years = np.arange(2013, 2024)

# Create data for different coffee beverages over the years
espresso = [50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 95]
latte = [40, 45, 50, 55, 60, 66, 70, 76, 80, 85, 90]
cappuccino = [30, 35, 40, 42, 45, 50, 55, 58, 60, 65, 70]
cold_brew = [10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 70]

# Combine the data into a list for stacking
beverages = np.array([espresso, latte, cappuccino, cold_brew])

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the stacked area chart
ax.stackplot(years, beverages, labels=['Espresso', 'Latte', 'Cappuccino', 'Cold Brew'],
             colors=['#8B4513', '#D2B48C', '#DEB887', '#A52A2A'], alpha=0.8)

# Set title and labels
ax.set_title("The Rise of Coffee Beverage Consumption\nFrom 2013 to 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Consumption (in millions)', fontsize=12)

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=10, title='Coffee Type', bbox_to_anchor=(1, 1))

# Add grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Customize x-axis tick labels to avoid overlap
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()