import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the funnel stages and corresponding values
stages = [
    "Signups",
    "First Week Active",
    "Midterm Active",
    "Final Week Active",
    "Course Completion"
]
values = [10000, 7500, 5000, 3500, 2000]

# Calculate dropout rates between stages
dropout_rates = [100 - (values[i] / values[i - 1] * 100) for i in range(1, len(values))]

# Define colors for the funnel stages
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']

# Create figure and two subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# Funnel chart
ax1 = axes[0]
width_reduction = 0.15
start_y = np.arange(len(values))

for i, (stage, value) in enumerate(zip(stages, values)):
    top_width = (1.0 - i * width_reduction)
    bottom_width = (1.0 - (i + 1) * width_reduction)
    corners = [
        (1.0 - top_width) / 2, start_y[i], 
        (1.0 + top_width) / 2, start_y[i],
        (1.0 + bottom_width) / 2, start_y[i] + 0.8, 
        (1.0 - bottom_width) / 2, start_y[i] + 0.8
    ]
    polygon = patches.Polygon(
        [corners[:2], corners[2:4], corners[4:6], corners[6:]], 
        closed=True, 
        color=colors[i], 
        edgecolor='black'
    )
    ax1.add_patch(polygon)
    ax1.text(0.5, start_y[i] + 0.4, f"{stage}: {value:,}", fontsize=12, fontweight='bold',
             color='white', ha='center', va='center')

ax1.set_xlim(0, 1)
ax1.set_ylim(0, len(stages))
ax1.axis('off')
ax1.set_title("EduPlus Student Retention Funnel", fontsize=14, fontweight='bold')

# Bar chart for dropout rates
ax2 = axes[1]
ax2.barh(stages[1:], dropout_rates, color='#c44e52')
ax2.set_xlim(0, 100)
ax2.set_xlabel('Dropout Rate (%)', fontsize=12)
ax2.set_ylabel('Funnel Stages', fontsize=12)
ax2.set_title('Dropout Rates Across Stages', fontsize=14, fontweight='bold')

for i, rate in enumerate(dropout_rates):
    ax2.text(rate + 1, i, f"{rate:.1f}%", va='center', fontsize=10)

# Adjust layout for better view
plt.tight_layout()

# Display the plot
plt.show()