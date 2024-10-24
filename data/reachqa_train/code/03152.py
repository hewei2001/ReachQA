import matplotlib.pyplot as plt
import numpy as np

# Define the competencies in healthcare innovation
competencies = [
    'Digital Health', 
    'Telemedicine', 
    'Genomics', 
    'AI in Diagnostics', 
    'Robotics Surgery'
]

# Strategic emphasis scores for each competency (scale 0-10)
scores_2025 = [8, 7, 9, 8, 6]
scores_2030 = [9, 6, 8, 9, 7]  # Hypothetical future data for comparison

# Extend scores to close the radar chart loop
scores_2025 += scores_2025[:1]
scores_2030 += scores_2030[:1]

# Calculate angle for each competency in the radar chart
angles = np.linspace(0, 2 * np.pi, len(competencies), endpoint=False).tolist()
angles += angles[:1]

# Create radar chart with polar coordinates
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Offset the starting angle to the top
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Plot the data for 2025
ax.plot(angles, scores_2025, linewidth=2, linestyle='solid', label='2025', color='navy', marker='o')
ax.fill(angles, scores_2025, color='blue', alpha=0.2)

# Plot the data for 2030
ax.plot(angles, scores_2030, linewidth=2, linestyle='solid', label='2030', color='darkorange', marker='s')
ax.fill(angles, scores_2030, color='orange', alpha=0.2)

# Add labels for each competency
ax.set_xticks(angles[:-1])
ax.set_xticklabels(competencies, fontsize=12, color='darkblue')

# Add title with line breaks for readability
ax.set_title("Strategic Focus on Key Competencies\nin Healthcare Innovation", 
             size=14, weight='bold', color='navy', va='bottom')

# Customize radial grid and labels
ax.yaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
ax.xaxis.grid(True, color='gray', linestyle='--', alpha=0.5)
ax.set_yticks([0, 2, 4, 6, 8, 10])
ax.set_yticklabels(['0', '2', '4', '6', '8', '10'], color='gray', size=10)

# Remove the polar spine for a cleaner look
ax.spines['polar'].set_visible(False)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the radar chart
plt.show()