import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
destinations = [
    'Paris, France', 'Bangkok, Thailand', 'New York, USA', 
    'Rome, Italy', 'Tokyo, Japan', 'Dubai, UAE', 'Barcelona, Spain'
]
tourists_millions = [18.5, 22.0, 15.6, 10.2, 13.9, 14.5, 12.8]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']

# Create bar chart
fig, ax = plt.subplots(figsize=(12, 8))
x_positions = np.arange(len(destinations))
bars = ax.bar(x_positions, tourists_millions, color=colors)

# Annotate each bar with the number of tourists
for i, bar in enumerate(bars):
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, yval + 0.5,  # Position above the bar
        f'{yval}M', ha='center', va='bottom', fontsize=10, fontweight='bold',
        color='black'
    )

# Title and labels
ax.set_title('Top Travel Destinations in 2023\nBased on Number of Tourists (in Millions)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Destination', fontsize=12)
ax.set_ylabel('Number of Tourists (Millions)', fontsize=12)

# Set x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(destinations, rotation=45, ha='right', fontsize=11)

# Show grid
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to avoid text clipping
plt.tight_layout()

# Display the chart
plt.show()