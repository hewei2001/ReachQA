import matplotlib.pyplot as plt
import numpy as np

# Define extended weekly hours for each ancient script team
hieroglyphics_hours = [10, 12, 9, 11, 10, 14, 13, 15, 12, 10, 12, 13, 11, 14, 15, 16, 14, 13, 17, 15, 18, 19, 20]
mayan_glyphs_hours = [8, 9, 11, 13, 12, 14, 10, 11, 13, 9, 8, 10, 13, 11, 12, 15, 12, 11, 10, 14, 13, 12, 11]
cuneiform_hours = [15, 14, 16, 18, 17, 15, 14, 17, 19, 16, 14, 18, 15, 14, 16, 20, 18, 17, 19, 21, 22, 23, 20]
rongorongo_hours = [7, 8, 6, 9, 5, 7, 6, 8, 9, 7, 8, 5, 7, 6, 8, 9, 10, 9, 8, 7, 11, 12, 13]
indus_script_hours = [12, 14, 13, 11, 15, 13, 12, 15, 11, 14, 13, 12, 10, 14, 13, 16, 14, 12, 11, 17, 16, 15, 14]
linear_a_hours = [9, 10, 8, 9, 11, 10, 11, 12, 8, 7, 8, 9, 10, 11, 9, 9, 8, 7, 8, 9, 10, 8, 11]

# Group data into a list of lists
decipherment_data = [
    hieroglyphics_hours,
    mayan_glyphs_hours,
    cuneiform_hours,
    rongorongo_hours,
    indus_script_hours,
    linear_a_hours
]

# Script names
scripts = [
    "Egyptian Hieroglyphics",
    "Mayan Glyphs",
    "Cuneiform",
    "Rongorongo",
    "Indus Script",
    "Linear A"
]

# Plotting the horizontal box chart
fig, ax = plt.subplots(figsize=(14, 9))

# Create the horizontal box plot
boxplot = ax.boxplot(decipherment_data, vert=False, patch_artist=True,
           boxprops=dict(facecolor='#E5E5E5', color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red'),
           flierprops=dict(marker='o', color='blue', markersize=5, alpha=0.5),
           notch=True, whis=1.5)

# Set the y-axis with the script names
ax.set_yticks(range(1, len(scripts) + 1))
ax.set_yticklabels(scripts, fontsize=11)
ax.set_xlabel('Weekly Hours Spent', fontsize=12)

# Add title and labels with multiple lines
ax.set_title("Deciphering Ancient Scripts: Weekly Hours Distribution\nAcross Different Teams (2023)\nAdvanced Statistical Analysis", 
             fontsize=16, fontweight='bold', pad=20)

# Add grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Customize the color of each box
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFB3E6', '#CCE5FF']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

# Adding a line for the mean for each box plot
means = [np.mean(hours) for hours in decipherment_data]
for i, mean in enumerate(means):
    ax.plot(mean, i + 1, 'D', color='darkorange')
    
# Add legend
legend_elements = [plt.Line2D([0], [0], color='red', lw=2, label='Median'),
                   plt.Line2D([0], [0], marker='D', color='w', label='Mean', markerfacecolor='darkorange', markersize=8),
                   plt.Line2D([0], [0], marker='o', color='w', label='Outliers', markerfacecolor='blue', markersize=5)]

ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()