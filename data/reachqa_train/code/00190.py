import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Data for the funnel plot
stages = ["Raw Energy Input", "Generation Losses", "Transmission Losses", "Distribution Losses", "End-User Utilization"]
values = [1000, 800, 700, 650, 600]  # Energy values in MW

# Calculate energy efficiency percentages
efficiency_percentages = [values[i] / values[i - 1] * 100 for i in range(1, len(values))]
efficiency_percentages.insert(0, 100)  # 100% at the starting point

# Derived data for the bar chart: Potential Savings
potential_savings = [values[i] - values[i+1] for i in range(len(values) - 1)]
potential_savings.append(50)  # Assuming a nominal potential saving at end-user utilization

# Colors for each stage
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

# Create the figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# First subplot: Funnel plot
ax1 = axs[0]
for i, (stage, value, color) in enumerate(zip(stages, values, colors)):
    x1 = (values[0] - value) / 2
    x2 = x1 + value
    height = 1.5
    y = -i * height
    polygon = patches.Polygon([[x1, y], [x2, y], [x2, y - height], [x1, y - height]],
                              closed=True, color=color, edgecolor='black', linewidth=1.2)
    ax1.add_patch(polygon)
    ax1.text((x1 + x2) / 2, y - height / 2, f"{stage}\n{value} MW\n({efficiency_percentages[i]:.1f}%)",
             va='center', ha='center', color='white', fontsize=9, fontweight='bold')

ax1.set_xlim(0, values[0])
ax1.set_ylim(-len(stages) * height, 0)
ax1.set_axis_off()
ax1.set_title("Energy Efficiency Funnel:\nFrom Source to Socket", fontsize=14, weight='bold', pad=20)

# Second subplot: Bar chart for potential savings
ax2 = axs[1]
bars = ax2.barh(stages, potential_savings, color=colors, edgecolor='black')
ax2.set_xlabel('Potential Energy Savings (MW)', fontsize=12)
ax2.set_title("Potential Energy Savings at Each Stage", fontsize=14, weight='bold', pad=20)

# Annotating the bars with their values
for bar, savings in zip(bars, potential_savings):
    ax2.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
             f'{savings} MW', va='center', ha='left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()