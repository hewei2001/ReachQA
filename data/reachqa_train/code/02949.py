import matplotlib.pyplot as plt
import numpy as np

# Define the milestones and their revenue changes in millions
revenue_changes = [100, 15, 20, 25, 10]  # Initial revenue and subsequent increases
growth_rates = [0, 15, 33.33, 25, 40]  # Manually defined growth rates as percentages for each subsequent year
labels = ['2018 Initial Revenue', 'AI Manufacturing', 'Chatbots', 'Autonomous Vehicles', 'Healthcare AI']
bar_color_scheme = ['darkblue', 'green', 'green', 'green', 'green']

# Calculate cumulative revenue for each year
cumulative_values = np.cumsum(revenue_changes)
start_values = np.insert(cumulative_values[:-1], 0, 0)  # Previous end point values

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot bars for each revenue change
ax1.bar(labels, revenue_changes, bottom=start_values, color=bar_color_scheme, edgecolor='black', linewidth=0.8)

# Adding data labels above each bar
for i, change in enumerate(revenue_changes):
    ax1.annotate(f"${change}M", (i, start_values[i] + change / 2),
                 ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Secondary y-axis for the growth rate
ax2 = ax1.twinx()
ax2.plot(labels, growth_rates, color='orange', marker='o', linestyle='-', linewidth=2.5, label='Growth Rate (%)')

# Adding growth rate labels
for i, rate in enumerate(growth_rates):
    if i > 0:  # Skip the initial revenue since growth rate is not applicable
        ax2.annotate(f"{rate}%", (i, rate + 2), ha='center', va='bottom', color='orange', fontsize=10)

# Titles and labels
ax1.set_title('Impact of AI Advancements on\nRoboTech Innovations Revenue and Growth Rate (2018-2022)', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Revenue (Million USD)', fontsize=12)
ax1.set_xlabel('Year and Innovation', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12, color='orange')

# Set x-ticks and adjust x-labels to avoid overlap
ax1.set_xticks(np.arange(len(labels)))
ax1.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)

# Enable grid lines on y-axis of the bar chart
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)

# Add legend for the growth rate
ax2.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Final layout adjustment
plt.tight_layout()

# Display the plot
plt.show()