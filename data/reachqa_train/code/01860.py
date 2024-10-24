import matplotlib.pyplot as plt
import numpy as np

# Data for bar chart
platforms = ['Coursera', 'Udemy', 'edX', 'Skillshare', 'LinkedIn Learning']
active_users = [25, 30, 15, 10, 20]  # in millions

# Data for overlay line plot (percentage growth rates)
growth_rates = [12, 18, 9, 15, 10]  # percentage growth over the past year

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Colors for bar chart
colors = ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f']

# Bar chart for active users
bars = ax1.bar(platforms, active_users, color=colors, width=0.6, label='Active Users (Millions)')
ax1.set_xlabel('Platform', fontsize=12)
ax1.set_ylabel('Active Users (Millions)', fontsize=12, color='black')
ax1.set_xticks(np.arange(len(platforms)))
ax1.set_xticklabels(platforms, rotation=30, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Data annotation for bar chart
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f"{yval}M", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Overlay line plot for growth rates
ax2 = ax1.twinx()
ax2.plot(platforms, growth_rates, color='navy', marker='o', linestyle='-', linewidth=2, label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='navy')
ax2.set_ylim(0, 20)

# Data annotation for line plot
for i, rate in enumerate(growth_rates):
    ax2.text(i, rate + 0.5, f"{rate}%", ha='center', va='bottom', fontsize=10, color='navy')

# Title and legend
plt.title('The Rise of Online Learning Platforms\nActive Users and Growth Rates by Platform in 2023', fontsize=16, fontweight='bold')
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()