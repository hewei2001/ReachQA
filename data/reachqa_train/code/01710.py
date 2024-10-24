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
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bottom of each stack (cumulative sum of previous rows)
cumulative_data = np.zeros(len(decades))

# Colors for each style
colors = ['#8B4513', '#FF7F50', '#4682B4', '#DA70D6', '#98FB98']

# Plot each style as a stacked bar
for i, (style, color) in enumerate(zip(styles, colors)):
    ax.bar(decades, data[:, i], bottom=cumulative_data, color=color, label=style, edgecolor='gray', alpha=0.8)
    cumulative_data += data[:, i]  # Update the base for the next style

# Add title and labels
ax.set_title('Evolution of Architectural Styles in Archovia:\nA Century of Transformation', fontsize=16, pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Prevalence (Percentage of New Buildings)', fontsize=12)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Styles")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()