import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Hypothetical global ice cream sales data (billion USD)
ice_cream_sales = np.array([
    10, 10.5, 11, 11.2, 11.8, 12.3, 13, 13.5, 14, 14.2, 
    15, 15.5, 16, 16.8, 17.3, 18, 18.5, 19, 19.7, 20, 
    20.5, 21, 21.5, 22, 22.3, 22.8, 23.5, 24, 24.5, 25, 
    25.5
])

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(years, ice_cream_sales, color='orange', marker='o', linestyle='-', linewidth=2, markersize=6, label='Ice Cream Sales (Billion USD)')

# Highlight specific data points with annotations
highlight_indices = [0, 10, 20, 30]  # Corresponds to years: 1990, 2000, 2010, 2020
for i in highlight_indices:
    plt.annotate(
        f'{ice_cream_sales[i]:.1f} B USD',
        (years[i], ice_cream_sales[i]),
        textcoords="offset points",
        xytext=(-5, 10),
        ha='center',
        fontsize=10,
        color='blue',
        bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgray', alpha=0.5)
    )

# Set labels and title
plt.title('Impact of Climate Change on Global Ice Cream Sales\nFrom 1990 to 2020', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Cream Sales (Billion USD)', fontsize=12)
plt.xticks(years[::2], rotation=45)  # Show every other year to reduce clutter
plt.yticks(np.arange(10, 26, 2))

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Add a legend to identify the data line
plt.legend(loc='upper left', fontsize=10)

# Automatically adjust layout to fit elements properly
plt.tight_layout()

# Show the plot
plt.show()