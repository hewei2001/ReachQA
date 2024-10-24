import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the stages of the publishing process and the number of manuscripts
stages = ['Manuscripts Submitted', 'Accepted for Review', 
          'Selected for Editing', 'Approved for Marketing', 'Books Published']
manuscripts = np.array([100, 80, 50, 30, 15])
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# Calculate percentage for each stage
percentages = (manuscripts / manuscripts[0]) * 100

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw each stage as a funnel segment
for i in range(len(stages)):
    # Create a trapezoid for the funnel segment
    trap = patches.FancyBboxPatch(
        (0.5 - percentages[i] / 200, i),  # Bottom-center position
        percentages[i] / 100, 0.5,  # Width and height
        boxstyle="sawtooth,pad=0.02", facecolor=colors[i],
        edgecolor='grey', linewidth=2, alpha=0.7
    )
    ax.add_patch(trap)

    # Annotate the number of manuscripts in each stage
    ax.text(0.5, i + 0.25, f'{manuscripts[i]} Manuscripts\n({percentages[i]:.0f}%)',
            ha='center', va='center', fontsize=11, color='black', fontweight='bold')

# Adjust axis limits and hide them to enhance funnel appearance
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')

# Title
plt.title('The Book Publishing Funnel:\nFrom Submission to Publication', fontsize=16, pad=20)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()