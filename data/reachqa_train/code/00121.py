import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for more detailed funnel steps
steps = [
    "Enrollment",
    "Coursework\nCompletion",
    "Qualifying\nExam",
    "Mid-Candidacy\nReview",
    "Comprehensive\nExams",
    "Proposal\nDefense",
    "Dissertation\nDefense",
    "Graduation"
]

# Number of students at each stage (explicitly constructed data)
student_counts = np.array([1000, 850, 700, 600, 500, 400, 300, 250])

# Calculate dropout rates
dropout_rates = 100 * (1 - student_counts[1:] / student_counts[:-1])

# Normalize widths for funnel-like appearance
widths = student_counts / student_counts[0]

# Define colors for each step
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Add trapezoids for each stage of the funnel
for i in range(len(steps)):
    top_width = widths[i-1] if i > 0 else 1.0
    bottom_width = widths[i]
    
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black'
    )
    ax.add_patch(trapezoid)
    
    # Center text within each trapezoid
    ax.text(0.5, i + 0.5, f"{steps[i]}\n{student_counts[i]} Students",
            ha='center', va='center', fontsize=11, color='black', weight='bold')

    # Add dropout rate annotation if applicable
    if i > 0:
        ax.text(0.95, i + 0.5, f"Dropout: {dropout_rates[i-1]:.1f}%", 
                ha='right', va='center', fontsize=10, color='red', weight='bold')

# Customize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps))
ax.axis('off')  # Remove axes for a cleaner look

# Title and Subtitle
ax.set_title('The Path to PhD:\nAcademic Attrition in STEM Disciplines',
             fontsize=16, weight='bold', ha='center', va='bottom', pad=30)

# Ensure tight layout
plt.tight_layout()

# Display the plot
plt.show()