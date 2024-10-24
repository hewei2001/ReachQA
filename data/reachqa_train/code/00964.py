import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(figsize=(12, 8))

# Create heatmap
c = ax.imshow(happiness_scores, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Set x and y axis labels
ax.set_xticks(np.arange(len(factors)))
ax.set_xticklabels(factors, rotation=45, ha='right')
ax.set_yticks(np.arange(len(departments)))
ax.set_yticklabels(departments)

# Annotate each cell with happiness data
for i in range(len(departments)):
    for j in range(len(factors)):
        ax.text(j, i, f"{happiness_scores[i, j]:.1f}", ha='center', va='center', color='black', fontsize=10)

# Color bar
cbar = fig.colorbar(c, ax=ax, orientation='vertical')
cbar.set_label('Happiness Score', rotation=270, labelpad=20)

# Title and labels
plt.title('Heatmap of Employee Happiness vs.\nWork Environment Conditions', fontsize=16, fontweight='bold')

# Add gridlines for clarity
ax.set_xticks(np.arange(-.5, len(factors), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(departments), 1), minor=True)
ax.grid(which="minor", color="w", linestyle='-', linewidth=2)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()