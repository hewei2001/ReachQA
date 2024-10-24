import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the expanded stages and corresponding data with a more complex, exponential decline
stages = [
    'Inquiries Received', 
    'Applications Submitted', 
    'Documents Reviewed',
    'Interviews Scheduled',
    'Background Checks', 
    'Offers Extended', 
    'Re-Evaluation',
    'Confirmations of Acceptance', 
    'Pre-Enrollment Activities',
    'Enrollments Completed'
]

# Complex values pattern
initial_value = 5000
decay_rate = 0.7
values = [int(initial_value * (decay_rate ** i)) for i in range(len(stages))]

# Define colors for each stage to enhance visual differentiation, using gradient-like variations
colors = ['#a1dab4', '#78c3b5', '#41b6c4', '#2c7fb8', '#206793', '#254b8a', '#233c77', '#253494', '#f03b20', '#bd0026']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 10))

# Define the width of each stage to create a funnel effect
total_width = 12  # Total width of the funnel at the widest point
stage_heights = 1.2  # Uniform height for each stage

# Calculate the width reduction factor for each step down the funnel
width_reduction = total_width / max(values)

# Plot each stage as a trapezoid with annotations for percentage decrease
for i in range(len(stages)):
    stage_width = values[i] * width_reduction
    x_offset = (total_width - stage_width) / 2

    # Create a trapezoid for each stage
    trapezoid = patches.FancyBboxPatch(
        (x_offset, -i * stage_heights),
        stage_width,
        -stage_heights,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=colors[i],
        linewidth=1.5
    )

    # Add trapezoid to the plot
    ax.add_patch(trapezoid)

    # Calculate percentage change from the previous stage, except for the first one
    if i > 0:
        percentage_change = (values[i] / values[i-1]) * 100
        annotation = f"{stages[i]}\n{values[i]} students\n({percentage_change:.1f}%)"
    else:
        annotation = f"{stages[i]}\n{values[i]} students"

    # Add annotations to indicate stage names, values, and percentage changes
    ax.text(total_width / 2, -i * stage_heights - (stage_heights / 2),
            annotation,
            ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# Set the plot limits and hide axes
ax.set_xlim(0, total_width)
ax.set_ylim(-len(stages) * stage_heights, 0)
ax.axis('off')

# Title of the plot with line breaks
plt.title('Innovative Learning University Application Funnel\nTracking the Journey from Inquiry to Enrollment\nIncluding Detailed Stage Changes',
          fontsize=14, fontweight='bold', pad=20)

# Ensure layout is tight and elements are not clipped
plt.tight_layout()

# Display the plot
plt.show()