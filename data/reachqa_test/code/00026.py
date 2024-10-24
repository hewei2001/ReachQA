import matplotlib.pyplot as plt
import numpy as np

# Data for e-commerce categories and their projected growth in 2025 (in millions USD)
categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Health & Beauty', 'Sports & Outdoors', 'Books & Media']
revenue_growth = [45, 38, 25, 32, 29, 15]

# Market share distribution (as percentages of total growth)
total_growth = sum(revenue_growth)
market_share = [(growth / total_growth) * 100 for growth in revenue_growth]

# Colors for the plots
colors = plt.cm.tab20(np.arange(len(categories)))

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# Bar Chart: Projected Growth
ax1 = axes[0]
bars = ax1.barh(categories, revenue_growth, color=colors, edgecolor='black')
ax1.set_title('Projected Growth of E-Commerce Categories in 2025\n(in millions USD)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Revenue Growth (Millions USD)', fontsize=13)
ax1.set_ylabel('E-Commerce Categories', fontsize=13)
ax1.invert_yaxis()
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)

# Add value labels
for bar, revenue in zip(bars, revenue_growth):
    ax1.text(revenue + 1, bar.get_y() + bar.get_height() / 2, f'{revenue}M', va='center', ha='left', fontsize=11)

# Pie Chart: Market Share
ax2 = axes[1]
wedges, texts, autotexts = ax2.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors,
                                   textprops={'fontsize': 11})
ax2.set_title('Market Share of E-Commerce Categories in 2025', fontsize=16, weight='bold')
ax2.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()