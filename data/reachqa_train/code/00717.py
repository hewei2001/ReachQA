import matplotlib.pyplot as plt

# Define the categories and their respective market share percentages
beverage_categories = ['Coffee', 'Tea', 'Soft Drinks', 'Energy Drinks', 'Bottled Water', 'Juices', 'Alcoholic Beverages']
market_shares = [25, 20, 15, 10, 15, 5, 10]

# Define colors for each category
colors = ['#6B4226', '#C5A880', '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#FF6666']

# Explode the 'Coffee' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(market_shares, labels=beverage_categories, autopct='%1.1f%%', startangle=140, 
        colors=colors, explode=explode, shadow=True)

# Title and layout adjustments
plt.title('Beverage Consumption Preferences Worldwide\n(2023)', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  # Ensure the pie chart is circular

# Add legend for clarity, placed to the side
plt.legend(beverage_categories, title="Beverage Categories", loc='upper right', bbox_to_anchor=(1.2, 1.0))

# Automatically adjust layout to accommodate elements
plt.tight_layout()

# Display the plot
plt.show()