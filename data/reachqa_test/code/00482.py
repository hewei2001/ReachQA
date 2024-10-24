import matplotlib.pyplot as plt
import numpy as np

# Define years and sectors
sectors = ['Retail', 'Hospitality', 'Health & Fitness', 'Real Estate', 'E-commerce', 'Technology', 'Transportation', 'Education', 'Finance']

# Percentage revenue increase from social media marketing for each sector across 10 data points
data = {
    'Retail': [5, 10, 15, 20, 8, 12, 17, 22, 6, 14],
    'Hospitality': [3, 7, 12, 18, 5, 9, 13, 16, 2, 11],
    'Health & Fitness': [4, 9, 14, 22, 6, 10, 15, 19, 8, 13],
    'Real Estate': [2, 8, 10, 15, 3, 11, 14, 17, 4, 12],
    'E-commerce': [6, 13, 17, 25, 9, 14, 18, 20, 7, 21],
    'Technology': [8, 15, 20, 26, 11, 19, 22, 24, 14, 16],
    'Transportation': [1, 4, 8, 11, 6, 10, 13, 15, 9, 7],
    'Education': [5, 6, 8, 12, 10, 14, 19, 20, 7, 11],
    'Finance': [3, 9, 10, 12, 5, 11, 16, 18, 6, 15],
}

# Convert data to a 2D array for plotting
data_values = list(data.values())

# Create a vertical box plot
plt.figure(figsize=(14, 10))

# Create the box plot
box = plt.boxplot(data_values, patch_artist=True, vert=True, labels=sectors, notch=True)

# Customizing box colors and style
colors = plt.cm.viridis(np.linspace(0, 1, len(sectors)))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Customize lines and medians
for median in box['medians']:
    median.set(color='darkblue', linewidth=2)
for whisker in box['whiskers']:
    whisker.set(color='gray', linewidth=1)
for cap in box['caps']:
    cap.set(color='black', linewidth=2)

# Calculate means for additional statistical visualization
means = [np.mean(d) for d in data_values]
plt.scatter(range(1, len(sectors) + 1), means, color='red', label='Mean', zorder=5)

# Setting the title and labels
plt.title('Impact of Social Media Marketing on Small Business Revenue\nAcross Various Sectors (2020-2023)', fontsize=16, pad=20)
plt.xlabel('Sectors', fontsize=14)
plt.ylabel('Percentage Revenue Increase (%)', fontsize=14)
plt.xticks(rotation=45, ha='right')

# Adding gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding a legend for clarity
plt.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()