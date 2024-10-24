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

# Error margins reflecting variability
brand_a_errors = np.array([1.2, 1.5, 1.0, 1.3, 1.4, 1.6, 1.1, 1.8, 1.7, 1.5, 1.3, 1.2])
brand_b_errors = np.array([1.0, 1.1, 0.9, 1.0, 1.2, 1.3, 1.1, 1.4, 1.3, 1.2, 1.1, 1.0])
brand_c_errors = np.array([0.9, 1.0, 0.8, 1.1, 1.2, 1.4, 1.0, 1.5, 1.3, 1.1, 1.0, 0.9])

# Convert seasons into numerical format for x-axis
x_indexes = np.arange(len(seasons))

# Plotting the data
plt.figure(figsize=(14, 8))

# Plot each brand with error bars
plt.errorbar(
    x_indexes, brand_a_prices, yerr=brand_a_errors, label='Brand A',
    fmt='-o', capsize=5, color='#FF5733', elinewidth=2, markerfacecolor='white', alpha=0.8
)
plt.errorbar(
    x_indexes, brand_b_prices, yerr=brand_b_errors, label='Brand B',
    fmt='-s', capsize=5, color='#33FF57', elinewidth=2, markerfacecolor='white', alpha=0.8
)
plt.errorbar(
    x_indexes, brand_c_prices, yerr=brand_c_errors, label='Brand C',
    fmt='-d', capsize=5, color='#3357FF', elinewidth=2, markerfacecolor='white', alpha=0.8
)

# Set titles and labels
plt.title('Variability in Designer Coffee Prices Over Seasons\n(2021-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Seasons', fontsize=12)
plt.ylabel('Average Price per Pound ($)', fontsize=12)

# Customize x-axis
plt.xticks(ticks=x_indexes, labels=seasons, rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)

# Add a legend
plt.legend(title='Coffee Brands', fontsize=10, loc='upper left')

# Adjust layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()