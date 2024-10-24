import matplotlib.pyplot as plt
import numpy as np

# Original financial stages and impacts
stages = [
    'Initial Investment', 
    'R&D Savings', 
    'Marketing Costs', 
    'Sales Revenue', 
    'Cost Reductions', 
    'Community Initiatives'
]
amounts = np.array([-100, 20, -30, 150, 10, -10])

# Cumulative sum for waterfall chart
cumulative = np.cumsum(np.insert(amounts, 0, 0))
final_gain = cumulative[-1]

# Colors for the waterfall chart
colors = ['#FF5733' if x < 0 else '#33FF57' for x in amounts]
colors.append('#3357FF' if final_gain >= 0 else '#FF3333')

# Create an additional dataset for the line chart
# This represents monthly financial projections over six months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_performance = np.array([10, 20, -5, 15, -10, 5])
monthly_cumulative = np.cumsum(np.insert(monthly_performance, 0, 0))

# Plot setup with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Waterfall chart
bars = ax1.bar(range(len(cumulative)), np.append(amounts, final_gain), 
               bottom=np.append([0], cumulative[:-1]), color=colors, edgecolor='grey', linewidth=1.2)
ax1.plot(range(len(cumulative)), cumulative, color='grey', linestyle='-', linewidth=1.5, marker='o', markersize=4)

# Bar annotations
for bar, amount in zip(bars, np.append(amounts, final_gain)):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + yval / 2,
             f'{amount:+,}K', ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Title and labels for waterfall
ax1.set_title('Financial Journey of GreenFuture Inc.\nLaunching an Eco-Friendly Product', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Development Stages', fontsize=12)
ax1.set_ylabel('Financial Impact (in Thousands)', fontsize=12)
ax1.set_xticks(range(len(cumulative)))
ax1.set_xticklabels(stages + ['Net Gain'], rotation=30, ha='right', fontsize=10)
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax1.axhspan(0, final_gain, facecolor='#3357FF', alpha=0.1)

# Line chart for monthly performance
ax2.plot(range(len(monthly_cumulative)), monthly_cumulative, color='#FFA500', marker='o', markersize=6, linestyle='-')
ax2.fill_between(range(len(monthly_cumulative)), 0, monthly_cumulative, color='#FFA500', alpha=0.2)

# Annotations for line chart
for i, val in enumerate(monthly_cumulative):
    ax2.text(i, val, f'{val:+,}K', fontsize=10, ha='center', va='bottom', fontweight='bold', color='#333')

# Title and labels for line chart
ax2.set_title('Monthly Financial Performance Projection\nOver Six Months', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Months', fontsize=12)
ax2.set_ylabel('Cumulative Impact (in Thousands)', fontsize=12)
ax2.set_xticks(range(len(monthly_cumulative)))
ax2.set_xticklabels(['Start'] + months, rotation=30, ha='right', fontsize=10)
ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()