import numpy as np
import matplotlib.pyplot as plt

# Define the elements and their influences for the current scenario
elements = ['Earth', 'Water', 'Fire', 'Air', 'Spirit']
current_influences = [85, 75, 90, 65, 70]

# Define historical influences for comparison
historical_influences = [80, 70, 85, 60, 75]

# Append the first value to close the radar chart loop
current_influences += current_influences[:1]
historical_influences += historical_influences[:1]

# Number of variables
num_vars = len(elements)

# Compute the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot current influences
ax.plot(angles, current_influences, color='darkblue', linewidth=2, label='Current Influences')
ax.fill(angles, current_influences, color='skyblue', alpha=0.4)

# Plot historical influences
ax.plot(angles, historical_influences, color='darkred', linestyle='dashed', linewidth=2, label='Historical Influences')
ax.fill(angles, historical_influences, color='salmon', alpha=0.2)

# Customize the chart's aesthetics
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(elements, fontsize=12, weight='bold')
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_linewidth(1)
ax.spines['polar'].set_color('grey')
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Annotate each element's influence score
for i in range(num_vars):
    ax.text(angles[i], current_influences[i] + 5, f'{current_influences[i]}%', 
            horizontalalignment='center', size=10, color='black')
    ax.text(angles[i], historical_influences[i] - 10, f'{historical_influences[i]}%', 
            horizontalalignment='center', size=10, color='black', style='italic')

# Add title with a line break
plt.title("Elemental Harmony:\nComparing Current and Historical Influences", 
          size=15, fontweight='bold', pad=20)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()