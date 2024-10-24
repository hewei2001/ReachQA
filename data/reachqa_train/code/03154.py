import matplotlib.pyplot as plt
import numpy as np

# Define the months and corresponding average production with variability
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_production = np.array([120, 130, 140, 160, 150, 155, 165, 170, 180, 190, 200, 210])
production_variability = np.array([10, 15, 10, 20, 15, 10, 15, 10, 20, 15, 10, 15])

# Create the plot
plt.figure(figsize=(12, 6))
plt.errorbar(months, average_production, yerr=production_variability, fmt='-o', 
             color='green', ecolor='lightgray', elinewidth=2, capsize=5, markeredgewidth=2)

# Customize the chart
plt.title('EcoThreads: Monthly Sustainable Fashion Production\nin 2023', fontsize=16, weight='bold', pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Number of Items Produced', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Add a legend
plt.legend(['Average Production ± Variability'], loc='upper left', fontsize=10)

# Ensure the layout is adjusted to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()