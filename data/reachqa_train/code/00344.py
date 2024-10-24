import matplotlib.pyplot as plt
import numpy as np

# Define decades and fashion styles
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
mod = [80, 40, 20, 50, 60, 55]
disco = [10, 90, 40, 20, 30, 25]
punk = [5, 30, 80, 40, 30, 20]
grunge = [0, 0, 10, 90, 60, 50]
boho = [15, 20, 25, 50, 85, 90]

# Compile data into a list for convenience
styles_data = [mod, disco, punk, grunge, boho]
styles_labels = ['Mod', 'Disco', 'Punk', 'Grunge', 'Boho']

# Create the plot
plt.figure(figsize=(14, 8))

# Plot each fashion style
for index, style in enumerate(styles_data):
    plt.plot(decades, style, marker='o', linestyle='-', linewidth=2, markersize=6, label=styles_labels[index])

# Annotate key points
annotations = {
    'Mod': ('1960s', 80, 'Peak of Mod'),
    'Disco': ('1970s', 90, 'Disco Craze'),
    'Punk': ('1980s', 80, 'Punk Rise'),
    'Grunge': ('1990s', 90, 'Grunge Peak'),
    'Boho': ('2010s', 90, 'Boho Revival')
}

# Add annotations
for style, (decade, popularity, annotation) in annotations.items():
    plt.annotate(annotation, xy=(decade, popularity), xytext=(20, -15),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1.5),
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Title and labels
plt.title('The Evolution of Vintage Fashion Trends\nOver the Decades', fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)
plt.legend(title='Fashion Styles', loc='upper left', bbox_to_anchor=(1, 1))

# Grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show plot
plt.show()