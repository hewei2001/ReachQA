import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Financial event values in thousands of dollars
funding_events = np.array([500, -150, 750, -200, 1200, -300, 2000, -500])
labels = [
    "Seed Funding\n(2017)", "Product Dev\n(2018)", "Series A\n(2019)",
    "Marketing & Expansion\n(2020)", "Series B\n(2021)", "Unexpected Expenses\n(2021)",
    "Series C\n(2022)", "Strategic Investments\n(2022)"
]

# Calculate cumulative funding values
cumulative_values = np.zeros(len(funding_events) + 1)
cumulative_values[0] = funding_events[0]
for i in range(1, len(funding_events) + 1):
    cumulative_values[i] = cumulative_values[i - 1] + funding_events[i - 1]

# Positions for the bars
bar_positions = np.arange(len(cumulative_values))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

# Create a color map for positive and negative values
colors = ['#66c2a5' if value > 0 else '#fc8d62' for value in funding_events]

# Plot bars for changes
for i in range(1, len(funding_events) + 1):
    ax.bar(bar_positions[i-1], funding_events[i-1], 
           color=colors[i-1], width=0.8,
           bottom=cumulative_values[i-1], edgecolor='grey', linewidth=1.2)

# Plot baseline and connections
ax.plot([0, len(funding_events)], [cumulative_values[0], cumulative_values[0]], 
        color='black', linewidth=1.5, linestyle='--')
ax.plot(bar_positions[:-1], cumulative_values[:-1], color='black', linewidth=1.2, marker='o', linestyle='--')

# Add annotations for cumulative values
for i in range(1, len(cumulative_values)):
    offset = 50 if funding_events[i-1] > 0 else -50
    ax.text(bar_positions[i-1], cumulative_values[i] + offset,
            f"${cumulative_values[i]:,.0f}K", ha='center', va='center', fontsize=10, color='darkblue')

    # Annotate funding events amount
    ax.text(bar_positions[i-1], cumulative_values[i-1] + funding_events[i-1]/2,
            f"{funding_events[i-1]:+,.0f}K", ha='center', va='center', fontsize=9, color='black')

# Enhancing the plot with background
ax.set_facecolor('#f7f7f7')

# Set labels, title, and grid
ax.set_xticks(bar_positions[:-1])
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=11)
ax.set_title("InnovateTech's Funding Journey:\nWaterfall Chart from Launch to Series C", fontsize=18, pad=20)
ax.set_ylabel('Cumulative Funding ($K)', fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()