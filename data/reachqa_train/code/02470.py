import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data for the funnel
stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Conversion']
users = [10000, 6000, 3000, 1200, 600]
colors = ['#007acc', '#3399ff', '#66b2ff', '#99ccff', '#cce6ff']

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Function to add funnel segments
def add_funnel_segment(ax, width, height, y_offset, color, label, user_count):
    left = (max(users) - width) / 2  # Center the segment
    rect = patches.FancyBboxPatch((left, y_offset), width, height,
                                  boxstyle="round,pad=0.02", color=color, ec="black")
    ax.add_patch(rect)
    ax.text(max(users) / 2, y_offset + height / 2, f'{label}\n{user_count} users', 
            va='center', ha='center', fontsize=10, color='black', fontweight='bold')

# Plot each stage of the funnel
y_offset = 0
height = 1
for i in range(len(stages)):
    width = users[i]
    add_funnel_segment(ax, width, height, y_offset, colors[i], stages[i], users[i])
    y_offset += height + 0.1  # Add some spacing between segments

# Set title and labels
ax.set_title('AdWizards Campaign Funnel Analysis', fontsize=16, fontweight='bold')
ax.set_xlim(0, max(users))
ax.set_ylim(0, y_offset)

# Remove axes for a cleaner look
ax.axis('off')

# Automatically adjust layout
plt.tight_layout()

# Display the funnel chart
plt.show()