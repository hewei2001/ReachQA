import matplotlib.pyplot as plt

# Original data for the bar chart
modes_of_transport = [
    'Public Buses', 'Trains', 'Bicycles', 
    'Autonomous Electric Cars', 'Hyperloops'
]
usage = [
    500, 400, 300, 600, 100
]
colors = ['blue', 'red', 'green', 'orange', 'purple']

# Create a figure that can contain multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plotting the horizontal bar chart with optimized elements
ax1.barh(modes_of_transport, usage, color=colors, height=0.6)
ax1.grid(axis='x', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
ax1.set_title('Predicted Usage of Urban Transportation Modes in 2035\n(Average Daily Usage in Millions)')
ax1.set_xlabel('Usage (Millions)')
ax1.set_ylabel('Modes of Transportation')
ax1.set_xlim(0, max(usage) + 100)
ax1.invert_yaxis() # Top-down display
ax1.set_xticklabels(ax1.get_xticks(), rotation=45) # Rotate labels for clarity

# Add text labels for each bar
for i in range(len(usage)):
    ax1.text(usage[i], i, f'{usage[i]:,}M', va='center', color='white',
             bbox=dict(facecolor='gray', alpha=0.5, boxstyle='round,pad=0.5'))

# Prepare data for the pie chart
total_usage = sum(usage)
percentages = [100 * u / total_usage for u in usage]

# Plot the pie chart with the same color scheme and labels
wedges, _, _ = ax2.pie(percentages, labels=modes_of_transport, colors=colors,
                       startangle=90, autopct='%1.1f%%')
ax2.set_title('Distribution of Usage Among Transportation Modes')

# Equal aspect ratio ensures that pie is drawn as a circle
ax2.axis('equal')

# Adjust layout to avoid any clipping of text or other elements
fig.tight_layout()

# Show the final plot
plt.show()