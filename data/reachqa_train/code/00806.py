import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Funnel stages and user data
stages = ["Awareness", "Interest", "Consideration", "Conversion", "Loyalty"]
users = [100000, 70000, 40000, 25000, 10000]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Reverse the stages and data for top-down plotting
stages.reverse()
users.reverse()
colors.reverse()

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 10))

# Define the width and height for each stage
max_width = max(users)
height = 0.2

# Plot each stage as a trapezoid using the patches module
for i in range(len(stages)):
    left_width = users[i] / max_width * 0.8  # Normalize width to max width
    rect = patches.Rectangle((0.1, i * (height + 0.1)), left_width, height, color=colors[i], edgecolor='gray', linewidth=1.5)
    ax.add_patch(rect)
    # Annotate the stage name and user count
    ax.text(0.1 + left_width / 2, i * (height + 0.1) + height / 2, 
            f"{stages[i]}: {users[i]:,}", ha='center', va='center', color='white', fontsize=10, fontweight='bold')

# Set titles and labels
ax.set_title("2023 Social Media User Journey Funnel:\nFrom Awareness to Loyalty", fontsize=14, fontweight='bold')
ax.set_xlabel("Stage of Journey", fontsize=12)
ax.set_ylabel("Number of Users", fontsize=12)

# Customize the x and y axis
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages) * (height + 0.1))
ax.set_xticks([])
ax.set_yticks([])

# Remove axis spines for a cleaner look
for spine in ax.spines.values():
    spine.set_visible(False)

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()