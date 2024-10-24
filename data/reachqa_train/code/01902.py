import matplotlib.pyplot as plt
import numpy as np

# Define missions and their budget allocation percentages
missions = [
    'Europa Ice Research', 
    'Mars Geodome Colonization', 
    'Titan Atmospheric Analysis', 
    'Venus Cloud Cities', 
    'Asteroid Belt Mining'
]
budget_allocation = [25, 35, 15, 15, 10]  # Budget allocation in percentages

# Define colors for each mission
colors = ['#4caf50', '#2196f3', '#ffeb3b', '#ff5722', '#9c27b0']

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each mission's percentage as a horizontal bar
bars = ax.barh(missions, budget_allocation, color=colors, edgecolor='black')

# Add labels with percentages inside the bars for clarity
for bar, percentage in zip(bars, budget_allocation):
    ax.text(bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, 
            f'{percentage}%', va='center', ha='center', color='white', 
            fontsize=12, fontweight='bold')

# Set chart title and labels
ax.set_title("Planetary Exploration Budget Allocation\nGalactic Federation - 2077", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Budget Allocation (%)', fontsize=14)
ax.set_ylabel('Exploration Missions', fontsize=14)

# Customize the x-axis to represent percentage
ax.set_xlim(0, 100)  # Ensure it sums to 100% for clarity
ax.set_xticks(np.arange(0, 101, 10))
ax.set_xticklabels([f'{x}%' for x in range(0, 101, 10)])

# Remove the grid lines for a cleaner look
ax.xaxis.grid(False)
ax.yaxis.grid(False)

# Ensure the layout is tight and there is no overlap
plt.tight_layout()

# Display the bar chart
plt.show()