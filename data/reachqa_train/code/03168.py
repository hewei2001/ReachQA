import matplotlib.pyplot as plt
import numpy as np

# Constructing hypothetical sentence length data for each language (in words)
english_sentence_lengths = [5, 7, 8, 5, 6, 7, 12, 15, 7, 8, 6, 9, 5, 9, 10, 18, 22]
spanish_sentence_lengths = [6, 8, 9, 6, 7, 10, 14, 18, 7, 9, 11, 6, 7, 5, 8, 20, 25]
mandarin_sentence_lengths = [4, 5, 6, 5, 6, 4, 7, 8, 9, 10, 5, 6, 7, 8, 3, 4, 5, 6, 30]
french_sentence_lengths = [7, 9, 11, 9, 7, 8, 10, 13, 15, 9, 10, 8, 7, 10, 11, 6, 23]
german_sentence_lengths = [8, 10, 11, 8, 9, 12, 14, 17, 8, 10, 12, 9, 8, 9, 14, 28]

# Organizing data for plotting
data = [
    english_sentence_lengths,
    spanish_sentence_lengths,
    mandarin_sentence_lengths,
    french_sentence_lengths,
    german_sentence_lengths
]

# Labels for the languages
language_labels = ['English', 'Spanish', 'Mandarin', 'French', 'German']

# Creating the horizontal box plot
plt.figure(figsize=(12, 8))
plt.boxplot(data, vert=False, patch_artist=True, labels=language_labels,
            boxprops=dict(facecolor='lightblue', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', color='gold', markersize=8, alpha=0.6),
            notch=True)  # adding notches for median significance

# Enhancing layout for better readability
plt.title('Comparative Analysis of Sentence Lengths\nAcross Different Languages', fontsize=16, fontweight='bold')
plt.xlabel('Sentence Length (Number of Words)', fontsize=12)
plt.ylabel('Languages', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Ensure no overlapping by adjusting layout
plt.tight_layout()

# Display the plot
plt.show()