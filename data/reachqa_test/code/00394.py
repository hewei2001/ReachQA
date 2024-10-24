import matplotlib.pyplot as plt
import numpy as np

# Country-wise EV sales data (units)
country_sales = {
    'USA': [5000, 8000, 10000, 12000, 15000],
    'China': [8000, 12000, 15000, 18000, 20000],
    'Norway': [2000, 3000, 4000, 5000, 6000],
    'Germany': [3000, 4000, 5000, 6000, 7000],
    'Japan': [1500, 2000, 2500, 3000, 3500]
}

# Manufacturer-wise EV sales data (units)
manufacturer_sales = {
    'Tesla': [15000, 18000, 20000, 22000, 25000],
    'Volkswagen': [10000, 12000, 14000, 16000, 18000],
    'Nissan': [8000, 10000, 12000, 14000, 16000],
    'BMW': [6000, 8000, 10000, 12000, 14000],
    'Hyundai': [4000, 5000, 6000, 7000, 8000]
}

# Extract manufacturer names
manufacturers = list(manufacturer_sales.keys())

# Extract sales data for each manufacturer
sales_data = [sales[-1] for sales in manufacturer_sales.values()]

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={'width_ratios': [3, 2]})

# Set x-axis tick positions for ax1
x_pos = np.arange(len(manufacturers))

# Set bar width for ax1
width = 0.7

# Create bars for ax1
ax1.bar(x_pos, sales_data, width, color=plt.cm.tab20(np.linspace(0, 1, len(manufacturers))))

# Add text labels for ax1
for i, sales in enumerate(sales_data):
    ax1.text(x_pos[i], sales + 500, f"{sales:,}", ha='center', va='bottom', fontsize=8)

# Set axis labels and title for ax1
ax1.set_xlabel('Manufacturer')
ax1.set_ylabel('2020 EV Sales (Units)')
ax1.set_title('2020 Electric Vehicle Sales by Manufacturer\nTop 5 Performers')

# Set x-axis tick labels and rotate for better readability for ax1
ax1.set_xticks(x_pos)
ax1.set_xticklabels(manufacturers, rotation=45, ha='right')

# Add grid lines for y-axis for ax1
ax1.grid(axis='y', linestyle='--')

# Create lines for ax2
years = list(range(2016, 2021))
for country, sales in country_sales.items():
    ax2.plot(years, sales, label=country, marker='o')

# Set axis labels and title for ax2
ax2.set_xlabel('Year')
ax2.set_ylabel('EV Sales (Units)')
ax2.set_title('Electric Vehicle Sales by Country')

# Add legend for ax2
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Automatically adjust the layout
fig.tight_layout()

# Display the plot
plt.show()