import matplotlib.pyplot as plt
import numpy as np

# Define months and sales data for each genre
months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Sales data for each genre
mystery_sales = np.array([200, 180, 220, 240, 260, 300, 320, 310, 290, 275, 260, 250])
scifi_sales = np.array([150, 160, 170, 180, 190, 210, 230, 240, 220, 210, 205, 200])
romance_sales = np.array([180, 190, 200, 210, 230, 250, 260, 265, 250, 240, 230, 220])
history_sales = np.array([130, 125, 140, 150, 155, 160, 180, 190, 200, 210, 190, 185])

# Calculate revenue data (price per genre: Mystery=$12, Sci-Fi=$10, Romance=$11, History=$9)
mystery_revenue = mystery_sales * 12
scifi_revenue = scifi_sales * 10
romance_revenue = romance_sales * 11
history_revenue = history_sales * 9

# Create the figure and primary axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot line chart for sales
ax1.plot(months, mystery_sales, marker='o', label='Mystery Sales', color='#1f77b4', linestyle='-', linewidth=2)
ax1.plot(months, scifi_sales, marker='s', label='Sci-Fi Sales', color='#ff7f0e', linestyle='--', linewidth=2)
ax1.plot(months, romance_sales, marker='^', label='Romance Sales', color='#2ca02c', linestyle='-.', linewidth=2)
ax1.plot(months, history_sales, marker='d', label='History Sales', color='#d62728', linestyle=':', linewidth=2)

# Create secondary axis for revenue overlay
ax2 = ax1.twinx()

# Plot bar chart for revenue
width = 0.2  # Width of bars
x_indices = np.arange(len(months))  # X-axis positions

ax2.bar(x_indices - width * 1.5, mystery_revenue, width=width, label='Mystery Revenue', color='#1f77b4', alpha=0.3)
ax2.bar(x_indices - width * 0.5, scifi_revenue, width=width, label='Sci-Fi Revenue', color='#ff7f0e', alpha=0.3)
ax2.bar(x_indices + width * 0.5, romance_revenue, width=width, label='Romance Revenue', color='#2ca02c', alpha=0.3)
ax2.bar(x_indices + width * 1.5, history_revenue, width=width, label='History Revenue', color='#d62728', alpha=0.3)

# Set titles and labels
ax1.set_title('Trend of Vintage Book Sales and Revenue by Genre\nin a Hypothetical Online Bookstore (2023)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Number of Books Sold', fontsize=12)
ax2.set_ylabel('Revenue (in $)', fontsize=12)

# Add legends
sales_legend = ax1.legend(title='Sales', loc='upper left', fontsize=10)
revenue_legend = ax2.legend(title='Revenue', loc='upper right', fontsize=10)
ax1.add_artist(sales_legend)

# Annotate revenue on bars
for i, (m_rev, s_rev, r_rev, h_rev) in enumerate(zip(mystery_revenue, scifi_revenue, romance_revenue, history_revenue)):
    ax2.text(i - width * 1.5, m_rev, f'${m_rev}', ha='center', va='bottom', fontsize=8)
    ax2.text(i - width * 0.5, s_rev, f'${s_rev}', ha='center', va='bottom', fontsize=8)
    ax2.text(i + width * 0.5, r_rev, f'${r_rev}', ha='center', va='bottom', fontsize=8)
    ax2.text(i + width * 1.5, h_rev, f'${h_rev}', ha='center', va='bottom', fontsize=8)

# Configure x-axis with proper alignment
ax1.set_xticks(x_indices)
ax1.set_xticklabels(months)
plt.xticks(rotation=45)

# Grid and layout adjustment
ax1.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Display the plot
plt.show()