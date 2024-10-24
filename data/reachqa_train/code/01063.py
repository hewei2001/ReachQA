import matplotlib.pyplot as plt
import numpy as np

# Define periods and their influence on modern art styles in Artlandia
periods = [
    'Renaissance', 'Baroque', 'Romanticism', 
    'Impressionism', 'Modernism', 'Postmodernism', 
    'Contemporary Art'
]
# Define the change in influence for each period
influence_changes = [30, -10, 15, 20, -5, 10, 40]

# Popularity Index for each period (constructed data)
popularity_index = [80, 60, 70, 85, 50, 65, 90]

# Calculate cumulative values
influence_values = [0] + list(np.cumsum(influence_changes))
cumulative = np.array(influence_values[:-1]) + np.array(influence_changes) / 2

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for positive and negative changes
colors = ['#66b3ff' if change > 0 else '#ff9999' for change in influence_changes]

# Plot each period's influence as a waterfall chart
ax1.bar(periods, influence_changes, width=0.6, color=colors, align='center', edgecolor='black')

# Draw dashed lines to connect the cumulative values
ax1.plot(np.arange(len(periods)), influence_values[1:], color='black', linewidth=1.5, linestyle='--')

# Label each bar with its contribution and cumulative value
for i, (change, value, center) in enumerate(zip(influence_changes, influence_values[1:], cumulative)):
    ax1.text(i, center, f'{change:+}', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    ax1.text(i, value + 2, f'{value}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Add secondary y-axis for Popularity Index
ax2 = ax1.twinx()
ax2.plot(periods, popularity_index, color='green', marker='o', linewidth=2, label='Popularity Index')

# Set titles and labels
ax1.set_title('Cultural Influence and Popularity on Modern Art Styles\nin Artlandia', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Influence Magnitude', fontsize=12, labelpad=10)
ax1.set_xlabel('Cultural and Historical Periods', fontsize=12, labelpad=10)
ax2.set_ylabel('Popularity Index', fontsize=12, color='green', labelpad=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add a horizontal baseline for initial value
ax1.axhline(0, color='gray', linewidth=0.8, linestyle='-')

# Legend for the secondary plot
ax2.legend(loc='upper left')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()