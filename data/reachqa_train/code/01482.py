import matplotlib.pyplot as plt
import numpy as np

# Define the conservation initiatives and their respective fund allocations
initiatives = ['Forest Restoration', 'Wildlife Protection', 'Ocean Cleanup', 'Renewable Energy Research', 'Community Education']
allocations = [400, 300, 250, 350, 150]

# Set the positions and width for the bars
positions = np.arange(len(initiatives))
bar_width = 0.6

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the bars
bars = ax.bar(positions, allocations, bar_width, color=['#7ca982', '#f39c12', '#3498db', '#9b59b6', '#e74c3c'])

# Add title and axis labels
ax.set_title('EcoFuture Fund Allocation 2023:\nSupporting Global Conservation Efforts', fontsize=16, fontweight='bold', pad=15)
ax.set_ylabel('Allocation (in thousands of $)', fontsize=12)
ax.set_xlabel('Conservation Initiatives', fontsize=12)

# Add annotations on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 10, f"${yval}k", ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Customize the x-axis labels
ax.set_xticks(positions)
ax.set_xticklabels(initiatives, rotation=45, ha='right', fontsize=11)

# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout to fit all elements
plt.tight_layout()

# Display the plot
plt.show()