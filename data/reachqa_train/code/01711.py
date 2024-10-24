import matplotlib.pyplot as plt
import numpy as np

# Decades for the x-axis
decades = ['1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s']

# Architectural styles
styles = ['Gothic Revival', 'Art Deco', 'Modernist', 'Postmodern', 'Contemporary']

# Data for each style (percentage of new buildings constructed in each style by decade)
data = np.array([
    [40, 20, 10, 0, 0],  # 1920s
    [35, 30, 15, 0, 0],  # 1930s
    [30, 25, 25, 0, 0],  # 1940s
    [25, 15, 40, 0, 0],  # 1950s
    [10, 5, 60, 0, 5],   # 1960s
    [5, 0, 40, 10, 15],  # 1970s
    [0, 0, 20, 30, 30],  # 1980s
    [0, 0, 10, 40, 35],  # 1990s
    [0, 0, 5, 30, 40],   # 2000s
    [0, 0, 0, 20, 50]    # 2010s
])

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 9))

# Create the bottom of each stack (cumulative sum of previous rows)
cumulative_data = np.zeros(len(decades))

# Colors for each style
colors = ['#8B4513', '#FF7F50', '#4682B4', '#DA70D6', '#98FB98']

# Plot each style as a stacked bar with gradients for depth
for i, (style, color) in enumerate(zip(styles, colors)):
    ax.bar(decades, data[:, i], bottom=cumulative_data, color=color, edgecolor='gray', alpha=0.7 - i*0.1, label=style)
    cumulative_data += data[:, i]

# Add title and labels
ax.set_title('Evolution of Architectural Styles in Archovia:\nA Century of Transformation', fontsize=16, pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Prevalence (Percentage of New Buildings)', fontsize=12)

# Add horizontal grid lines for better readability
ax.yaxis.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)

# Annotations for key transitions
ax.annotate('Modernist peak', xy=(4, 70), xytext=(5, 80),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Highlight every other decade label for visual distinction
for label in ax.get_xticklabels()[::2]:
    label.set_fontweight('bold')

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Styles")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()