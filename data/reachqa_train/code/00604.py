import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.arange(1, 13)  # 1 through 12 for the months of the year

# Engagement data in hours (monthly)
videos = np.array([80, 90, 110, 130, 160, 180, 200, 190, 150, 140, 130, 120])
articles = np.array([60, 60, 65, 70, 70, 75, 80, 75, 70, 65, 60, 55])
podcasts = np.array([30, 40, 50, 60, 50, 45, 55, 60, 70, 80, 90, 95])

# Plotting the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(months, videos, articles, podcasts, labels=['Videos', 'Articles', 'Podcasts'],
              colors=['skyblue', 'lightcoral', 'lightgreen'], alpha=0.8)

# Customizing the plot with title, labels, and legend
plt.title("User Engagement on ShareSphere Platform\nMonthly Cumulative Hours by Media Type", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Engagement (Hours)", fontsize=12)

# Adding x-ticks to denote months
month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
plt.xticks(months, month_labels)

# Customizing the legend
plt.legend(loc='upper left', title='Media Types', fontsize=10, frameon=False)

# Adding gridlines for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()