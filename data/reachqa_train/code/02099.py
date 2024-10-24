import matplotlib.pyplot as plt
import numpy as np

# Data: Script names and their usage percentages
scripts = ['Hieroglyphics', 'Cuneiform', 'Runes', 'Sanskrit', 'Mayan Glyphs', 'Chinese Oracle Bone Script']
usage_percentages = [25, 15, 30, 10, 10, 10]

# Define distinct colors for each script
colors = ['#FFD700', '#8B4513', '#8B008B', '#4682B4', '#FF8C00', '#32CD32']

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(scripts, usage_percentages, color=colors, edgecolor='black', height=0.6)

# Annotate each bar with the usage percentage
for bar in bars:
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width()}%', va='center', ha='left', fontsize=10, color='black')

# Title and axis labels
ax.set_title('The Renaissance of Ancient Scripts:\nModern Usage in Creative Projects', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Usage Percentage (%)', fontsize=12)
ax.set_ylabel('Ancient Scripts', fontsize=12)

# Customize y-axis to ensure script names align with bars
ax.set_yticks(np.arange(len(scripts)))
ax.set_yticklabels(scripts, fontsize=12)

# Add grid lines to aid readability
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Ensure layout adjustments to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()