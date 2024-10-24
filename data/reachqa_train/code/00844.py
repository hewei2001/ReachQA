import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Define stages and corresponding data
stages = [
    'Applications Received',
    'Applications Approved',
    'Students Enrolled',
    'Students in Second Year',
    'Students in Final Year',
    'Students Graduated'
]

values = np.array([5000, 4000, 3500, 3000, 2500, 2000])

# Calculate percentage for annotations
percentages = (values / values[0]) * 100

# Initialize the figure
fig, ax = plt.subplots(figsize=(12, 8))

# Set initial position for each segment
height = 1.5
gap = 0.3
y_pos = np.arange(len(stages)) * (height + gap)

# Define colors for each stage
colors = ['#004c6d', '#00798c', '#6b7b8c', '#f2b705', '#f28705', '#f25c05']

# Draw the funnel with trapezoidal shapes
for i in range(len(stages)):
    x_center = (5000 - values[i]) / 2
    # Create a trapezoid shape
    trapezoid = patches.FancyBboxPatch(
        (x_center, y_pos[i]), values[i], height,
        boxstyle="round,pad=0.1", ec='black', fc=colors[i], alpha=0.8
    )
    ax.add_patch(trapezoid)
    # Annotate each stage with number and percentage
    ax.text(5000 / 2, y_pos[i] + height / 2,
            f'{stages[i]}\n{values[i]} ({percentages[i]:.1f}%)',
            va='center', ha='center', fontsize=10, color='white', weight='bold')

# Set title and labels
ax.set_title('University Engineering Program Funnel:\nStudent Journey from Application to Graduation', 
             fontsize=16, fontweight='bold', pad=30)
ax.set_xlim(0, 5000)
ax.set_ylim(-gap, y_pos[-1] + height + gap)
ax.set_xlabel('Number of Students', fontsize=12)
ax.set_ylabel('Stages', fontsize=12)

# Remove default axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Customize the plot background
ax.set_facecolor('#f7f7f7')

# Adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()