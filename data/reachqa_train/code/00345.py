import matplotlib.pyplot as plt
import numpy as np

# Define decades and fashion styles
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
mod = [80, 40, 20, 50, 60, 55]
disco = [10, 90, 40, 20, 30, 25]
punk = [5, 30, 80, 40, 30, 20]
grunge = [0, 0, 10, 90, 60, 50]
boho = [15, 20, 25, 50, 85, 90]

# Cultural Influence Scores
influence_score = [50, 70, 65, 80, 75, 85]

# Compile data into a list for convenience
styles_data = [mod, disco, punk, grunge, boho]
styles_labels = ['Mod', 'Disco', 'Punk', 'Grunge', 'Boho']

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each fashion style
for index, style in enumerate(styles_data):
    ax1.plot(decades, style, marker='o', linestyle='-', linewidth=2, markersize=6, label=styles_labels[index])

# Set title and labels
ax1.set_title('The Evolution of Vintage Fashion Trends\nAnd Their Cultural Influence Over the Decades', fontsize=16, fontweight='bold')
ax1.set_xlabel('Decades', fontsize=12)
ax1.set_ylabel('Popularity Score', fontsize=12)

# Annotate key points
annotations = {
    'Mod': ('1960s', 80, 'Peak of Mod'),
    'Disco': ('1970s', 90, 'Disco Craze'),
    'Punk': ('1980s', 80, 'Punk Rise'),
    'Grunge': ('1990s', 90, 'Grunge Peak'),
    'Boho': ('2010s', 90, 'Boho Revival')
}

for style, (decade, popularity, annotation) in annotations.items():
    ax1.annotate(annotation, xy=(decade, popularity), xytext=(20, -15),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1.5),
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Create a secondary y-axis for the cultural influence score
ax2 = ax1.twinx()
ax2.bar(decades, influence_score, color='lightblue', alpha=0.5, width=0.3, label='Cultural Influence Score')
ax2.set_ylabel('Cultural Influence Score', fontsize=12)

# Add legends for both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1, 1))

# Grid for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show plot
plt.show()