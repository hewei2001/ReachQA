import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
destinations = [
    'Paris, France', 'Bangkok, Thailand', 'New York, USA', 
    'Rome, Italy', 'Tokyo, Japan', 'Dubai, UAE', 'Barcelona, Spain'
]
tourists_millions = [18.5, 22.0, 15.6, 10.2, 13.9, 14.5, 12.8]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']

# Hypothetical data for the line chart - Tourist growth rates in percentage
growth_rates = [5.5, 6.1, 4.3, 3.8, 4.7, 5.2, 3.5]

# Create the figure and the primary y-axis
fig, ax1 = plt.subplots(figsize=(14, 9))

# Bar chart for tourists
x_positions = np.arange(len(destinations))
bars = ax1.bar(x_positions, tourists_millions, color=colors, label='Tourists (Millions)')

# Annotate each bar with the number of tourists
for i, bar in enumerate(bars):
    yval = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2, yval + 0.5,
        f'{yval}M', ha='center', va='bottom', fontsize=10, fontweight='bold'
    )

# Secondary y-axis for the growth rate line chart
ax2 = ax1.twinx()
ax2.plot(x_positions, growth_rates, color='green', marker='o', linestyle='-', linewidth=2, label='Growth Rate (%)')
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Annotate each point on the line chart
for i, growth in enumerate(growth_rates):
    ax2.text(
        x_positions[i], growth + 0.3,
        f'{growth}%', ha='center', va='bottom', fontsize=10, color='green'
    )

# Title and labels
ax1.set_title('Top Travel Destinations in 2023\nNumber of Tourists and Growth Rate', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Destination', fontsize=12)
ax1.set_ylabel('Number of Tourists (Millions)', fontsize=12)

# Set x-ticks and labels
ax1.set_xticks(x_positions)
ax1.set_xticklabels(destinations, rotation=45, ha='right', fontsize=11)

# Add grid to the primary axis
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Add legends for both plots
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()