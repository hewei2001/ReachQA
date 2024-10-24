import matplotlib.pyplot as plt
import numpy as np

# Sample data: Quality scores for coffee farms in five regions
regions = ["Ethiopia", "Colombia", "Costa Rica", "Brazil", "Indonesia"]
quality_scores = [
    [85, 88, 86, 87, 89, 90, 91, 87, 88, 90],  # Ethiopia
    [82, 83, 81, 85, 84, 86, 83, 82, 85, 84],  # Colombia
    [88, 87, 90, 89, 91, 92, 88, 87, 89, 90],  # Costa Rica
    [80, 82, 81, 83, 85, 84, 83, 84, 82, 83],  # Brazil
    [86, 87, 88, 89, 90, 89, 88, 87, 86, 90]   # Indonesia
]

# Calculate average scores over time for each region
average_scores = [np.mean(scores) for scores in quality_scores]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the horizontal box plot
boxes = ax.boxplot(quality_scores, vert=False, patch_artist=True, notch=True,
                   boxprops=dict(facecolor='lightblue', color='navy', linewidth=1.5),
                   whiskerprops=dict(color='navy', linewidth=1.5),
                   capprops=dict(color='navy', linewidth=1.5),
                   medianprops=dict(color='red', linewidth=2),
                   flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Customize box colors for each region
colors = ['lightcoral', 'lightgreen', 'lightskyblue', 'khaki', 'lightpink']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Add a line plot overlay for average quality scores over time
years = np.arange(1, 11)  # Assuming each score represents a different year
for i, (region, scores) in enumerate(zip(regions, quality_scores)):
    ax.plot(scores, [i + 1] * len(scores), label=f'{region} Avg Trend', linestyle='--', marker='x')

# Enhancing the plot with titles and labels
ax.set_title('Variability in Artisan Coffee Bean Quality Across Global Farms\nWith Average Trends Over Time',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Quality Score', fontsize=12)
ax.set_yticks(range(1, len(regions) + 1))
ax.set_yticklabels(regions, fontsize=12)

# Legend for the overlay lines
ax.legend(loc='upper right', fontsize=10, frameon=False)

# Annotate interesting points on the average line plot
ax.annotate('High Variance', xy=(92, 3), xytext=(93, 2.5),
            arrowprops=dict(facecolor='darkgreen', arrowstyle='->'), fontsize=10, color='darkgreen')

# Use tight_layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()