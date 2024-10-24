import matplotlib.pyplot as plt
import numpy as np

# Art Movements and their corresponding influence scores
art_movements = [
    "Proto-Renaissance",
    "Early Renaissance",
    "High Renaissance",
    "Mannerism",
    "Northern Renaissance",
    "Venetian Renaissance",
    "Late Renaissance"
]

impact_scores = [30, 45, 80, 50, 60, 55, 35]

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.6

# Creating the horizontal bar chart
colors = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039', '#581845', '#8E44AD', '#3498DB']
bars = ax.barh(art_movements, impact_scores, color=colors, height=bar_height)

# Adding text annotations to bars
for bar in bars:
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2, 
            f'{bar.get_width()}', va='center', ha='left', fontsize=10, color='black')

# Titles and labels
ax.set_title('Evolution of Renaissance Art Movements:\nA Horizontal Insight', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Impact Score (Estimated)', fontsize=12)
ax.set_ylabel('Art Movements', fontsize=12)
ax.set_xlim(0, 90)

# Adding a legend for better identification
legend_elements = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(colors, art_movements)]
ax.legend(handles=legend_elements, title='Art Movements', loc='lower right', frameon=True, fontsize=10)

# Customizing grid and appearance
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()