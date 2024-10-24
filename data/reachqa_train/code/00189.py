import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data representing energy at each stage of the funnel in megawatts (MW)
stages = ["Raw Energy Input", "Generation Losses", "Transmission Losses", "Distribution Losses", "End-User Utilization"]
values = [1000, 800, 700, 650, 600]  # Decreasing values due to losses

# Colors for each stage
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the funnel plot
fig, ax = plt.subplots(figsize=(10, 7))

# Calculate trapezoid width positions for the funnel effect
for i in range(len(stages)):
    x1 = (values[0] - values[i]) / 2
    x2 = x1 + values[i]
    height = 1.5
    y = -i * height
    polygon = patches.Polygon([[x1, y], [x2, y], [x2, y - height], [x1, y - height]],
                              closed=True, color=colors[i], edgecolor='black', linewidth=1.2)
    ax.add_patch(polygon)

    # Add text inside each section of the funnel
    ax.text((x1 + x2) / 2, y - height / 2, f"{stages[i]}\n{values[i]} MW", 
            va='center', ha='center', color='white', fontsize=10, fontweight='bold')

# Set labels and title
ax.set_xlim(0, values[0])
ax.set_ylim(-len(stages) * height, 0)
ax.set_axis_off()  # Turn off axis
ax.set_title("Energy Efficiency Funnel:\nFrom Source to Socket", fontsize=14, weight='bold', pad=20)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()