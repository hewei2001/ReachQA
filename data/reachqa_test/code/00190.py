import matplotlib.pyplot as plt
import numpy as np

# Original data: Vegetable types and their respective yields in kilograms
vegetables = ['Tomatoes', 'Cucumbers', 'Carrots', 'Lettuce', 'Bell Peppers']
yields = [120, 95, 75, 60, 110]  # Hypothetical yields in kg

# Additional data: Nutritional scores for each vegetable
# These scores are hypothetical values representing overall nutrition (out of 100)
nutritional_scores = [80, 70, 85, 75, 78]

# Setup for a 1x2 subplot grid
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Bar Chart of Vegetable Yields
bar_colors = ['#FF6347', '#32CD32', '#FFA500', '#8FBC8F', '#FFD700']
bars = ax1.bar(np.arange(len(yields)), yields, color=bar_colors, alpha=0.8, edgecolor='black')

# Data labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval} kg', ha='center', va='bottom', fontsize=10)

# Customize the first subplot
ax1.set_title("Bountiful Bounty:\nUrban Garden Harvest Yields by Vegetable", fontsize=14, fontweight='bold')
ax1.set_xlabel("Type of Vegetable", fontsize=12)
ax1.set_ylabel("Yield (kg)", fontsize=12)
ax1.set_ylim(0, 140)
ax1.set_xticks(np.arange(len(vegetables)))
ax1.set_xticklabels(vegetables, fontsize=11, rotation=30, ha='right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Subplot 2: Horizontal Bar Chart of Nutritional Scores
bar_colors_horizontal = ['#FF4500', '#2E8B57', '#FFA07A', '#556B2F', '#FFDAB9']
h_bars = ax2.barh(np.arange(len(nutritional_scores)), nutritional_scores, color=bar_colors_horizontal, alpha=0.8, edgecolor='black')

# Data labels for horizontal bars
for bar in h_bars:
    xval = bar.get_width()
    ax2.text(xval + 1, bar.get_y() + bar.get_height()/2, f'{xval}/100', va='center', fontsize=10)

# Customize the second subplot
ax2.set_title("Nutritional Power:\nScores of Each Vegetable", fontsize=14, fontweight='bold')
ax2.set_xlabel("Nutritional Score", fontsize=12)
ax2.set_xlim(0, 100)
ax2.set_yticks(np.arange(len(vegetables)))
ax2.set_yticklabels(vegetables, fontsize=11)
ax2.xaxis.grid(True, linestyle='--', alpha=0.5)
ax2.set_axisbelow(True)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()