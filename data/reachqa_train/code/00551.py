import matplotlib.pyplot as plt
import numpy as np

# Data preparation
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])
user_variability = np.array([2, 1.5, 3, 2.5, 4, 3, 5, 4, 3.5, 2.5, 4, 2])

# Additional dataset for cumulative users
cumulative_users = np.cumsum(average_users)

# Percentage growth calculation
percentage_growth = np.append([0], np.diff(average_users) / average_users[:-1] * 100)

# Plot setup
fig, ax1 = plt.subplots(figsize=(14, 10))

# First axis - Average users with error bars
ax1.errorbar(months, average_users, yerr=user_variability, fmt='-o', color='darkorange', capsize=5, alpha=0.8, 
             elinewidth=2, markerfacecolor='white', label='Average MAU')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Monthly Active Users (in thousands)', fontsize=12, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')
ax1.set_ylim(15, 55)

# Secondary axis - Cumulative users
ax2 = ax1.twinx()
ax2.plot(months, cumulative_users, 's-', color='blue', alpha=0.6, label='Cumulative MAU')
ax2.set_ylabel('Cumulative Monthly Active Users (in thousands)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
ax2.set_ylim(0, cumulative_users[-1] + 10)

# Adding a trend line
z = np.polyfit(range(len(months)), average_users, 1)
p = np.poly1d(z)
ax1.plot(months, p(range(len(months))), "r--", label='Trend Line', linewidth=1.5)

# Adding annotations for key months
peak_month = np.argmax(average_users)
ax1.annotate('Peak', xy=(months[peak_month], average_users[peak_month]), xytext=(peak_month, average_users[peak_month]+5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Titles and formatting
plt.title('Growth and Trends of Monthly Active Users on ChatterBuzz:\nA Year in Review', fontsize=16, fontweight='bold')
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
fig.tight_layout()

# Legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Secondary plot for percentage growth
fig, ax3 = plt.subplots(figsize=(14, 4))
ax3.bar(months, percentage_growth, color='lightgreen', alpha=0.7, label='Monthly Growth Rate (%)')
ax3.axhline(y=0, color='grey', linewidth=1)
ax3.set_title('Monthly Percentage Growth in Active Users', fontsize=14, fontweight='bold')
ax3.set_ylabel('Growth Rate (%)', fontsize=12)
ax3.set_xlabel('Month', fontsize=12)
ax3.legend(loc='upper right', fontsize=10)
ax3.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
fig.tight_layout()

# Display plots
plt.show()