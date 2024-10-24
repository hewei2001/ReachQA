import matplotlib.pyplot as plt
import numpy as np

# Define the sectors and their corresponding percentage distribution
sectors = ['Artificial Intelligence', 'FinTech', 'HealthTech', 'EdTech', 'CleanTech']
percentages = [30, 25, 20, 15, 10]

# Define colors for each sector using a visually appealing color palette
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the percentage bars
bars = ax.barh(sectors, percentages, color=colors, edgecolor='black')

# Add percentage text labels on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width - 3 if width > 5 else width + 3  # Position text within or outside the bar based on width
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}%', ha='center', va='center', fontsize=11, color='black' if width > 5 else 'white', fontweight='bold')

# Set the title and labels
ax.set_title("Startup Sector Distribution\nin Tech Innovation - 2023", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Percentage of Startups", fontsize=12)
ax.set_xlim(0, 100)  # Fixed x-axis range to represent 0-100%

# Invert y-axis to have the largest percentage on top
ax.invert_yaxis()

# Add gridlines for horizontal reference only
ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.yaxis.grid(False)

# Ensure the layout is tight to avoid overlaps and optimize spacing
plt.tight_layout()

# Show the plot
plt.show()