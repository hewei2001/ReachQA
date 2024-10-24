import matplotlib.pyplot as plt
import numpy as np

# Define the categories and their corresponding percentage values
activities = [
    'Heating & Cooling', 'Water Heating', 'Lighting', 'Appliances', 'Electronics',
    'Other', 'Renewable Energy', 'Insulation', 'Cooking', 'Refrigerators', 'Washing Machines'
]
percentages = [25, 15, 10, 12, 8, 5, 10, 5, 5, 3, 2]

# Define raw data for calculating percentages
energy_consumption = np.array([2500, 1500, 1000, 1200, 800, 500, 1000, 500, 500, 300, 200])
total_consumption = energy_consumption.sum()
percentages_calculated = (energy_consumption / total_consumption) * 100

# Define a color palette
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', 
    '#ff6666', '#66ffb3', '#b3b3cc', '#99ccff', '#ffcccb'
]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal stacked bar chart
bars = ax.barh(activities, percentages_calculated, color=colors)

# Add percentage labels inside the bars
for bar, percentage in zip(bars, percentages_calculated):
    ax.text(bar.get_width() / 2, bar.get_y() + bar.get_height()/2, f'{percentage:.1f}%', 
            va='center', ha='center', color='black', fontsize=9)

# Set title and labels
ax.set_title('Detailed Breakdown of Household Energy Consumption\nby Activity and Appliance', fontsize=16, pad=20)
ax.set_xlabel('Percentage of Total Energy (%)', fontsize=12)

# Add a legend with adjusted location
ax.legend(bars, activities, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title="Categories")

# Set x-axis range to ensure it covers 0-100%
ax.set_xlim(0, 100)

# Improve layout spacing to avoid overlapping
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Add a secondary plot for comparative monthly consumption
fig, ax2 = plt.subplots(figsize=(12, 4))
months = np.arange(1, 13)
monthly_consumption = [2200, 2100, 2300, 2500, 2400, 2600, 2700, 2600, 2400, 2300, 2200, 2100]
ax2.plot(months, monthly_consumption, marker='o', color='teal', linestyle='-', linewidth=2)

# Add titles, labels, and grid
ax2.set_title('Monthly Household Energy Consumption (kWh)', fontsize=16, pad=20)
ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Energy (kWh)', fontsize=12)
ax2.set_xticks(months)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.grid(True, linestyle='--', alpha=0.6)

# Improve layout spacing
plt.tight_layout()

# Display both plots
plt.show()