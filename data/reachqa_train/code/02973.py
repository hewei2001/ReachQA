import matplotlib.pyplot as plt
import numpy as np

# Data: Mythical creatures and their respective sighting percentages
creatures = ['Dragons', 'Bigfoot', 'Loch Ness Monster', 'Unicorns', 'Chupacabra']
percentages = [35, 25, 15, 10, 15]

# Colors for each mythical creature
colors = ['#FF6666', '#66B2FF', '#FFCC66', '#99FF99', '#FF99CC']

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot horizontal percentage bar chart
bars = ax.barh(creatures, percentages, color=colors, edgecolor='black')

# Add annotations to each bar with percentage
for bar in bars:
    width = bar.get_width()
    ax.text(width - 5, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='center', va='center', color='black', fontsize=12, weight='bold')

# Set title with a creative layout
ax.set_title("Global Sightings of\nMythical Creatures in 2022", fontsize=16, weight='bold', pad=20)

# Label axes
ax.set_xlabel("Percentage of Total Sightings", fontsize=14)
ax.set_ylabel("Mythical Creatures", fontsize=14)

# Set x-axis limit to maintain consistency
ax.set_xlim(0, 100)

# Add grid lines for better readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to prevent label cutoff or overlap
plt.tight_layout()

# Display the plot
plt.show()