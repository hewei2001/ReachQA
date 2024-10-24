import matplotlib.pyplot as plt
import numpy as np

# Define domains and expertise scores for Leonardo and external assessment (out of 100)
domains = ['Art', 'Anatomy', 'Engineering', 'Mathematics', 'Botany', 'Astronomy']
leonardo_scores = [95, 85, 90, 80, 75, 70]
external_assessment_scores = [88, 78, 85, 75, 68, 62]

# Number of variables we're plotting
num_vars = len(domains)

# Create a 360-degree angle representation and append the start to close the loop
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
leonardo_scores += leonardo_scores[:1]
external_assessment_scores += external_assessment_scores[:1]
angles += angles[:1]

# Initiate a radar plot
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

# Draw one full line per variable and fill the space for Leonardo's scores
ax.fill(angles, leonardo_scores, color='cyan', alpha=0.3)
ax.plot(angles, leonardo_scores, color='blue', linewidth=2, label='Leonardo Self-Assessment')

# Overlay with external assessment using a bar chart, adjust the width and alpha to reduce occlusion
bar_width = 0.08  # Reduced width
bars = ax.bar(angles[:-1], external_assessment_scores[:-1], width=bar_width, 
              color='orange', alpha=0.6, label='External Assessment', align='center')

# Enhance the radar chart with gridlines and labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(domains, fontsize=12, color='darkblue')

# Add a title with multi-line support
ax.set_title('The Renaissance Scholar:\nA Comparative Radar Chart of Expertise', 
             size=14, color='navy', weight='bold', va='bottom', pad=20)

# Add a legend outside the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), frameon=False)

# Automatically adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()