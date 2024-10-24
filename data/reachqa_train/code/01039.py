import matplotlib.pyplot as plt
import numpy as np

# Define sectors and technologies
sectors = ['Healthcare', 'Finance', 'Education', 'Manufacturing', 'Retail']
technologies = ['AI', 'Blockchain', 'IoT', 'AR', '5G']

# Define focus levels for each sector and technology
focus_levels = np.array([
    [8, 5, 7, 6, 8],  # Healthcare
    [7, 9, 5, 4, 6],  # Finance
    [6, 4, 6, 8, 5],  # Education
    [9, 6, 8, 5, 7],  # Manufacturing
    [7, 7, 6, 7, 9],  # Retail
])

# Plotting the heat map
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(focus_levels, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add color bar with label
cbar = fig.colorbar(cax, orientation='vertical', pad=0.02)
cbar.set_label('Focus Level', fontsize=12)

# Set the ticks and labels
ax.set_xticks(np.arange(len(technologies)))
ax.set_xticklabels(technologies, fontsize=10)
ax.set_yticks(np.arange(len(sectors)))
ax.set_yticklabels(sectors, fontsize=10)

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Add a title
ax.set_title('Tech Innovation Trends:\nEmerging Technologies Across Sectors in 2023', 
             fontsize=14, fontweight='bold', pad=20)

# Annotate each cell with the numeric value
for (i, j), val in np.ndenumerate(focus_levels):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black', fontsize=9)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the heat map
plt.show()