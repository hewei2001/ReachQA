import matplotlib.pyplot as plt
import numpy as np

# Define synthetic popularity data for each fashion trend over 20 years
bohemian_chic_scores = [30, 35, 40, 50, 55, 60, 58, 62, 67, 70, 72, 68, 65, 63, 60, 58, 57, 54, 53, 50]
cyberpunk_scores = [20, 25, 30, 35, 42, 48, 50, 52, 51, 50, 55, 60, 58, 62, 65, 68, 72, 75, 78, 80]
minimalism_scores = [60, 58, 55, 50, 48, 46, 45, 44, 43, 42, 40, 38, 37, 36, 35, 35, 34, 33, 32, 31]
streetwear_scores = [10, 12, 15, 18, 25, 30, 35, 40, 50, 60, 65, 70, 75, 80, 85, 90, 92, 95, 97, 100]
vintage_scores = [40, 42, 43, 45, 48, 50, 52, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 68, 70, 72]

# Combine data into a list
data = [
    bohemian_chic_scores,
    cyberpunk_scores,
    minimalism_scores,
    streetwear_scores,
    vintage_scores
]

# Labels for the trends
trend_labels = ['Bohemian Chic', 'Cyberpunk', 'Minimalism', 'Streetwear', 'Vintage Revival']

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))
boxprops = dict(linestyle='-', linewidth=2, color='darkblue', facecolor='#b3cde3', alpha=0.7)
whiskerprops = dict(linestyle='-', linewidth=1.5, color='royalblue')
capprops = dict(linestyle='-', linewidth=2, color='royalblue')
medianprops = dict(linestyle='-', linewidth=2.5, color='darkorange')

ax.boxplot(data, vert=False, patch_artist=True, labels=trend_labels, boxprops=boxprops, 
           whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops, notch=True)

# Set plot titles and labels
ax.set_title("The Evolution of Fashion Trends:\nA Snapshot from the Archives (2000-2020)", fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel("Popularity Score (0 to 100)", fontsize=12)
ax.set_ylabel("Fashion Trends", fontsize=12)

# Customize the appearance
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

# Add a grid for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Optimize layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()