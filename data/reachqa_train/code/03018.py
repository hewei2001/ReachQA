import matplotlib.pyplot as plt
import numpy as np

# Define space agencies and their fictional exoplanet discovery counts
agencies = ['NASA', 'ESA', 'CNSA', 'ISRO', 'Roscosmos']
discovery_counts = np.array([320, 245, 198, 152, 180])

# Define colors for the bars for visual distinction
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create positions for the bars on the x-axis
positions = np.arange(len(agencies))

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(positions, discovery_counts, color=colors, width=0.6)

# Annotate each bar with its value
for bar, count in zip(bars, discovery_counts):
    height = bar.get_height()
    ax.annotate(f'{count}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # Offset to display above the bar
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, color='black')

# Set x-ticks and labels
ax.set_xticks(positions)
ax.set_xticklabels(agencies, fontsize=12)

# Set chart title and labels
ax.set_title('Exoplanet Discoveries by Major Space Agencies (2013-2023)\nA Decade of Cosmic Exploration', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Space Agencies', fontsize=14)
ax.set_ylabel('Number of Exoplanets Discovered', fontsize=14)

# Add y-axis grid lines for improved readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend to identify bars
ax.legend(bars, agencies, title='Space Agencies', fontsize=10, loc='upper right', frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the bar chart
plt.show()