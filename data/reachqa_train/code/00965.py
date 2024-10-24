import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

# Define departments and environment factors
departments = ["Development", "Marketing", "Sales", "HR", "Support"]
factors = ["Temp (°C)", "Noise (dB)", "Lighting (Lux)", "Amenities"]

# Artificial happiness scores based on work environment conditions
happiness_scores = np.array([
    [7.5, 5.0, 6.5, 8.0],  # Development
    [6.8, 6.2, 6.0, 7.5],  # Marketing
    [5.5, 7.0, 7.0, 6.8],  # Sales
    [7.0, 6.5, 7.8, 8.2],  # HR
    [6.2, 5.8, 6.7, 7.0]   # Support
])

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Use a diverging colormap with a central value at the mean score
mean_score = np.mean(happiness_scores)
norm = TwoSlopeNorm(vmin=happiness_scores.min(), vcenter=mean_score, vmax=happiness_scores.max())
c = ax.imshow(happiness_scores, cmap='coolwarm', norm=norm, aspect='auto', interpolation='nearest')

# Set x and y axis labels
ax.set_xticks(np.arange(len(factors)))
ax.set_xticklabels(factors, rotation=45, ha='right', fontsize=11)
ax.set_yticks(np.arange(len(departments)))
ax.set_yticklabels(departments, fontsize=11)

# Annotate each cell with happiness data, emphasizing deviations
for i in range(len(departments)):
    for j in range(len(factors)):
        score = happiness_scores[i, j]
        color = 'black' if abs(score - mean_score) < 1 else 'white'
        ax.text(j, i, f"{score:.1f}", ha='center', va='center', color=color, fontsize=12, fontweight='bold' if score > mean_score else 'normal')

# Add a color bar with enhanced labeling
cbar = fig.colorbar(c, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
cbar.set_label('Happiness Score', rotation=270, labelpad=20, fontsize=12)
cbar.ax.set_yticklabels([f"{i:.1f}" for i in cbar.get_ticks()], fontsize=10)

# Title with subtitle
plt.title('Employee Happiness Scores in Relation to\nWork Environment Conditions', fontsize=18, fontweight='bold')
plt.suptitle('A Comparative Analysis Across Departments', fontsize=14, fontstyle='italic', y=0.96)

# Add gridlines for clarity
ax.set_xticks(np.arange(-.5, len(factors), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(departments), 1), minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=1.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()