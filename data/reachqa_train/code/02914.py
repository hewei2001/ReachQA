import matplotlib.pyplot as plt
import numpy as np

# Define transportation modes and their usage percentages
transportation_modes = [
    "Autonomous Electric Vehicles",
    "Hyperloop",
    "Public Bicycles",
    "Maglev Trains",
    "Flying Taxis",
    "Traditional Public Transit"
]
usage_percentages = [30, 20, 15, 10, 10, 15]

# Data for the pie chart (projected future usage)
projected_usage_percentages = [25, 25, 20, 15, 5, 10]

# Colors for each transportation mode
colors = ['#6a0dad', '#ff6347', '#4682b4', '#ffd700', '#32cd32', '#ff4500']

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Horizontal Bar Chart
bars = ax1.barh(transportation_modes, usage_percentages, color=colors, edgecolor='black')
ax1.set_title("Urban Mobility in 2050:\nCurrent Distribution in Futuristic City X", 
              fontsize=14, weight='bold', pad=10)
ax1.set_xlabel("Percentage of Population Using the Mode", fontsize=12)
ax1.set_xlim(0, 35)
ax1.set_yticks(range(len(transportation_modes)))
ax1.set_yticklabels(transportation_modes, fontsize=10)
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Add data labels for each bar
for bar, percentage in zip(bars, usage_percentages):
    ax1.text(bar.get_width() - 3, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
             va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Pie Chart
ax2.pie(projected_usage_percentages, labels=transportation_modes, autopct='%1.1f%%', 
        startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'})
ax2.set_title("Projected Urban Mobility in 2060", fontsize=14, weight='bold', pad=20)

# Set a consistent theme and adjust layout
plt.tight_layout()

# Display the plot
plt.show()