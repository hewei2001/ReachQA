import matplotlib.pyplot as plt
import numpy as np

# Data for the year 2023
months = np.arange(1, 13)
visitor_counts = np.array([35, 45, 50, 60, 70, 85, 100, 95, 80, 65, 55, 40])  # Visitor count in thousands
whirlwind_popularity = np.array([5.0, 6.5, 7.0, 8.0, 9.0, 9.5, 10.0, 9.8, 9.2, 8.5, 7.0, 5.5])  # Popularity index
monthly_revenue = np.array([100, 120, 130, 150, 180, 210, 250, 240, 200, 180, 160, 130])  # Revenue in million USD

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(16, 8))

# Plot the visitor count data
ax1.plot(months, visitor_counts, color='tab:blue', marker='o', linestyle='-', linewidth=2, label='Visitors (thousands)')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Visitors (thousands)', color='tab:blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Set months as x-ticks and label them
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax1.set_xticks(months)
ax1.set_xticklabels(month_labels)

# Create a secondary y-axis for the ride popularity index
ax2 = ax1.twinx()
ax2.plot(months, whirlwind_popularity, color='tab:red', marker='^', linestyle='--', linewidth=2, label='The Whirlwind Popularity')
ax2.set_ylabel('Popularity Index', color='tab:red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add bar plot for monthly revenue on the same primary axis
ax1.bar(months, monthly_revenue, alpha=0.3, color='tab:green', label='Revenue (Million USD)', width=0.6)

# Add title with multiple lines for clarity
plt.title("Adventure World 2023:\nVisitor Trends, 'The Whirlwind' Ride Popularity, and Monthly Revenue", fontsize=16, fontweight='bold', pad=20)

# Add legends for each data set
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()