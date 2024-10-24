import matplotlib.pyplot as plt
import numpy as np

# Data for smartphone OS market share
os_labels = ['Android', 'iOS', 'HarmonyOS', 'Others']
market_share = [71, 27, 1, 1]

# Colors for the bars
colors = ['#4CAF50', '#2196F3', '#FFC107', '#9E9E9E']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Creating the percentage bar chart
bars = ax.bar(os_labels, market_share, color=colors, edgecolor='grey', linewidth=1.5)

# Adding the percentage values on top of the bars
for bar, percentage in zip(bars, market_share):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{percentage}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Title and labels
ax.set_title("Global Smartphone Operating System Market Share in 2023", fontsize=14, fontweight='bold')
ax.set_xlabel("Operating System", fontsize=12)
ax.set_ylabel("Market Share (%)", fontsize=12)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Customize the y-axis
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))

# Adjust the layout for readability
plt.tight_layout()

# Display the plot
plt.show()