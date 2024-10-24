import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(range(1, 13))

# Coffee consumption data (in cups) for Espresso and French Press
espresso_consumption = np.array([210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320])
french_press_consumption = np.array([190, 200, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295])

# Error margins representing the uncertainty in consumption data (in cups)
espresso_errors = np.array([10, 15, 10, 12, 8, 15, 13, 14, 9, 11, 10, 8])
french_press_errors = np.array([12, 8, 11, 9, 10, 14, 12, 15, 8, 13, 9, 10])

# Plotting the line chart with error bars
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data with error bars for each method
ax.errorbar(months, espresso_consumption, yerr=espresso_errors, label='Espresso',
            capsize=5, marker='o', linestyle='-', color='#2b8cbe', alpha=0.9)
ax.errorbar(months, french_press_consumption, yerr=french_press_errors, label='French Press',
            capsize=5, marker='s', linestyle='--', color='#fdae61', alpha=0.9)

# Customize plot aesthetics
ax.set_title("Trends in Seasonal Coffee Consumption: Monthly Variability\nEspresso vs. French Press (2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Consumption (Cups)", fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.legend(title="Brewing Method", loc='upper left')
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the completed chart
plt.show()