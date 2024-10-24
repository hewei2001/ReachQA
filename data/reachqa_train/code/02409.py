import matplotlib.pyplot as plt
import squarify
import numpy as np

# Define research disciplines and their corresponding funding in millions of dollars
disciplines = [
    'Physics', 'Chemistry', 'Biology', 
    'Computer Science', 'Environmental\nScience', 
    'Mechanical\nEngineering', 'Electrical\nEngineering'
]

funding = [
    150, 120, 180, 200, 80, 130, 140  # Hypothetical funding amounts
]

# Normalize colors to represent funding levels
colors = plt.cm.plasma(funding / np.max(funding))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Create the tree map
squarify.plot(sizes=funding, label=disciplines, color=colors, alpha=0.85, edgecolor="white", linewidth=2, ax=ax)

# Set title and format the plot
ax.set_title('Research Funding Allocation in Science and Engineering\nNational Research Grant Program', fontsize=18, fontweight='bold', pad=20)
ax.axis('off')  # Turn off the axis

# Add a color bar to indicate funding levels
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=min(funding), vmax=max(funding)))
cbar = plt.colorbar(sm, ax=ax, label='Funding in Millions ($)', orientation='horizontal', pad=0.05, fraction=0.046)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()