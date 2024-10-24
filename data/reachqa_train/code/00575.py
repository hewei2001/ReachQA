import matplotlib.pyplot as plt
import numpy as np

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

# Colors for each stage (distinguish positive/negative impacts)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#17becf']

# Create the waterfall chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each stage as a bar
previous_value = 0
for i, (stage, impact, cumulative) in enumerate(zip(stages, impacts, cumulative_impacts)):
    color = colors[i % len(colors)]
    if impact < 0:  # For reductions like recycling
        ax.bar(stage, cumulative, bottom=previous_value, color=color, edgecolor='black')
    else:
        ax.bar(stage, impact, bottom=previous_value, color=color, edgecolor='black')
    
    # Line to connect previous cumulative to current cumulative
    if i > 0:
        ax.plot([i-0.5, i-0.5], [previous_value, cumulative], color='black', linewidth=1)

    # Store the previous cumulative value for the next connection
    previous_value = cumulative

    # Display the cumulative total at each stage
    offset = 10 if impact >= 0 else -30
    ax.text(i, cumulative + offset, f"{cumulative:.0f} tCO2", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Set title and labels, breaking the title into multiple lines for clarity
ax.set_title('Carbon Footprint Cascade:\nEmission Stages in Electronic Device Manufacturing', fontsize=14, pad=20)
ax.set_xlabel('Stages of Manufacturing', fontsize=12)
ax.set_ylabel('Carbon Footprint (tons of CO2)', fontsize=12)

# Ensure x-axis labels are visible and readable
plt.xticks(rotation=45, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()