import matplotlib.pyplot as plt
import numpy as np

# Define the time range
years = np.arange(2013, 2024)

# Market penetration data as a percentage of total packaging market
edible_packaging_market_penetration = np.array([0.5, 1.0, 1.8, 3.0, 5.2, 8.0, 10.5, 13.0, 16.0, 20.0, 25.0])

# Related data for the overlay: market size in millions of dollars
market_size = np.array([2, 5, 10, 20, 30, 50, 75, 110, 150, 200, 260])

# Plotting the data
fig, ax1 = plt.subplots(figsize=(12, 7))

# Primary y-axis: Line plot for market penetration
ax1.plot(years, edible_packaging_market_penetration, marker='o', linestyle='-', color='green', linewidth=2, label='Market Penetration (%)')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Market Penetration (%)', fontsize=12, color='green')
ax1.tick_params(axis='y', labelcolor='green')

# Annotate key milestones
annotations = {
    2014: ("Regulatory Approval", 1.0),
    2017: ("Cost Reduction Breakthrough", 3.0),
    2019: ("Public Awareness Campaign", 10.5),
    2021: ("Major Players Enter Market", 16.0)
}

for year, (text, y_value) in annotations.items():
    ax1.annotate(text, xy=(year, y_value), xytext=(year, y_value + 5),
                 arrowprops=dict(arrowstyle='->', color='blue'), fontsize=10, color='blue', ha='center',
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='blue'))

# Secondary y-axis: Bar plot for market size
ax2 = ax1.twinx()
ax2.bar(years, market_size, color='lightblue', alpha=0.6, label='Market Size (Millions)', width=0.5)
ax2.set_ylabel('Market Size (Millions $)', fontsize=12, color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Customize plot with title and legend
ax1.set_title('Innovation in Edible Packaging:\nA Decade of Growth and Market Expansion (2013-2023)', fontsize=16, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85), bbox_transform=ax1.transAxes)
ax1.grid(True, linestyle='--', alpha=0.7)

# Set the x-axis ticks and rotate them for better readability
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)

# Add data value labels on each point of market penetration
for year, value in zip(years, edible_packaging_market_penetration):
    ax1.text(year, value + 1, f'{value:.1f}%', fontsize=9, ha='center', color='black', alpha=0.7)

# Add data value labels on top of each bar for market size
for year, value in zip(years, market_size):
    ax2.text(year, value + 5, f'{value}', fontsize=9, ha='center', color='blue', alpha=0.7)

# Adjust the layout to ensure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()