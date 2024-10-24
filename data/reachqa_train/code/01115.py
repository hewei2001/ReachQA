import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the stages and corresponding data
stages = [
    "Idea Generation", 
    "Manuscript Drafting", 
    "First Editing", 
    "Peer Review", 
    "Final Editing", 
    "Publishing"
]
authors_count = [1000, 800, 600, 400, 250, 100]

# Additional hypothetical data: average time spent (in weeks) at each stage
average_time_weeks = [5, 10, 8, 12, 6, 4]

# Define colors for each stage
colors = ['#3498db', '#9b59b6', '#e74c3c', '#f39c12', '#2ecc71', '#e67e22']

# Create figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 1]})

# First subplot: Funnel Chart
max_width = authors_count[0]

for i, stage in enumerate(stages):
    left_width = authors_count[i] / max_width
    right_width = authors_count[i+1] / max_width if i+1 < len(authors_count) else 0.1

    vertices = [
        (-left_width/2, -i),  # bottom-left
        (left_width/2, -i),   # bottom-right
        (right_width/2, -i-1),  # top-right
        (-right_width/2, -i-1)  # top-left
    ]
    
    trap = patches.Polygon(vertices, closed=True, color=colors[i], edgecolor='grey')
    ax1.add_patch(trap)

    ax1.text(0, -i-0.5, f"{stages[i]}: {authors_count[i]} authors", 
             va='center', ha='center', color='white', fontsize=9, weight='bold')

ax1.set_xlim(-0.6, 0.6)
ax1.set_ylim(-len(stages), 0)
ax1.set_title("Journey of Sci-Fi Book Authors\n to Publishing Success", fontsize=13, fontweight='bold')
ax1.axis('off')

# Second subplot: Bar Chart
ax2.barh(stages, average_time_weeks, color=colors, edgecolor='grey')
ax2.set_xlabel('Average Time (weeks)', fontsize=10, weight='bold')
ax2.set_title("Average Time Spent at Each Stage", fontsize=13, fontweight='bold')
ax2.invert_yaxis()

for i, time in enumerate(average_time_weeks):
    ax2.text(time + 0.5, i, f'{time} weeks', va='center', fontsize=9)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the combined chart
plt.show()