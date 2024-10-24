import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the funnel
stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Conversion']
users = [10000, 6000, 3000, 1200, 600]
colors = ['#007acc', '#3399ff', '#66b2ff', '#99ccff', '#cce6ff']

# Calculating drop-off rates for the bar chart
drop_off_rates = [100 * (users[i] - users[i+1]) / users[i] for i in range(len(users) - 1)]

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# Function to add funnel segments
def add_funnel_segment(ax, width, height, y_offset, color, label, user_count):
    left = (max(users) - width) / 2
    rect = patches.FancyBboxPatch((left, y_offset), width, height,
                                  boxstyle="round,pad=0.02", color=color, ec="black")
    ax.add_patch(rect)
    ax.text(max(users) / 2, y_offset + height / 2, f'{label}\n{user_count} users', 
            va='center', ha='center', fontsize=10, color='black', fontweight='bold')

# Plot each stage of the funnel
y_offset = 0
height = 1
for i in range(len(stages)):
    width = users[i]
    add_funnel_segment(ax1, width, height, y_offset, colors[i], stages[i], users[i])
    y_offset += height + 0.1

# Funnel Chart: Titles and layout
ax1.set_title('AdWizards Campaign Funnel\nAnalysis', fontsize=16, fontweight='bold')
ax1.set_xlim(0, max(users))
ax1.set_ylim(0, y_offset)
ax1.axis('off')

# Bar Chart: Drop-off rates
x_positions = np.arange(len(drop_off_rates))
ax2.bar(x_positions, drop_off_rates, color=colors[:-1], edgecolor='black')
ax2.set_xticks(x_positions)
ax2.set_xticklabels([f"{stages[i]} to {stages[i+1]}" for i in range(len(drop_off_rates))], rotation=45, ha='right')
ax2.set_ylabel('Drop-off Rate (%)', fontsize=12)
ax2.set_title('Stage-wise User Drop-off Rates', fontsize=14, fontweight='bold')

# Adding percentage values on top of bars
for i, rate in enumerate(drop_off_rates):
    ax2.text(i, rate + 1, f'{rate:.1f}%', ha='center', va='bottom', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the charts
plt.show()