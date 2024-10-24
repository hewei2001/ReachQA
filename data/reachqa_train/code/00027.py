import matplotlib.pyplot as plt
import numpy as np

# Define the quarters
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Financial data for each component (all values in thousands of dollars)
gross_revenue = np.array([500, 700, 650, 800])
product_dev_costs = np.array([100, 150, 120, 180])
marketing_expenses = np.array([80, 90, 85, 95])
operational_expenses = np.array([150, 160, 155, 170])
unexpected_expenses = np.array([20, 25, 15, 30])

# Calculate net profit for each quarter
net_profit = gross_revenue - (product_dev_costs + marketing_expenses + operational_expenses + unexpected_expenses)

# Create cumulative data for waterfall chart
data = [gross_revenue[0],
        -product_dev_costs[0], -marketing_expenses[0], -operational_expenses[0], -unexpected_expenses[0], net_profit[0]]
for i in range(1, len(quarters)):
    data.extend([gross_revenue[i], -product_dev_costs[i], -marketing_expenses[i],
                 -operational_expenses[i], -unexpected_expenses[i], net_profit[i]])

# Setup the labels for the waterfall chart
labels = [f"{q} Gross Revenue" for q in quarters] + \
         ["Product Dev Costs", "Marketing Expenses", "Operational Expenses", "Unexpected Expenses", "Net Profit"] * len(quarters)

# Calculate cumulative values for waterfall
cumulative = np.cumsum(data)

# Adjust for display purposes, net profit should bring back to 0 in cumulative values for clarity
cumulative_adjusted = [0] + cumulative[:-1].tolist()

# Plotting the Waterfall Chart
fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#76c7c0' if val > 0 else '#f05454' for val in data]

ax.bar(range(len(data)), data, bottom=cumulative_adjusted, color=colors, edgecolor='black', width=0.5)

# Add lines for clarity on connection between the bars
for i in range(1, len(data)):
    ax.plot([i - 1, i], [cumulative[i - 1], cumulative[i - 1]], "k-", linewidth=1)

# Set labels and title
ax.set_xticks(range(len(data)))
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax.set_ylabel('Amount (in thousands of $)', fontsize=12)
ax.set_title('Tech Startups\' Quarterly Financial Performance\nBreakdown - 2023', fontsize=14, fontweight='bold')

# Display the net profit as annotations on the bars
for i, (cumulative, val) in enumerate(zip(cumulative, data)):
    ax.text(i, cumulative + val * 0.05, f"${val:+.0f}k", ha='center', va='bottom', fontweight='bold', fontsize=10)

# Add a horizontal baseline
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Auto layout adjustment for clear viewing
plt.tight_layout()

plt.show()