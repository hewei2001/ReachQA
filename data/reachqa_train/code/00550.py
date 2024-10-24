import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Average monthly active users (in thousands) over a year
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])

# Error values to represent variability in user activity
user_variability = np.array([2, 1.5, 3, 2.5, 4, 3, 5, 4, 3.5, 2.5, 4, 2])

# Setting up the plot
plt.figure(figsize=(14, 8))

# Plotting the line chart with error bars
plt.errorbar(months, average_users, yerr=user_variability, fmt='-o', label='Average MAU', 
             color='darkorange', capsize=5, alpha=0.8, elinewidth=2, markerfacecolor='white')

# Titles and labels
plt.title('Growth of Monthly Active Users on ChatterBuzz:\nA Year in Review', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Monthly Active Users (in thousands)', fontsize=12)

# Customize axes for improved visibility
plt.ylim(15, 55)
plt.xticks(fontsize=10)
plt.yticks(np.arange(15, 60, 5), fontsize=10)

# Adding a legend
plt.legend(title='Metrics', fontsize=10, loc='upper left')

# Add grid for better readability
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()