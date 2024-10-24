import matplotlib.pyplot as plt
import numpy as np

# Define months and data for two years and three categories
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
categories = ['Men\'s Wear', 'Women\'s Wear', 'Accessories']

# Production data for 2022 and 2023
production_data_2022 = np.array([
    [100, 110, 120, 140, 135, 145, 150, 155, 160, 170, 180, 190],  # Men's Wear
    [90, 100, 110, 130, 125, 135, 140, 145, 150, 160, 170, 180],   # Women's Wear
    [60, 65, 70, 85, 80, 90, 95, 100, 110, 120, 130, 140]          # Accessories
])

production_data_2023 = np.array([
    [120, 130, 140, 160, 150, 155, 165, 170, 180, 190, 200, 210],  # Men's Wear
    [110, 120, 130, 150, 145, 155, 160, 165, 175, 185, 195, 205],  # Women's Wear
    [80, 85, 90, 105, 100, 110, 115, 120, 130, 140, 150, 160]      # Accessories
])

variability = np.array([5, 10, 5, 10, 10, 5, 10, 5, 10, 10, 5, 10])  # Standard variability

# Create subplots for each category
fig, axs = plt.subplots(len(categories), 1, figsize=(12, 15))
fig.suptitle('EcoThreads: Multi-Year Production Analysis by Category', fontsize=18, weight='bold')

# Loop over each category
for i, category in enumerate(categories):
    # Plot data for 2022 and 2023
    axs[i].errorbar(months, production_data_2022[i], yerr=variability, fmt='-o', 
                    label='2022', color='blue', ecolor='lightblue', elinewidth=2, capsize=5, markeredgewidth=2)
    axs[i].errorbar(months, production_data_2023[i], yerr=variability, fmt='-o', 
                    label='2023', color='green', ecolor='lightgreen', elinewidth=2, capsize=5, markeredgewidth=2)
    
    # Customizing each subplot
    axs[i].set_title(category, fontsize=14, pad=10)
    axs[i].set_xlabel('Month', fontsize=12)
    axs[i].set_ylabel('Average Number of Items Produced', fontsize=12)
    axs[i].grid(True, linestyle='--', alpha=0.7)
    axs[i].legend(loc='upper left', fontsize=10)

# Adjust layout to prevent overlaps
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()