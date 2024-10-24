import matplotlib.pyplot as plt
import numpy as np

# Expanded coffee types and branches
coffee_types = ['Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Macchiato', 'Americano']
branches = ['Downtown', 'Uptown', 'Suburban', 'Airport', 'Mall', 'Seaside']

# Monthly sales data for each branch (number of cups sold)
sales_data = {
    'Downtown': [350, 400, 300, 280, 260, 310],
    'Uptown': [300, 330, 290, 260, 280, 290],
    'Suburban': [280, 310, 270, 240, 260, 270],
    'Airport': [400, 420, 380, 350, 370, 390],
    'Mall': [320, 340, 310, 300, 290, 320],
    'Seaside': [370, 390, 360, 340, 350, 365]
}

# Define colors
coffee_colors = ['#8B4513', '#CD853F', '#DEB887', '#D2B48C', '#A0522D', '#F4A460']

# Initialize the figure with multiple subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Width of a single bar
bar_width = 0.12

# Plot bars for each branch
for i, branch in enumerate(branches):
    # Calculate positions for each set of bars
    positions = np.arange(len(coffee_types)) + i * bar_width
    ax.bar(positions, sales_data[branch], width=bar_width, color=coffee_colors[i % len(coffee_colors)], label=branch)

# Set labels and title
ax.set_xlabel('Coffee Types', fontsize=12)
ax.set_ylabel('Number of Cups Sold', fontsize=12)
ax.set_title('Monthly Sales Performance\nComparison of Coffee Types Across Branches', fontsize=14, fontweight='bold', pad=15)

# Set x-ticks to be in the middle of grouped bars
ax.set_xticks(np.arange(len(coffee_types)) + bar_width * (len(branches) / 2))
ax.set_xticklabels(coffee_types, rotation=45, ha='right')

# Add grid for easier visualization
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add data labels on top of each bar
for i, branch in enumerate(branches):
    positions = np.arange(len(coffee_types)) + i * bar_width
    for j, value in enumerate(sales_data[branch]):
        ax.text(positions[j], value + 5, str(value), ha='center', va='bottom', fontsize=9, color='black')

# Legend
ax.legend(title='Branches', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()