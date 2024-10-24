import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import cm

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
percentages = (values / values[0]) * 100
drop_rates = np.round(100 - (percentages[1:] / percentages[:-1]) * 100, 1)

fig, ax = plt.subplots(figsize=(14, 10))

height = 1.5
gap = 0.4
y_pos = np.arange(len(stages)) * (height + gap)

# Define color gradients
colors = cm.viridis(np.linspace(0, 1, len(stages)))

# Draw the funnel with trapezoidal shapes and gradient fills
for i in range(len(stages)):
    x_center = (5000 - values[i]) / 2
    trapezoid = patches.FancyBboxPatch(
        (x_center, y_pos[i]), values[i], height,
        boxstyle="round,pad=0.1", ec='black', fc=colors[i], alpha=0.8
    )
    ax.add_patch(trapezoid)
    ax.text(2500, y_pos[i] + height / 2,
            f'{stages[i]}\n{values[i]} ({percentages[i]:.1f}%)',
            va='center', ha='center', fontsize=10, color='white', weight='bold')

# Add arrows and drop rates between stages
for i in range(len(stages) - 1):
    ax.annotate('', xy=(2500, y_pos[i] + height), xytext=(2500, y_pos[i] + height + gap - 0.2),
                arrowprops=dict(arrowstyle='->', color='gray'))
    ax.text(2500, y_pos[i] + height + gap / 2 - 0.2, f'Drop: {drop_rates[i]}%', fontsize=9, color='gray', ha='center')

# Set title and labels
ax.set_title('University Engineering Program Funnel\nStudent Journey from Application to Graduation', 
             fontsize=16, fontweight='bold', pad=30, loc='center')
ax.set_xlim(0, 5000)
ax.set_ylim(-gap, y_pos[-1] + height + gap)
ax.set_xlabel('Number of Students', fontsize=12)
ax.set_ylabel('Stages', fontsize=12)

# Remove default axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Customize the plot background
ax.set_facecolor('#f7f7f7')

# Tighten layout
plt.tight_layout()

# Display the plot
plt.show()