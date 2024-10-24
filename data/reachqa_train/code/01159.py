import matplotlib.pyplot as plt
import numpy as np

# Synthetic data representing tech startups
funding_rounds = np.array([1, 2, 3, 4, 5, 1, 6, 2, 7, 8, 3, 9, 5, 6, 10, 4, 7, 8, 9, 10])
success_rates = np.array([20, 35, 50, 65, 80, 10, 40, 30, 90, 95, 60, 85, 70, 75, 100, 55, 82, 87, 92, 98])
# Size of markers to reflect the magnitude of funding in millions
sizes = np.array([5, 15, 20, 25, 30, 10, 22, 13, 35, 40, 18, 33, 28, 32, 50, 24, 37, 38, 44, 48])

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Creating the scatter plot
scatter = ax.scatter(funding_rounds, success_rates, s=sizes * 10, c=success_rates, cmap='coolwarm', alpha=0.8, edgecolors='k')

# Adding a color bar for success rate
cbar = plt.colorbar(scatter)
cbar.set_label('Success Rate (%)', fontsize=12)

# Title and labels
ax.set_title('Venture Capital Landscape:\nFunding Rounds & Success Rates in Tech Startups (2023)', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Funding Rounds', fontsize=12)
ax.set_ylabel('Success Rate (%)', fontsize=12)

# Setting x and y limits
ax.set_xlim(0, 11)
ax.set_ylim(0, 110)

# Adding grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotating plot for additional context
ax.text(1, 105, "Point size represents\nfunding magnitude (in millions).",
        fontsize=10, verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3))

# Setting the x and y ticks
ax.set_xticks(np.arange(1, 11, 1))
ax.set_yticks(np.arange(0, 101, 10))

# Adjust layout to avoid text overlapping
plt.tight_layout()

# Display the plot
plt.show()