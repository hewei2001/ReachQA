import matplotlib.pyplot as plt
import numpy as np

# Define the data
categories = ['Social Media', 'Gaming', 'Productivity', 'Health & Fitness', 'Entertainment']
market_shares = np.array([35, 30, 15, 10, 10])  # Percentage values adding up to 100
projected_growth = np.array([2.5, 3.0, 1.5, 2.0, 1.0])  # Projected growth rates in percentage

# Define colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a horizontal bar chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
bar_container = ax1.barh(categories, market_shares, color=colors)
ax1.set_title('Mobile App Market Share and Projected Growth\nin 2023', fontsize=16, pad=20)
ax1.set_xlabel('Market Share (%)', fontsize=12)
ax1.set_xlim(0, 100)

# Add percentage labels to the bars
for bar, share in zip(bar_container, market_shares):
    ax1.text(share - 5, bar.get_y() + bar.get_height()/2, f'{share}%', va='center', ha='center', color='white', fontsize=10)

# Line plot overlay
ax2 = ax1.twiny()
ax2.plot(projected_growth, categories, marker='o', linestyle='--', color='gray', label='Projected Growth (%)')
ax2.set_xlabel('Projected Growth (%)', fontsize=12)
ax2.set_xlim(0, max(projected_growth) + 1)

# Adding error bars to indicate variability (assumed small fixed variability here for demonstration)
error = np.array([0.2, 0.3, 0.1, 0.1, 0.05])
ax2.errorbar(projected_growth, categories, xerr=error, fmt='o', linestyle='', color='gray', capsize=3)

# Add legend
lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='lower right')

# Adjust layout for visibility and non-overlapping elements
plt.tight_layout()

# Show the plot
plt.show()