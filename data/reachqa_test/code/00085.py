import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Funnel stage data
stages = ['Website Visits', 'Free Trial Sign-ups', 'Active Free Trial Users', 'Paid Subscriptions']
values = [1000000, 250000, 200000, 50000]

# Additional data for the bar chart
channels = ['Email', 'Social Media', 'Direct', 'Referral']
subscriptions_by_channel = [15000, 20000, 10000, 5000]

# Colors for each stage of the funnel and for bar chart
funnel_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
bar_colors = ['#c2f0c2', '#ffb3b3', '#c299ff', '#99e6ff']

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax1, ax2 = axes

# Maximum and minimum widths of the funnel
max_width = 10
min_width = 2

# Calculate widths for each stage
widths = np.linspace(max_width, min_width, len(values))

# Create the funnel using trapezoids
y_offset = 0
for i in range(len(values)):
    polygon = patches.Polygon([
        (0, y_offset),
        (widths[i], y_offset),
        (widths[i+1] if i+1 < len(values) else min_width, y_offset + 1),
        (0, y_offset + 1)
    ], closed=True, color=funnel_colors[i], edgecolor='black')
    ax1.add_patch(polygon)
    
    ax1.text(widths[i]/2, y_offset + 0.5, f"{stages[i]}\n{values[i]:,} Users",
             horizontalalignment='center', verticalalignment='center', fontsize=9, fontweight='bold')
    y_offset += 1

ax1.set_xlim(-0.5, max_width + 0.5)
ax1.set_ylim(0, len(values))
ax1.set_aspect('auto')
ax1.axis('off')
ax1.set_title('User Conversion Funnel\nFrom Visits to Subscriptions', fontsize=12, weight='bold')

# Bar chart for subscriptions by channel
ax2.bar(channels, subscriptions_by_channel, color=bar_colors, edgecolor='black')
ax2.set_title('Subscriptions by Marketing Channel', fontsize=12, weight='bold')
ax2.set_ylabel('Number of Subscriptions')
ax2.set_ylim(0, 25000)

# Adding values on top of bars
for i, v in enumerate(subscriptions_by_channel):
    ax2.text(i, v + 500, f"{v:,}", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()