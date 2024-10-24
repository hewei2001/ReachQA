import matplotlib.pyplot as plt
import numpy as np

# Define the years for the analysis
years = np.arange(2010, 2023)

# Artificial data for bicycle sales (in thousands)
road_bikes = [15, 16, 17, 19, 20, 23, 25, 26, 27, 26, 26, 27, 28]
mountain_bikes = [10, 11, 13, 15, 18, 20, 22, 25, 23, 22, 23, 24, 25]
hybrid_bikes = [8, 9, 10, 12, 13, 15, 16, 18, 20, 21, 22, 23, 24]
electric_bikes = [1, 2, 4, 5, 7, 9, 10, 15, 20, 25, 30, 35, 40]
gravel_bikes = [0, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]

# Average selling price data for the new y-axis
avg_price = [1000, 1050, 1025, 1080, 1100, 1150, 1200, 1300, 1350, 1400, 1450, 1500, 1550]

# Combine the data for plotting
bicycle_sales_data = np.array([road_bikes, mountain_bikes, hybrid_bikes, electric_bikes, gravel_bikes])
bicycle_types = ['Road Bikes', 'Mountain Bikes', 'Hybrid Bikes', 'Electric Bikes', 'Gravel Bikes']
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Create figure and axis for the bar chart
fig, ax1 = plt.subplots(figsize=(14, 9))
ax2 = ax1.twinx()  # Secondary y-axis for average price

# Calculate bar width and positions
bar_width = 0.15
x = np.arange(len(years))

# Plot each type of bicycle data with annotations
for i in range(len(bicycle_types)):
    bars = ax1.bar(x + i * bar_width, bicycle_sales_data[i], width=bar_width, color=colors[i], label=bicycle_types[i])
    ax1.bar_label(bars, padding=2, fontsize=8, color='black')

# Plot total sales line
total_sales = bicycle_sales_data.sum(axis=0)
ax1.plot(x + bar_width * 2.5, total_sales, marker='o', color='black', linewidth=2, label='Total Sales')

# Plot average selling price on the secondary y-axis
ax2.plot(x + bar_width * 2.5, avg_price, marker='x', color='darkblue', linestyle='--', label='Average Price ($)', linewidth=2)

# Add titles and labels
ax1.set_title('Bicycle Sales in Cyclopolis\n2010-2022: Sales by Type and Average Prices', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Sales in Thousands', fontsize=12)
ax2.set_ylabel('Average Price ($)', fontsize=12)

# Customize x-axis with year labels
ax1.set_xticks(x + bar_width * 2)
ax1.set_xticklabels(years, fontsize=10)

# Add a legend to differentiate the bicycle types and total sales
ax1.legend(loc='upper left', title='Bicycle Type & Sales', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Add gridlines for better readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()