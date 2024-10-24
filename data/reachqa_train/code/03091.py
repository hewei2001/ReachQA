import numpy as np
import matplotlib.pyplot as plt

# Define the elements and their influences
elements = ['Earth', 'Water', 'Fire', 'Air', 'Spirit']
influences = [85, 75, 90, 65, 70]

# Append the first value to close the radar chart loop
influences += influences[:1]

# Number of variables we have
num_vars = len(elements)

# Compute the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the radar chart and fill the area
ax.plot(angles, influences, color='darkblue', linewidth=2)
ax.fill(angles, influences, color='skyblue', alpha=0.4)

# Configure the radar chart grid and appearance
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(elements, fontsize=12, weight='bold')
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_linewidth(1)
ax.spines['polar'].set_color('grey')
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Annotate each element's influence score for clarity
for i in range(num_vars):
    ax.text(angles[i], influences[i] + 5, f'{influences[i]}%', 
            horizontalalignment='center', size=10, color='black')

# Add title with a line break for better readability
plt.title("Elemental Harmony:\nBalancing the Forces of Nature", 
          size=15, fontweight='bold', pad=20)

# Adjust layout to ensure no overlapping
plt.tight_layout()

# Show the plot
plt.show()