import matplotlib.pyplot as plt
import numpy as np

# Noise levels (in decibels) for five urban libraries
library_a = [35, 40, 42, 45, 38, 41, 37, 44, 39, 40, 43, 42, 45, 46, 47, 39, 40, 41]
library_b = [50, 52, 51, 54, 53, 52, 50, 51, 53, 52, 54, 56, 58, 57, 55, 53, 52, 51]
library_c = [60, 62, 65, 63, 61, 60, 62, 64, 63, 65, 66, 64, 63, 62, 61, 60, 64, 66]
library_d = [70, 72, 71, 73, 74, 72, 71, 70, 72, 73, 74, 73, 75, 74, 72, 71, 70, 72]
library_e = [45, 48, 50, 47, 46, 45, 49, 50, 51, 47, 46, 49, 50, 53, 52, 51, 49, 47]

# Combine the data into a list
data = [library_a, library_b, library_c, library_d, library_e]

# Create a boxplot with customized appearance
plt.figure(figsize=(12, 8))
box = plt.boxplot(data, patch_artist=True, vert=True, 
                  labels=["Library A", "Library B", "Library C", "Library D", "Library E"],
                  notch=True, widths=0.6)

# Define custom colors for the boxes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Color and style adjustments
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
    patch.set_edgecolor('darkblue')

# Customizing the whiskers, caps, and medians
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")

for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)

for median in box['medians']:
    median.set(color='red', linewidth=2)

# Setting the title and labels
plt.title("Monthly Noise Levels in Various Urban Libraries\n(January - June)", fontsize=16, fontweight='bold', pad=20)
plt.ylabel("Noise Level (Decibels)", fontsize=14)
plt.xlabel("Libraries", fontsize=14)

# Add a grid for easier comparison
plt.grid(True, linestyle='--', alpha=0.5)

# Apply tight_layout to automatically adjust for overlap
plt.tight_layout()

# Display the plot
plt.show()