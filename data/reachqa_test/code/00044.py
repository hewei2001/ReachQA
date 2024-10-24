import matplotlib.pyplot as plt
import numpy as np

# Data for the chart: Countries and their respective percentage increases in renewable energy capacity
countries = ['Germany', 'China', 'USA', 'India', 'Brazil', 'Australia']
renewable_growth = [12.5, 15.3, 8.7, 18.2, 13.9, 10.1]

# Additional data for global average growth
global_avg_growth = np.mean(renewable_growth)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create bars with a gradient-like color palette to reflect growth magnitude
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(countries)))
bars = ax.bar(np.arange(len(countries)), renewable_growth, color=colors, width=0.5)

# Overlay line plot for global average growth
ax.axhline(y=global_avg_growth, color='gray', linestyle='--', linewidth=1, label='Global Avg Growth')

# Annotate each bar with the growth percentage
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customizing the appearance of the plot
ax.set_title('Global Renewable Energy Adoption in 2023\nPercentage Increase in Capacity with Global Average', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Countries', fontsize=12)
ax.set_ylabel('Percentage Increase', fontsize=12)
ax.set_xticks(np.arange(len(countries)))
ax.set_xticklabels(countries, rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding a legend for the line
ax.legend(loc='upper left', fontsize=10)

# Background color adjustment to enhance readability
fig.patch.set_facecolor('#f4f4f4')

# Add an annotation for global average line
ax.text(5.5, global_avg_growth + 0.5, f'Global Average: {global_avg_growth:.1f}%', color='gray', va='bottom', ha='right', fontsize=10)

# Enhance the bottom margin to fit x-axis labels
plt.tight_layout()

# Display the chart
plt.show()