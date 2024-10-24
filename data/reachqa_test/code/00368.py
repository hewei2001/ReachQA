import matplotlib.pyplot as plt
import numpy as np

# Data
years = list(range(2010, 2030))  # Expanded years from 2010 to 2029
markets = ['United States', 'China', 'Europe', 'Japan', 'South Korea', 'India']  # Added two new markets
sales_data = {
    'United States': [5000, 10000, 20000, 35000, 50000, 70000, 90000, 120000, 150000, 180000, 200000, 220000, 250000, 280000, 300000, 350000, 400000, 450000, 500000, 550000],
    'China': [2000, 5000, 10000, 25000, 50000, 80000, 120000, 180000, 250000, 350000, 450000, 550000, 650000, 750000, 850000, 950000, 1050000, 1150000, 1250000, 1350000],
    'Europe': [3000, 6000, 12000, 25000, 40000, 60000, 90000, 120000, 150000, 180000, 210000, 240000, 270000, 300000, 330000, 360000, 390000, 420000, 450000, 480000],
    'Japan': [1000, 2000, 4000, 8000, 15000, 25000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000],
    'South Korea': [500, 1000, 2000, 4000, 8000, 12000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000],
    'India': [200, 500, 1000, 2000, 4000, 8000, 15000, 30000, 50000, 80000, 120000, 160000, 200000, 240000, 280000, 320000, 360000, 400000, 440000, 480000]
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the line charts
for i, market in enumerate(markets):
    ax.plot(years, sales_data[market], label=market, marker=['o', 's', 'D', '^', 'x', 'p'][i], 
            linestyle=['-', '--', '-.', (0, (3, 5, 1, 5))][i % 4], linewidth=2, color=['C0', 'C1', 'C2', 'C3', 'C4', 'C5'][i])

# Customize the chart
ax.set_title("The Rise of Electric Vehicles:\nComparative Analysis of Sales Trends in Major Markets (2010-2029)\n")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Electric Vehicles Sold")

# Ensure ticks are aligned with the years and improve readability
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Add gridlines and customize layout
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), fontsize=12)

# Adjust layout to ensure nothing overlaps
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()