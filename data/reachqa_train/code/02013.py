import numpy as np
import matplotlib.pyplot as plt

# Define hours and corresponding ship traffic data
hours = [
    "Midnight-3AM", "3AM-6AM", "6AM-9AM",
    "9AM-Noon", "Noon-3PM", "3PM-6PM",
    "6PM-9PM", "9PM-Midnight"
]

# Traffic volume (ships per hour)
traffic_volumes = np.array([4, 3, 7, 18, 16, 20, 11, 6])

# Number of categories
num_categories = len(hours)

# Calculate angles for each category
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False)

# Set up the plot with polar projection
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# Normalize color intensity by traffic volume
colors = plt.cm.plasma(traffic_volumes / max(traffic_volumes))

# Plot the rose chart
bars = ax.bar(angles, traffic_volumes, width=(2 * np.pi) / num_categories, color=colors, edgecolor='w', linewidth=1.5, alpha=0.75)

# Adjust labels to avoid overlap
ax.set_xticks(angles)
ax.set_xticklabels(hours, fontsize=10, rotation=45, ha='right')

# Y-axis (r) adjustments
ax.set_yticks([5, 10, 15, 20])
ax.set_yticklabels(['5', '10', '15', '20'], fontsize=8)

# Add a title with line breaks for clarity
plt.title("Shipping Traffic Distribution\nat Port of Atlantis (Typical Day)", fontsize=16, color='navy', pad=40)

# Add a legend on the right
plt.legend(bars, [f"{vol} ships" for vol in traffic_volumes], bbox_to_anchor=(1.2, 1), title='Traffic Volume', title_fontsize=10)

# Automatically adjust layout for neatness
plt.tight_layout()

# Display the chart
plt.show()