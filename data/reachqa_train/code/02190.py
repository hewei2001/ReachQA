import matplotlib.pyplot as plt
import numpy as np

# Define the months of the year
months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

# Average writing hours per week for each month
average_hours = np.array([20, 22, 25, 24, 27, 26, 28, 30, 29, 26, 25, 24])

# Standard deviation representing the variance in writing hours
std_devs = np.array([3, 4, 3.5, 4.5, 4, 3.2, 3.8, 4.1, 3.9, 4.2, 4, 3.5])

# Convert months to a numerical scale for plotting
x_values = np.arange(len(months))

# Create the line chart with error bars
plt.figure(figsize=(12, 8))
plt.errorbar(
    x_values, average_hours, yerr=std_devs, fmt='-o', color='#1f77b4',
    ecolor='lightcoral', elinewidth=2, capsize=4, alpha=0.8,
    label='Average Weekly Hours'
)

# Customize the chart
plt.title('Writing Habits of Authors in 2023\nAverage Weekly Writing Hours', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Writing Hours Per Week', fontsize=14)
plt.xticks(x_values, months, rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(15, 35)

# Add a legend
plt.legend(loc='upper left', fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for visual clarity
plt.tight_layout()

# Display the plot
plt.show()