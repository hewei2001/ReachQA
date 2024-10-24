import matplotlib.pyplot as plt

# Sample data: Quality scores for coffee farms in five regions
regions = ["Ethiopia", "Colombia", "Costa Rica", "Brazil", "Indonesia"]
quality_scores = [
    [85, 88, 86, 87, 89, 90, 91, 87, 88, 90],  # Ethiopia
    [82, 83, 81, 85, 84, 86, 83, 82, 85, 84],  # Colombia
    [88, 87, 90, 89, 91, 92, 88, 87, 89, 90],  # Costa Rica
    [80, 82, 81, 83, 85, 84, 83, 84, 82, 83],  # Brazil
    [86, 87, 88, 89, 90, 89, 88, 87, 86, 90]   # Indonesia
]

# Creating the horizontal box plot
plt.figure(figsize=(14, 8))
boxes = plt.boxplot(quality_scores, vert=False, patch_artist=True, notch=True,
                    boxprops=dict(facecolor='lightblue', color='navy', linewidth=1.5),
                    whiskerprops=dict(color='navy', linewidth=1.5),
                    capprops=dict(color='navy', linewidth=1.5),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

# Customize box colors for each region
colors = ['lightcoral', 'lightgreen', 'lightskyblue', 'khaki', 'lightpink']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

# Enhancing the plot with titles and labels
plt.title('Variability in Artisan Coffee Bean Quality\nAcross Global Farms', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Quality Score', fontsize=12)
plt.yticks(range(1, len(regions) + 1), regions, fontsize=12)

# Adding a brief legend
plt.figtext(0.15, 0.85, "Notched boxes indicate 95% CI around the median.", fontsize=10)

# Annotate interesting points
plt.annotate('High Variance', xy=(92, 3), xytext=(93, 3.5),
             arrowprops=dict(facecolor='darkgreen', arrowstyle='->'), fontsize=10, color='darkgreen')

# Use tight_layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()