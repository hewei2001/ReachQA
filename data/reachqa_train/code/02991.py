import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Recruitment stages and candidate counts
stages = [
    "Applicants",
    "Phone Screening",
    "Technical Test",
    "On-site Interview",
    "Offer Extended",
    "Hired"
]

candidate_counts = [1000, 600, 350, 150, 80, 40]

# Colors for each stage
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']

# Figure setup
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, max(candidate_counts) + 200)
ax.set_ylim(0, len(stages))

# Plot each section of the funnel
for i in range(len(stages) - 1):
    left = (max(candidate_counts) - candidate_counts[i]) / 2
    width_top = candidate_counts[i]
    width_bottom = candidate_counts[i + 1]
    height = 1

    # Draw trapezoids
    trapezoid = patches.Polygon(
        [
            (left, i),  # Top left
            (left + width_top, i),  # Top right
            (left + (width_top + width_bottom) / 2, i + height),  # Bottom right
            (left + (width_top - width_bottom) / 2, i + height)   # Bottom left
        ],
        closed=True, color=colors[i], edgecolor='grey'
    )
    ax.add_patch(trapezoid)

# Last stage (rectangle)
left = (max(candidate_counts) - candidate_counts[-1]) / 2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), candidate_counts[-1], 1, color=colors[-1], edgecolor='grey'
)
ax.add_patch(rectangle)

# Label each section
for i, (stage, count) in enumerate(zip(stages, candidate_counts)):
    ax.text(max(candidate_counts) / 2, i + 0.5, f'{stage}: {count}', va='center', ha='center',
            color='black', fontsize=12, fontweight='bold')

# Axis formatting
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('TechNovate Recruitment Funnel in 2023\nCandidate Progression Through Stages', fontsize=16, fontweight='bold')

# Remove spines to enhance the funnel look
for spine in ax.spines.values():
    spine.set_visible(False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()