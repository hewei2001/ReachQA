import matplotlib.pyplot as plt
import numpy as np

# Define the categories for the radar chart
categories = ['Battery Life', 'Camera Quality', 'Screen Resolution', 'Processing Power', 'Storage Capacity']
num_vars = len(categories)

# Survey data for each demographic group
teenagers = [6, 8, 7, 9, 6]
professionals = [8, 7, 6, 7, 9]
seniors = [9, 5, 8, 6, 5]

# Complete the loop to close the radar chart
teenagers += teenagers[:1]
professionals += professionals[:1]
seniors += seniors[:1]

# Calculate the angle for each axis on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a radar chart figure
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f2f2f7')  # Light background color

# Draw each sector and add labels to each axis
plt.xticks(angles[:-1], categories, color='#1a1a1a', size=12)

# Define y-labels and limits for each axis
ax.set_ylim(0, 10)
ax.yaxis.set_tick_params(labelsize=10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], color='#666666')

# Improved gridlines and radial background shading
ax.yaxis.grid(True, linestyle='--', color='#cccccc')
ax.spines['polar'].set_visible(False)

# Plot data for Teenagers
ax.plot(angles, teenagers, linewidth=2.0, linestyle='-', label='Teenagers', color='#ff6347', marker='o')
ax.fill(angles, teenagers, '#ff6347', alpha=0.1)

# Plot data for Working Professionals
ax.plot(angles, professionals, linewidth=2.0, linestyle='--', label='Working Professionals', color='#1e90ff', marker='x')
ax.fill(angles, professionals, '#1e90ff', alpha=0.1)

# Plot data for Seniors
ax.plot(angles, seniors, linewidth=2.0, linestyle='-.', label='Seniors', color='#32cd32', marker='s')
ax.fill(angles, seniors, '#32cd32', alpha=0.1)

# Add a descriptive title
ax.set_title("Tech Gadget Features Preference Survey\nUser Priorities by Demographic Group",
             size=15, color='darkblue', y=1.1, ha='center')

# Add a legend with customized location and appearance
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()