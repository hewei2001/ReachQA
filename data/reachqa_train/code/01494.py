import matplotlib.pyplot as plt
import numpy as np

# Define periods and corresponding data for art style preference scores
periods = ['2000-2004', '2005-2009', '2010-2014', '2015-2019']
abstract = [68, 75, 80, 85]
realism = [60, 58, 55, 53]
surrealism = [55, 60, 63, 68]
impressionism = [78, 75, 70, 65]
pop_art = [50, 54, 60, 67]

# Organize the data into a format suitable for box plot
data = [abstract, realism, surrealism, impressionism, pop_art]
labels = ['Abstract', 'Realism', 'Surrealism', 'Impressionism', 'Pop Art']

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Create a vertical box plot
plt.boxplot(data, vert=True, patch_artist=True, labels=labels, notch=True, showmeans=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(marker='o', color='red', alpha=0.5),
            medianprops=dict(color='orange', linewidth=2),
            meanprops=dict(marker='D', markeredgecolor='black', markerfacecolor='yellow'))

# Customizing the plot
plt.title("Evolution of Art Styles: The 21st Century Canvas\nPreference Among Art Collectors", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Art Style", fontsize=12)
plt.ylabel("Preference Score", fontsize=12)

# Adding grid for better readability
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Add annotations for notable trends
plt.annotate('Rise in Pop Art popularity', xy=(5, 67), xytext=(4.5, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Ensure layout is tight and elements are not overlapping
plt.tight_layout()

# Display the plot
plt.show()