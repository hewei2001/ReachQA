import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the stages of the publishing process and the number of manuscripts
stages = ['Manuscripts Submitted', 'Accepted for Review', 
          'Selected for Editing', 'Approved for Marketing', 'Books Published']
manuscripts = np.array([100, 80, 50, 30, 15])
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# Additional data for overlay: Average processing time for each stage
processing_times = np.array([30, 25, 20, 15, 10])  # in days

# Calculate percentage for each stage
percentages = (manuscripts / manuscripts[0]) * 100

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 8))

# Draw each stage as a funnel segment
for i in range(len(stages)):
    trap = patches.FancyBboxPatch(
        (0.5 - percentages[i] / 200, i),  # Bottom-center position
        percentages[i] / 100, 0.5,  # Width and height
        boxstyle="sawtooth,pad=0.02", facecolor=colors[i],
        edgecolor='grey', linewidth=2, alpha=0.7
    )
    ax1.add_patch(trap)

    # Annotate the number of manuscripts in each stage
    ax1.text(0.5, i + 0.25, f'{manuscripts[i]} Manuscripts\n({percentages[i]:.0f}%)',
             ha='center', va='center', fontsize=11, color='black', fontweight='bold')

# Adjust axis limits and hide them to enhance funnel appearance
ax1.set_xlim(0, 1)
ax1.set_ylim(0, len(stages))
ax1.axis('off')

# Overlay plot for processing times
ax2 = ax1.twinx()
ax2.plot(processing_times, np.arange(len(stages)) + 0.25, color='blue', linestyle='-', marker='o', linewidth=2)
ax2.set_ylim(0, len(stages))
ax2.invert_yaxis()  # Match y-axis direction with funnel
ax2.set_ylabel('Average Processing Time (days)', color='blue', fontsize=12)
ax2.tick_params(axis='y', labelcolor='blue')

# Add legends and adjust layout
ax1.legend(['Manuscripts Funnel'], loc='upper left', fontsize=10)
ax2.legend(['Processing Time'], loc='upper right', fontsize=10)

# Title
plt.title('The Book Publishing Funnel and Processing Times:\nFrom Submission to Publication', fontsize=16, pad=20)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()