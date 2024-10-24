import matplotlib.pyplot as plt
import numpy as np

# Data for painting durations in hours, representative of various art styles
realism_durations = [120, 135, 150, 165, 130, 145, 155, 160, 140, 155, 170, 150, 145, 155]
impressionism_durations = [80, 90, 85, 95, 70, 85, 75, 88, 92, 83, 86, 80, 89, 77]
abstract_expressionism_durations = [60, 65, 70, 75, 50, 80, 68, 72, 77, 70, 74, 60, 66, 73]
surrealism_durations = [100, 110, 115, 95, 105, 120, 110, 100, 108, 112, 105, 102, 118, 116]
cubism_durations = [95, 100, 90, 105, 85, 100, 95, 110, 92, 101, 98, 99, 97, 94]

durations_data = [
    realism_durations,
    impressionism_durations,
    abstract_expressionism_durations,
    surrealism_durations,
    cubism_durations
]

art_styles = ['Realism', 'Impressionism', 'Abstract Expressionism', 'Surrealism', 'Cubism']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Create the vertical box plot
colors = ['#d3d3d3', '#b0c4de', '#fa8072', '#dda0dd', '#ffdab9']
box = ax.boxplot(durations_data, patch_artist=True, labels=art_styles, notch=True)

# Customizing the box plot appearance
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker in box['whiskers']:
    whisker.set(color='grey', linewidth=1.5)

for cap in box['caps']:
    cap.set(color='grey', linewidth=1.5)

for median in box['medians']:
    median.set(color='black', linewidth=2)

# Overlay individual data points
for i, durations in enumerate(durations_data):
    y = np.random.normal(i + 1, 0.04, size=len(durations))
    ax.plot(y, durations, 'o', alpha=0.6, color='navy')

# Calculate and overlay the mean as a line plot
means = [np.mean(durations) for durations in durations_data]
ax.plot(range(1, len(art_styles) + 1), means, color='darkgreen', marker='D', markersize=8, linestyle='-', linewidth=2, label='Mean Duration')

# Add labels and title
ax.set_xlabel("Art Styles", fontsize=14)
ax.set_ylabel("Painting Duration (hours)", fontsize=14)
ax.set_title("Creativity Unveiled:\nVariance and Mean Trends in Painting Duration Among Famous Art Styles", fontsize=16, wrap=True)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, which='both', color='lightgrey')

# Add a legend
legend_elements = [
    plt.Line2D([0], [0], color='black', lw=2, label='Median'),
    plt.Line2D([0], [0], color='darkgreen', lw=2, marker='D', label='Mean Duration'),
    plt.Line2D([0], [0], marker='o', color='navy', label='Individual Data Points', markersize=8, linestyle='None')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize='small', title="Plot Elements")

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()