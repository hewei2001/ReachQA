import matplotlib.pyplot as plt
import numpy as np

# Define oceanic zones and corresponding expedition counts
zones = ['Sunlight Zone', 'Twilight Zone', 'Midnight Zone', 'Abyssal Zone', 'Hadal Zone']
expeditions = [50, 35, 20, 15, 5]

# Define colors for each zone
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Create horizontal bars
bars = ax.barh(zones, expeditions, color=colors, edgecolor='black', height=0.6)

# Setting labels and title
ax.set_xlabel('Number of Expeditions', fontsize=12, fontweight='bold')
ax.set_title('Decadal Exploration of Ocean Depths:\nExpedition Counts by Oceanic Zone', fontsize=14, fontweight='bold', pad=15)

# Add grid for x-axis to improve readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Annotate bar values
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width}', va='center', fontsize=10, fontweight='bold', color='black')

# Ensure labels are centered with their respective bars
ax.set_yticks(np.arange(len(zones)))
ax.set_yticklabels(zones, ha='center', fontsize=11)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()