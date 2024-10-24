import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Noise levels (in decibels) for five urban libraries
library_a = [35, 40, 42, 45, 38, 41, 37, 44, 39, 40, 43, 42, 45, 46, 47, 39, 40, 41]
library_b = [50, 52, 51, 54, 53, 52, 50, 51, 53, 52, 54, 56, 58, 57, 55, 53, 52, 51]
library_c = [60, 62, 65, 63, 61, 60, 62, 64, 63, 65, 66, 64, 63, 62, 61, 60, 64, 66]
library_d = [70, 72, 71, 73, 74, 72, 71, 70, 72, 73, 74, 73, 75, 74, 72, 71, 70, 72]
library_e = [45, 48, 50, 47, 46, 45, 49, 50, 51, 47, 46, 49, 50, 53, 52, 51, 49, 47]

# Combine the data into a list
data = [library_a, library_b, library_c, library_d, library_e]

# Set up the figure and axis
plt.figure(figsize=(14, 10))
plt.subplot(1, 1, 1)  # Single subplot for the boxplot

# Create the boxplot
box = plt.boxplot(data, patch_artist=True, vert=True, 
                  labels=["Library A", "Library B", "Library C", "Library D", "Library E"],
                  notch=True, widths=0.6)

# Define and apply color map
cmap = plt.cm.viridis
colors = [cmap(i) for i in np.linspace(0, 1, len(data))]

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_edgecolor('darkblue')

# Customizing whiskers, caps, and medians
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
for median in box['medians']:
    median.set(color='red', linewidth=2)

# Add individual data points with jitter
for i, y in enumerate(data):
    x = np.random.normal(i + 1, 0.04, size=len(y))
    plt.scatter(x, y, alpha=0.6, color=colors[i], edgecolor='darkblue')

# Add mean markers
means = [np.mean(library) for library in data]
plt.plot(range(1, len(means)+1), means, marker='D', color='black', linestyle='none', label='Mean')

# Title and labels
plt.title("Monthly Noise Levels in Various Urban Libraries\n(January - June 2023)", fontsize=16, fontweight='bold')
plt.ylabel("Noise Level (Decibels)", fontsize=14)
plt.xlabel("Libraries", fontsize=14)

# Grid, legend, and layout
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Display the plot
plt.show()