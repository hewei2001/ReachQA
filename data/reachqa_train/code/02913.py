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

# Colors for each transportation mode
colors = ['#6a0dad', '#ff6347', '#4682b4', '#ffd700', '#32cd32', '#ff4500']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Generate the horizontal bar chart
bars = ax.barh(transportation_modes, usage_percentages, color=colors, edgecolor='black')

# Add data labels for each bar
for bar, percentage in zip(bars, usage_percentages):
    ax.text(bar.get_width() - 3, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
            va='center', ha='right', color='white', fontsize=10, fontweight='bold')

# Set title and labels
ax.set_title("Urban Mobility in 2050:\nDistribution of Transportation Modes in Futuristic City X", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Percentage of Population Using the Mode", fontsize=12)
ax.set_xlim(0, 35)

# Customize y-axis labels
ax.set_yticks(range(len(transportation_modes)))
ax.set_yticklabels(transportation_modes, fontsize=11)

# Add grid lines for the x-axis
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()