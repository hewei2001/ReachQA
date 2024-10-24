import matplotlib.pyplot as plt
import numpy as np

# Popularity scores for each flavor across decades
# Each sublist represents a decade and contains scores for each flavor
popularity_data = np.array([
    [70, 80, 60, 50, 10],  # 1960
    [65, 75, 55, 45, 20],  # 1970
    [60, 72, 50, 55, 30],  # 1980
    [55, 68, 45, 60, 40],  # 1990
    [50, 65, 40, 65, 50],  # 2000
    [45, 60, 35, 70, 60],  # 2010
    [40, 55, 30, 75, 70],  # 2020
])

# Define flavor names for labeling
flavor_labels = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough"]

# Create a boxplot
plt.figure(figsize=(12, 8))
boxplot = plt.boxplot(popularity_data, patch_artist=True, labels=flavor_labels, notch=True, vert=True)

# Customizing the boxplot with colors and styles
colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

for whisker in boxplot['whiskers']:
    whisker.set(color='black', linewidth=1.5, linestyle='--')

for cap in boxplot['caps']:
    cap.set(color='black', linewidth=1.5)

for median in boxplot['medians']:
    median.set(color='yellow', linewidth=2)

# Title and labels
plt.title("Flavors of the Decade:\nA Journey Through Popular Ice Cream Varieties", fontsize=14, fontweight='bold')
plt.xlabel("Ice Cream Flavors", fontsize=12)
plt.ylabel("Popularity Score (0-100)", fontsize=12)

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate the trend of a new favorite emerging over time
plt.annotate('Emerging Favorite', xy=(5, 65), xytext=(4, 80),
             arrowprops=dict(facecolor='gray', shrink=0.05),
             fontsize=10, fontweight='bold', color='brown')

# Automatically adjust layout for better presentation
plt.tight_layout()

# Display the plot
plt.show()