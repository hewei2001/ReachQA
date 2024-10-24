import matplotlib.pyplot as plt
import numpy as np

# Data for the years and coffee consumption in Brewtown
years = np.arange(2013, 2024)
coffee_consumption = [3.2, 3.5, 3.8, 4.0, 4.5, 5.0, 5.2, 5.5, 5.8, 6.1, 6.3]

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
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the line chart with markers
ax.plot(years, coffee_consumption, marker='o', color='brown', linestyle='-', linewidth=2, markersize=6, label='Coffee Consumption')

# Fill area under the curve
ax.fill_between(years, coffee_consumption, color='sandybrown', alpha=0.2)

# Annotate each point with its significant event
for i, year in enumerate(annotation_years):
    ax.annotate(annotations[i], 
                xy=(year, coffee_consumption[year - years[0]]), 
                xytext=(5, 15), 
                textcoords='offset points', 
                ha='center', 
                fontsize=10,
                arrowprops=dict(arrowstyle="->", color='gray'), 
                color='darkred')

# Add titles and labels
ax.set_title('Evolution of Coffee Consumption in Brewtown\n2013-2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Coffee Consumption (kg per capita)', fontsize=14)

# Add grid for clarity
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper left', fontsize=11)

# Ensure the layout is tight for better viewing
plt.tight_layout()

# Display the plot
plt.show()