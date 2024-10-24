import matplotlib.pyplot as plt
import numpy as np

# Types of waste
waste_types = ['Plastic', 'Glass', 'Metal', 'Organic', 'Electronic']

# Annual waste production in thousands of tons
waste_production = [120, 80, 60, 150, 30]

# Recycling rates in percentage
recycling_rates = [85, 75, 90, 50, 60]

# Define bar width and positions
bar_width = 0.5
x_positions = np.arange(len(waste_types))

# Create figure and axes for dual y-axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot bar chart for waste production
bars = ax1.bar(x_positions, waste_production, bar_width, color='teal', label='Waste Produced')

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Offset label above the bar
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=10, color='black')

# Plot line for recycling rates
ax2 = ax1.twinx()
ax2.plot(x_positions, recycling_rates, color='orange', marker='o', linewidth=2, label='Recycling Rate (%)')

# Add data labels for recycling rates
for i, rate in enumerate(recycling_rates):
    ax2.annotate(f'{rate}%',
                 xy=(x_positions[i], rate),
                 xytext=(-10, 10),  # Offset slightly from the marker
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=10, color='orange')

# Set x-axis labels
ax1.set_xticks(x_positions)
ax1.set_xticklabels(waste_types, fontsize=11, rotation=45, ha='right')

# Set y-axis labels
ax1.set_ylabel('Waste Produced (Thousands of Tons)', fontsize=12, color='teal')
ax2.set_ylabel('Recycling Rate (%)', fontsize=12, color='orange')

# Set chart title
plt.title('Annual Waste Production and Recycling Rates\nin a Futuristic Eco-City', fontsize=14, fontweight='bold')

# Add legends
bars_legend = ax1.legend(loc='upper left', bbox_to_anchor=(0, 1), fontsize=10)
line_legend = ax2.legend(loc='upper right', bbox_to_anchor=(1, 1), fontsize=10)
ax1.add_artist(bars_legend)

# Display grid for y1 axis
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()