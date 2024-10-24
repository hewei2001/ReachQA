import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Define colleges and their percentage growth in fantasy literature courses
colleges = ['Hogwarts University', 'Middle-earth College', 'Narnia Institute', 
            'Westeros Academy', 'Avalon College']
growth_percentages = [25, 18, 30, 20, 22]

# Additional data: average student satisfaction scores
satisfaction_scores = [4.5, 4.2, 4.8, 4.3, 4.4]

# Colors and patterns for the bars
bar_colors = ['#8A2BE2', '#5F9EA0', '#D2691E', '#FF7F50', '#556B2F']
hatches = ['/', '\\', '|', '-', '+']

# Create figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create the bar chart
bars = ax1.bar(colleges, growth_percentages, color=bar_colors, edgecolor='black', hatch=hatches)

# Set titles and labels
ax1.set_title('Annual Growth in Student Enrollment\nand Student Satisfaction Scores 2023', fontsize=16, fontweight='bold')
ax1.set_xlabel('Colleges', fontsize=12)
ax1.set_ylabel('Growth in Enrollment (%)', fontsize=12)
ax1.set_ylim(0, max(growth_percentages) + 10)

# Add grid for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

# Annotate bars with growth percentages
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10)

# Create a secondary axis for student satisfaction scores
ax2 = ax1.twinx()
ax2.plot(colleges, satisfaction_scores, color='darkred', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Student Satisfaction (1-5)', fontsize=12, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=15, ha='right')

# Create custom legend
handles = [mpatches.Patch(color=bar_colors[i], label=f'{colleges[i]} Growth', hatch=hatches[i]) for i in range(len(colleges))]
handles.append(mpatches.Patch(color='darkred', label='Satisfaction Score', linestyle='-', linewidth=2))
ax1.legend(handles=handles, loc='upper left')

# Ensure layout is tight so nothing overlaps
plt.tight_layout()

# Show the plot
plt.show()