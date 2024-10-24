import matplotlib.pyplot as plt
import numpy as np

# Define the sources and their contributions
sources = [
    'Packaging Waste',
    'Fishing Equipment',
    'Textile Fibers',
    'Industrial Discharges',
    'Household Products',
    'Automotive Materials'
]
contributions = np.array([8.5, 4.3, 3.8, 2.1, 1.7, 1.2])  # in Million Metric Tons

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Create a horizontal bar chart
bars = ax.barh(sources, contributions, color=colors, alpha=0.85, edgecolor='black')

# Add data labels to each bar
for bar, value in zip(bars, contributions):
    ax.text(value + 0.1, bar.get_y() + bar.get_height()/2, f"{value:.1f}", va='center', fontsize=10)

# Set chart title and labels
ax.set_title('Ocean Plastic Waste Distribution by Source in 2023', fontsize=15, fontweight='bold')
ax.set_xlabel('Contribution (Million Metric Tons)', fontsize=12)

# Configure the x-axis and y-axis
ax.set_xlim(0, max(contributions) + 2)
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Customize ticks on y-axis to ensure labels align properly
ax.set_yticks(np.arange(len(sources)))
ax.set_yticklabels(sources, fontsize=11)

# Add a subtle background
ax.set_facecolor('whitesmoke')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()