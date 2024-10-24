import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Synthetic Data: Color saturation preferences in percentage for different age groups
youth_saturation = [60, 55, 75, 80, 70, 68, 74, 60, 65, 85, 90, 77, 72, 66, 69]
adult_saturation = [50, 48, 53, 55, 58, 60, 59, 62, 57, 63, 61, 54, 56, 64, 52]
senior_saturation = [30, 35, 40, 42, 45, 37, 39, 38, 41, 33, 36, 34, 31, 43, 44]

saturation_data = [youth_saturation, adult_saturation, senior_saturation]
group_labels = ['Youth (18-25)', 'Adults (26-40)', 'Seniors (41-60)']

plt.figure(figsize=(14, 8))

# Create the box plot
box = plt.boxplot(saturation_data, patch_artist=True, notch=True, vert=True, labels=group_labels, flierprops=dict(marker='o', color='red', alpha=0.5))

# Customizing box plot colors
colors = ['#F28E2B', '#4E79A7', '#76B7B2']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Add mean markers
for i, data in enumerate(saturation_data):
    mean_val = np.mean(data)
    plt.plot(i + 1, mean_val, marker='D', color='darkblue')

# Add swarm plot for data distribution detail
for i, data in enumerate(saturation_data):
    x = np.random.normal(i + 1, 0.04, size=len(data))  # Add jitter to x-axis
    plt.scatter(x, data, alpha=0.7, color='black')

# Titles and labels
plt.title("Color Saturation Preferences in Abstract Art\nAcross Different Age Groups", fontsize=16, weight='bold')
plt.xlabel("Age Group", fontsize=14, weight='bold')
plt.ylabel("Saturation Preference (%)", fontsize=14, weight='bold')

# Grid for readability
plt.grid(True, linestyle='--', alpha=0.7)

# Custom legend
handles = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(colors, group_labels)]
plt.legend(handles=handles, loc='upper right', fontsize=10, frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()