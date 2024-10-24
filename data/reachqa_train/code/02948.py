import matplotlib.pyplot as plt
import numpy as np

# Define the milestones and their revenue changes in millions
revenue_changes = [100, 15, 20, 25, 10]  # Initial revenue and subsequent increases
labels = ['2018 Initial Revenue', 'AI Manufacturing', 'Chatbots', 'Autonomous Vehicles', 'Healthcare AI']
color_scheme = ['darkblue', 'green', 'green', 'green', 'green']

# Calculate cumulative revenue for each year
cumulative_values = np.cumsum(revenue_changes)
start_values = np.insert(cumulative_values[:-1], 0, 0)  # Previous end point values

fig, ax = plt.subplots(figsize=(12, 7))

# Plot bars for each revenue change
for i in range(len(revenue_changes)):
    ax.bar(labels[i], revenue_changes[i], bottom=start_values[i],
           color=color_scheme[i], edgecolor='black', linewidth=0.8)

# Adding connecting lines to visualize the flow
for i in range(1, len(revenue_changes)):
    ax.plot([i-1, i], [cumulative_values[i-1], start_values[i]], color='black', linewidth=1.5, linestyle='--')

# Adding data labels above each bar
for i in range(len(revenue_changes)):
    ax.annotate(f"${revenue_changes[i]}M", (i, start_values[i] + revenue_changes[i] / 2),
                ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Final cumulative annotation
final_value = cumulative_values[-1]
ax.text(len(revenue_changes) - 1, final_value + 5, f'2022 Final Revenue: ${final_value}M',
        ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkgreen')

# Title and labels
ax.set_title('Impact of AI Advancements\non RoboTech Innovations Revenue (2018-2022)',
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Revenue (Million USD)', fontsize=12)
ax.set_xlabel('Year and Innovation', fontsize=12)

# Set x-ticks and adjust x-labels to avoid overlap
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Adjust layout to ensure everything fits
plt.tight_layout()

# Display the plot
plt.show()