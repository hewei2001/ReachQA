import matplotlib.pyplot as plt
import numpy as np

# Define the districts and their corresponding green space areas (in square kilometers)
districts = ['Downtown', 'East End', 'West Side', 'North Hill', 'South Bay']
green_spaces = np.array([4.2, 7.5, 5.8, 6.3, 8.1])

# Hypothetical average annual growth rate of green spaces (%) over the past decade for each district
growth_rates = np.array([1.2, 2.0, 1.5, 1.8, 2.1])

# Generate positions for the bars on the x-axis
x_positions = np.arange(len(districts))

# Create the figure and axis objects
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar chart for green spaces
bars = ax1.bar(x_positions, green_spaces, color=['#76c7c0', '#e2a76f', '#b6d7a8', '#ffe599', '#a4c2f4'], width=0.5, label='Green Spaces (km²)')

# Annotate the bars with their values
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval:.1f}', ha='center', va='bottom', fontsize=10, weight='bold')

# Secondary y-axis for growth rates
ax2 = ax1.twinx()
ax2.plot(x_positions, growth_rates, color='magenta', marker='o', linestyle='-', linewidth=2, markersize=8, label='Growth Rate (%)')

# Title and labels
ax1.set_title('Green Spaces and Growth Rates Across \nGreensville Districts', fontsize=16, fontweight='bold')
ax1.set_xlabel('Districts', fontsize=12)
ax1.set_ylabel('Area of Green Spaces (km²)', fontsize=12)
ax2.set_ylabel('Average Annual Growth Rate (%)', fontsize=12)

# Customize the x-ticks
ax1.set_xticks(x_positions)
ax1.set_xticklabels(districts, rotation=45, ha='right')

# Add grid lines for better readability
ax1.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)

# Legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Ensure the layout is tight to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()