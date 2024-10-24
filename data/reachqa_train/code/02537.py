import matplotlib.pyplot as plt
import numpy as np

# Data for the years and coffee consumption in Brewtown
years = np.arange(2013, 2024)
coffee_consumption = [3.2, 3.5, 3.8, 4.0, 4.5, 5.0, 5.2, 5.5, 5.8, 6.1, 6.3]

# Hypothetical average coffee price over the years
coffee_price = [2.5, 2.6, 2.7, 2.8, 2.85, 3.0, 3.1, 3.2, 3.25, 3.4, 3.5]

# Key events or changes to annotate
annotations = [
    'Artisanal cafes popular',
    'Cold brew rises',
    'Subscription services launch',
    'Roasting innovations',
    'Coffee as social trend'
]

# Indices of years to annotate based on events
annotation_years = [2014, 2016, 2018, 2020, 2022]

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the coffee consumption line chart
ax1.plot(years, coffee_consumption, marker='o', color='brown', linestyle='-', linewidth=2.5, markersize=7, label='Coffee Consumption')
ax1.fill_between(years, coffee_consumption, color='sandybrown', alpha=0.3)

# Create a secondary y-axis for coffee price
ax2 = ax1.twinx()
ax2.plot(years, coffee_price, marker='s', color='darkgreen', linestyle='--', linewidth=2, markersize=6, label='Coffee Price (per kg)')

# Annotate each significant event
for i, year in enumerate(annotation_years):
    ax1.annotate(annotations[i], 
                xy=(year, coffee_consumption[year - years[0]]), 
                xytext=(0, 25), 
                textcoords='offset points', 
                ha='center', 
                fontsize=10, 
                arrowprops=dict(arrowstyle="->", color='gray'), 
                color='darkred')

# Add titles and labels
ax1.set_title('Evolution of Coffee Consumption and Prices in Brewtown\n(2013-2023)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Coffee Consumption (kg per capita)', fontsize=14, color='brown')
ax2.set_ylabel('Average Coffee Price ($ per kg)', fontsize=14, color='darkgreen')

# Add legends
ax1.legend(loc='upper left', fontsize=11, frameon=False)
ax2.legend(loc='upper right', fontsize=11, frameon=False)

# Grid and style adjustments
ax1.grid(True, linestyle='--', alpha=0.7)
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
ax1.set_facecolor('#f7f6f6')
plt.tight_layout()

# Display the plot
plt.show()