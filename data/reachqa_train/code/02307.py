import matplotlib.pyplot as plt
import numpy as np

# Data preparation
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
awards = np.array([3, 7, 12, 15, 20, 25, 30])

# Annotations for key milestones in genre recognition
annotations = [
    "1965: Hugo Award established",
    "1970: Nebula Awards gain popularity",
    "1985: World Fantasy Award launched",
    "1995: SFWA Grand Master Award created",
    "2005: Increased award diversity",
    "2015: More genre-specific awards",
    "2025: Major international acceptance"
]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the line chart
ax.plot(decades, awards, marker='o', color='teal', linestyle='-', linewidth=2, markersize=8, label='Number of Awards')

# Adding annotations at each data point with text wrapping
for i, txt in enumerate(annotations):
    ax.annotate(txt, (decades[i], awards[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='darkgreen', 
                bbox=dict(facecolor='lightyellow', edgecolor='gray', boxstyle='round,pad=0.3'))

# Set the title and labels with appropriate line breaks
ax.set_title('The Evolution of Literary Awards for Science Fiction & Fantasy\n(1960s to 2020s)', fontsize=14, fontweight='bold', ha='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Number of Awards', fontsize=12)

# Adding a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a legend
ax.legend(loc='upper left', frameon=False)

# Adjusting layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()