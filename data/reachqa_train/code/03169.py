import matplotlib.pyplot as plt
import numpy as np

# Original sentence length data
english_sentence_lengths = [5, 7, 8, 5, 6, 7, 12, 15, 7, 8, 6, 9, 5, 9, 10, 18, 22]
spanish_sentence_lengths = [6, 8, 9, 6, 7, 10, 14, 18, 7, 9, 11, 6, 7, 5, 8, 20, 25]
mandarin_sentence_lengths = [4, 5, 6, 5, 6, 4, 7, 8, 9, 10, 5, 6, 7, 8, 3, 4, 5, 6, 30]
french_sentence_lengths = [7, 9, 11, 9, 7, 8, 10, 13, 15, 9, 10, 8, 7, 10, 11, 6, 23]
german_sentence_lengths = [8, 10, 11, 8, 9, 12, 14, 17, 8, 10, 12, 9, 8, 9, 14, 28]

# Data for the box plot
data = [
    english_sentence_lengths,
    spanish_sentence_lengths,
    mandarin_sentence_lengths,
    french_sentence_lengths,
    german_sentence_lengths
]

# Labels for the languages
language_labels = ['English', 'Spanish', 'Mandarin', 'French', 'German']

# Creating hypothetical "sentence complexity" scores
english_complexity = [x * 0.9 + 1 for x in english_sentence_lengths]
spanish_complexity = [x * 1.1 - 0.5 for x in spanish_sentence_lengths]
mandarin_complexity = [x * 0.85 + 2 for x in mandarin_sentence_lengths]
french_complexity = [x * 1.05 for x in french_sentence_lengths]
german_complexity = [x * 0.95 + 1.5 for x in german_sentence_lengths]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Creating the horizontal box plot
ax.boxplot(data, vert=False, patch_artist=True, labels=language_labels,
           boxprops=dict(facecolor='lightblue', color='black'),
           whiskerprops=dict(color='black'),
           capprops=dict(color='black'),
           medianprops=dict(color='red', linewidth=2),
           flierprops=dict(marker='o', color='gold', markersize=8, alpha=0.6),
           notch=True)  # adding notches for median significance

# Plotting the scatter overlay
language_indices = np.arange(1, len(language_labels) + 1)
scatter_colors = ['blue', 'green', 'purple', 'orange', 'brown']

# Scatter plot for each language
ax.scatter(english_complexity, [1] * len(english_complexity), c=scatter_colors[0], alpha=0.5, label='English Complexity')
ax.scatter(spanish_complexity, [2] * len(spanish_complexity), c=scatter_colors[1], alpha=0.5, label='Spanish Complexity')
ax.scatter(mandarin_complexity, [3] * len(mandarin_complexity), c=scatter_colors[2], alpha=0.5, label='Mandarin Complexity')
ax.scatter(french_complexity, [4] * len(french_complexity), c=scatter_colors[3], alpha=0.5, label='French Complexity')
ax.scatter(german_complexity, [5] * len(german_complexity), c=scatter_colors[4], alpha=0.5, label='German Complexity')

# Enhance layout for readability
ax.set_title('Comparative Analysis of Sentence Lengths\nAcross Different Languages with Complexity Scores', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Sentence Length and Complexity', fontsize=12)
ax.set_ylabel('Languages', fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add a legend for the scatter plot
ax.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()