import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
categories = ['Parks', 'Gardens', 'Greenways', 'Community Gardens', 'Rooftop Gardens', 
              'Sports Fields', 'Botanical Gardens', 'Nature Reserves']
area_coverage = [120, 75, 40, 25, 10, 90, 60, 50]  # Area in hectares
maintenance_costs = [1.2, 0.8, 0.5, 0.2, 0.1, 0.9, 1.0, 0.7]  # Maintenance cost in millions

# Positions for each category on the x-axis
x_positions = np.arange(len(categories))

# Create the figure and the first axis for the bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plotting the bar chart for area coverage
bars = ax1.bar(x_positions, area_coverage, color=['#76c893', '#c9e4c5', '#f0f3bd', '#f4a261', '#e76f51',
                                                  '#118ab2', '#073b4c', '#ffd166'], width=0.6)

# Annotate each bar with the area covered
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval} ha', ha='center', va='bottom', fontsize=10, weight='bold')

# Create the second y-axis for maintenance costs
ax2 = ax1.twinx()
ax2.plot(x_positions, maintenance_costs, marker='o', color='black', label='Maintenance Cost (millions)')

# Setting labels and title
ax1.set_xlabel('Types of Green Spaces', fontsize=12, weight='bold')
ax1.set_ylabel('Area Coverage (hectares)', fontsize=12, weight='bold')
ax2.set_ylabel('Maintenance Cost (millions)', fontsize=12, color='black', weight='bold')

# Breaking the title into multiple lines for readability
ax1.set_title('Urban Green Spaces Distribution\nand Maintenance Cost Analysis in Greenfield City', fontsize=14, weight='bold')

# Set the x-ticks to match the categories and adjust rotation for readability
ax1.set_xticks(x_positions)
ax1.set_xticklabels(categories, rotation=30, ha='right', fontsize=10)

# Add grid lines for better estimation of values
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Add legend for the maintenance cost line
ax2.legend(loc='upper right', fontsize=10)

# Display the chart
plt.show()