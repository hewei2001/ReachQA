import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define stages of the manufacturing process
stages = [
    "Raw Material\nExtraction",
    "Production",
    "Packaging",
    "Transportation",
    "Recycling"
]

# Carbon footprint in tons of CO2 for each stage (cumulative change)
impacts = [0, 200, 150, 100, 80, -130]  # Recycling is a negative change

# Calculate cumulative impacts
cumulative_impacts = np.cumsum(impacts)

# Colors for each stage, gradient approach
colors = ['#4f83cc', '#80aaff', '#99cc99', '#ff9999', '#99e6ff']

# Create the waterfall chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each stage as a bar
previous_value = 0
for i, (stage, impact, cumulative) in enumerate(zip(stages, impacts, cumulative_impacts)):
    color = colors[i % len(colors)]
    hatch = '/' if impact < 0 else ''
    ax.bar(stage, impact if impact >= 0 else -impact, bottom=previous_value if impact >= 0 else cumulative,
           color=color, edgecolor='black', hatch=hatch, label=f'{stage} Impact')

    # Connect bars with lines to indicate the cumulative effect
    if i > 0:
        ax.plot([i-0.5, i-0.5], [previous_value, cumulative], color='black', linewidth=1)

    # Store the previous cumulative value for the next connection
    previous_value = cumulative

    # Display the cumulative total at each stage
    offset = 10 if impact >= 0 else -30
    ax.text(i, cumulative + offset, f"{cumulative:.0f} tCO2", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Title and labels, breaking the title into multiple lines for clarity
ax.set_title('Carbon Footprint Cascade:\nEmission Stages in Electronic Device Manufacturing', fontsize=16, pad=20)
ax.set_xlabel('Stages of Manufacturing', fontsize=12)
ax.set_ylabel('Carbon Footprint (tons of CO2)', fontsize=12)

# Create custom legends for visual clarity
positive_patch = mpatches.Patch(facecolor='grey', edgecolor='black', label='Positive Impact')
negative_patch = mpatches.Patch(facecolor='grey', edgecolor='black', hatch='/', label='Negative Impact')
ax.legend(handles=[positive_patch, negative_patch], loc='upper left')

# Ensure x-axis labels are visible and readable
plt.xticks(rotation=45, ha='right')

# Add grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()