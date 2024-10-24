import matplotlib.pyplot as plt
import numpy as np

# Define seasons
seasons = [
    "Spring '21", "Summer '21", "Autumn '21", "Winter '21",
    "Spring '22", "Summer '22", "Autumn '22", "Winter '22",
    "Spring '23", "Summer '23", "Autumn '23", "Winter '23"
]

# Average price data for each season for three brands
brand_a_prices = np.array([22, 24, 23, 25, 26, 28, 27, 30, 31, 33, 32, 34])
brand_b_prices = np.array([20, 21, 22, 21, 22, 24, 23, 26, 25, 27, 28, 29])
brand_c_prices = np.array([19, 20, 20, 22, 23, 25, 24, 27, 26, 28, 29, 31])

# Error margins
brand_a_errors = np.array([1.2, 1.5, 1.0, 1.3, 1.4, 1.6, 1.1, 1.8, 1.7, 1.5, 1.3, 1.2])
brand_b_errors = np.array([1.0, 1.1, 0.9, 1.0, 1.2, 1.3, 1.1, 1.4, 1.3, 1.2, 1.1, 1.0])
brand_c_errors = np.array([0.9, 1.0, 0.8, 1.1, 1.2, 1.4, 1.0, 1.5, 1.3, 1.1, 1.0, 0.9])

# Sales volume data (in thousands)
brand_a_sales = np.array([150, 160, 170, 175, 180, 190, 185, 195, 200, 210, 205, 215])
brand_b_sales = np.array([140, 145, 155, 150, 158, 165, 160, 170, 168, 175, 178, 185])
brand_c_sales = np.array([135, 140, 145, 148, 150, 155, 152, 160, 158, 162, 165, 172])

# Convert seasons into numerical format for x-axis
x_indexes = np.arange(len(seasons))
bar_width = 0.2

# Plotting the data
fig, ax1 = plt.subplots(figsize=(16, 9))

# Plot each brand with error bars
ax1.errorbar(
    x_indexes, brand_a_prices, yerr=brand_a_errors, label='Brand A Price',
    fmt='-o', capsize=5, color='#FF5733', elinewidth=2, markerfacecolor='white', alpha=0.8
)
ax1.errorbar(
    x_indexes, brand_b_prices, yerr=brand_b_errors, label='Brand B Price',
    fmt='-s', capsize=5, color='#33FF57', elinewidth=2, markerfacecolor='white', alpha=0.8
)
ax1.errorbar(
    x_indexes, brand_c_prices, yerr=brand_c_errors, label='Brand C Price',
    fmt='-d', capsize=5, color='#3357FF', elinewidth=2, markerfacecolor='white', alpha=0.8
)

# Add a secondary axis for sales volume
ax2 = ax1.twinx()
ax2.bar(x_indexes - bar_width, brand_a_sales, width=bar_width, label='Brand A Sales', color='#FFC300', alpha=0.6)
ax2.bar(x_indexes, brand_b_sales, width=bar_width, label='Brand B Sales', color='#DAF7A6', alpha=0.6)
ax2.bar(x_indexes + bar_width, brand_c_sales, width=bar_width, label='Brand C Sales', color='#C70039', alpha=0.6)

# Set titles and labels
ax1.set_title('Variability in Designer Coffee Prices & Sales Volumes\nOver Seasons (2021-2023)', fontsize=16, fontweight='bold', loc='center')
ax1.set_xlabel('Seasons', fontsize=12)
ax1.set_ylabel('Average Price per Pound ($)', fontsize=12)
ax2.set_ylabel('Sales Volume (in thousands)', fontsize=12)

# Customize x-axis
ax1.set_xticks(x_indexes)
ax1.set_xticklabels(seasons, rotation=45, ha='right')
ax1.grid(True, linestyle='--', alpha=0.7)

# Add legends
ax1.legend(loc='upper left', title='Price Data', fontsize=10)
ax2.legend(loc='upper right', title='Sales Volume', fontsize=10)

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()