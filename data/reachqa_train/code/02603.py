import matplotlib.pyplot as plt
import numpy as np

# Define regions and coffee consumption data in millions of bags (60 kg each)
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
coffee_consumption = [27.5, 45.3, 18.2, 25.0, 12.3, 3.9]

# Colors for the regions
colors = ['#7b9acc', '#f1c232', '#76a5af', '#e06666', '#6aa84f', '#a64d79']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the bar chart
bar_positions = np.arange(len(regions))
ax.bar(bar_positions, coffee_consumption, color=colors, alpha=0.8, edgecolor='grey')

# Add titles and labels
ax.set_title('Global Coffee Consumption by Region in 2022', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Regions', fontsize=14)
ax.set_ylabel('Coffee Consumption (Millions of Bags)', fontsize=14)

# Annotate each bar with the exact value
for i, value in enumerate(coffee_consumption):
    ax.text(i, value + 0.5, f"{value:.1f}", ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Enhance the plot aesthetics
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Customize ticks and labels
plt.xticks(bar_positions, regions, rotation=45, fontsize=12)
plt.yticks(np.arange(0, 51, 5))

# Adjust layout for better appearance
plt.tight_layout()

# Show the plot
plt.show()