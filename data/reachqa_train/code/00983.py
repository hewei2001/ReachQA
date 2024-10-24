import matplotlib.pyplot as plt
import numpy as np

# Word counts for each literary work in thousands
word_counts = np.array([150, 121, 30, 80, 75, 122, 183, 183, 47, 89])

# Literary eras
eras = ['Classical', 'Classical', 'Renaissance', 'Renaissance',
        'Romantic', 'Romantic', 'Victorian', 'Victorian',
        'Modern', 'Modern']

# Corresponding works
works = ['The Iliad', 'The Odyssey', 'Hamlet', 'Paradise Lost',
         'Frankenstein', 'Pride & Prejudice', 'Jane Eyre',
         'Great Expectations', 'The Great Gatsby', '1984']

# Set colors for each era
colors = ['#1f77b4', '#1f77b4', '#ff7f0e', '#ff7f0e', 
          '#2ca02c', '#2ca02c', '#d62728', '#d62728', 
          '#9467bd', '#9467bd']

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Plot line graph with colors
ax.plot(eras, word_counts, marker='o', linestyle='-', linewidth=2, color='grey', zorder=1)

# Annotating each data point
for i, (era, word_count, work) in enumerate(zip(eras, word_counts, works)):
    ax.annotate(f'{work}\n({word_count}k)',
                (era, word_count),
                textcoords="offset points",
                xytext=(0,10 if i % 2 == 0 else -15),
                ha='center',
                fontsize=9,
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

# Highlighting the specific era with colors
for i, (era, word_count, color) in enumerate(zip(eras, word_counts, colors)):
    ax.scatter(era, word_count, color=color, s=100, zorder=2)

# Title and labels
ax.set_title("Journey Through Literary Eras:\nProminent Literature Word Counts", fontsize=16, fontweight='bold', color='darkslateblue')
ax.set_xlabel('Literary Era', fontsize=12, fontweight='bold')
ax.set_ylabel('Word Count (in thousands)', fontsize=12, fontweight='bold')

# Customize x-axis
plt.xticks(np.arange(len(set(eras))), sorted(set(eras)), fontsize=10)
plt.yticks(fontsize=10)

# Adding grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

# Legend for highlighting colors
legend_labels = ['Classical', 'Renaissance', 'Romantic', 'Victorian', 'Modern']
handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                      markerfacecolor=color, markersize=8) for label, color in zip(legend_labels, colors[::2])]
plt.legend(handles=handles, title='Literary Eras', loc='upper left', fontsize=10, title_fontsize=12)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()