import matplotlib.pyplot as plt
import numpy as np

# Data
platforms = ['Coursera', 'Udemy', 'edX', 'Skillshare', 'LinkedIn Learning']
active_users = [25, 30, 15, 10, 20]  # in millions

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f']

# Plot bars and add data annotations
bars = ax.bar(platforms, active_users, color=colors, width=0.6)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval}M", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add titles and labels
ax.set_title('The Rise of Online Learning Platforms\nActive Users by Platform in 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Platform', fontsize=12)
ax.set_ylabel('Active Monthly Users (Millions)', fontsize=12)

# Customize x-ticks and y-ticks
ax.set_xticks(np.arange(len(platforms)))
ax.set_xticklabels(platforms, rotation=30, ha='right')
ax.set_yticks(np.arange(0, 35, 5))

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()