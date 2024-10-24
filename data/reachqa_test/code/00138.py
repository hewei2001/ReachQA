import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Original funnel data
stages = ['Invitations Sent', 'RSVP Responses', 'Webinar Attendance', 
          'Engagement During Webinar', 'Conversions']
data = np.array([1000, 600, 450, 300, 150])

# Comparative data
benchmark_data = np.array([950, 550, 400, 320, 180])

# Calculate the width of each stage relative to the largest stage
widths = data / np.max(data)
benchmark_widths = benchmark_data / np.max(benchmark_data)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Virtual Event Performance Analysis', fontsize=16, fontweight='bold')

# Funnel chart on the left
ax1.set_xlim(0, 1)
ax1.set_ylim(-0.5, len(stages) - 0.5)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

for i, (stage, color, width) in enumerate(zip(stages, colors, widths)):
    rect = Rectangle(((1 - width) / 2, i - 0.5), width, 0.9, color=color, ec='gray')
    ax1.add_patch(rect)
    ax1.text(0.5, i, f'{stage}: {data[i]}', ha='center', va='center', fontsize=11, weight='bold')

ax1.set_title('Engagement Funnel', fontsize=14, pad=10)
ax1.axis('off')

# Comparative bar chart on the right
bar_width = 0.35
index = np.arange(len(stages))

ax2.barh(index, data, bar_width, label='Current Event', color='#ff9999', edgecolor='gray')
ax2.barh(index + bar_width, benchmark_data, bar_width, label='Benchmark', color='#66b3ff', edgecolor='gray')

for i, (actual, benchmark) in enumerate(zip(data, benchmark_data)):
    ax2.text(actual + 20, i, f'{actual}', va='center', ha='left', fontsize=9)
    ax2.text(benchmark + 20, i + bar_width, f'{benchmark}', va='center', ha='left', fontsize=9)

ax2.set_yticks(index + bar_width / 2)
ax2.set_yticklabels(stages)
ax2.invert_yaxis()
ax2.set_xlabel('Participants/Responses')
ax2.set_title('Event Performance vs. Benchmark', fontsize=14, pad=10)
ax2.legend(loc='lower right')

# Adjust layout for better spacing
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()