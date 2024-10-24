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

# Calculate cumulative values
influence_values = [0] + list(np.cumsum(influence_changes))
cumulative = np.array(influence_values[:-1]) + np.array(influence_changes) / 2

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for positive and negative changes
colors = ['#66b3ff' if change > 0 else '#ff9999' for change in influence_changes]

# Plot each period's influence as a waterfall chart
ax.bar(periods, influence_changes, width=0.6, color=colors, align='center', edgecolor='black')

# Draw dashed lines to connect the cumulative values
ax.plot(np.arange(len(periods)), influence_values[1:], color='black', linewidth=1.5, linestyle='--')

# Label each bar with its contribution and cumulative value
for i, (change, value, center) in enumerate(zip(influence_changes, influence_values[1:], cumulative)):
    ax.text(i, center, f'{change:+}', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    ax.text(i, value + 2, f'{value}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Set the title and labels, breaking title into two lines
ax.set_title('Cultural Influence on Modern Art Styles\nin Artlandia', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Influence Magnitude', fontsize=12, labelpad=10)
ax.set_xlabel('Cultural and Historical Periods', fontsize=12, labelpad=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add a horizontal baseline for initial value
ax.axhline(0, color='gray', linewidth=0.8, linestyle='-')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()