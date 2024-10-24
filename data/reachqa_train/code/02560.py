import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the stages and corresponding data
stages = [
    'Inquiries Received', 
    'Applications Submitted', 
    'Interviews Scheduled',
    'Offers Extended', 
    'Confirmations of Acceptance', 
    'Enrollments Completed'
]
values = [5000, 3500, 2500, 1500, 1000, 750]

# Define colors for each stage to enhance visual differentiation
colors = ['#a1dab4', '#41b6c4', '#2c7fb8', '#253494', '#f03b20', '#bd0026']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Define the width of each stage to create a funnel effect
total_width = 12  # Total width of the funnel at the widest point
stage_heights = 1.5  # Uniform height for each stage

# Calculate the width reduction factor for each step down the funnel
width_reduction = total_width / max(values)

# Plot each stage as a trapezoid (or rectangle, in this simplified case)
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

    # Add annotations to indicate stage names and values
    ax.text(total_width / 2, -i * stage_heights - (stage_heights / 2),
            f"{stages[i]}\n{values[i]} students",
            ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Set the plot limits and hide axes
ax.set_xlim(0, total_width)
ax.set_ylim(-len(stages) * stage_heights, 0)
ax.axis('off')

# Title of the plot
plt.title('Innovative Learning University Application Funnel\nFrom Inquiry to Enrollment', fontsize=14, fontweight='bold', pad=20)

# Ensure layout is tight and elements are not clipped
plt.tight_layout()

# Display the plot
plt.show()