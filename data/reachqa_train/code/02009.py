import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Expanded list of most translated literary works
works = [
    "The Little Prince",
    "Pinocchio",
    "The Adventures of Huckleberry Finn",
    "Harry Potter Series",
    "Alice in Wonderland",
    "Don Quixote",
    "The Bible",
    "Moby Dick",
    "Les Misérables",
    "War and Peace",
    "The Alchemist",
    "Pride and Prejudice",
    "Winnie-the-Pooh",
    "The Odyssey",
    "The Great Gatsby"
]

# Corresponding number of translations
translations = [300, 260, 275, 350, 150, 250, 335, 200, 175, 190, 220, 160, 230, 185, 210]

# Years since publication as an additional data series
years_since_pub = [77, 139, 138, 24, 158, 418, 2700, 172, 161, 156, 35, 210, 97, 2754, 98]

# Create a figure with multiple subplots
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(14, 10))
fig.subplots_adjust(left=0.15, right=0.85, top=0.9, bottom=0.1)

# Create a bar chart
colors = plt.cm.viridis(np.linspace(0, 1, len(works)))
bars = ax.barh(works, translations, color=colors, height=0.6, alpha=0.85, label='Translations')

# Adding a line plot for years since publication to challenge data understanding
ax2 = ax.twiny()
ax2.plot(years_since_pub, works, color='grey', linestyle='--', marker='o', label='Years Since Publication')
ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

# Titles and labels
ax.set_title("Exploring the Translation and Longevity of Global Literary Works:\nInsights Across Time", 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Number of Translations', fontsize=12)
ax.set_ylabel('Literary Works', fontsize=12)
ax2.set_xlabel('Years Since Publication', fontsize=12)

# Add value labels to the end of each bar
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', 
            va='center', ha='left', fontsize=11)

# Customize tick parameters for better readability
ax.tick_params(axis='y', labelsize=10, pad=10)
ax.set_xlim(0, max(translations) + 50)
ax2.set_xlim(max(years_since_pub) + 20, 0)  # Flip axis for years since publication

# Add vertical grid lines to improve readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Legends
ax.legend(loc='upper right')
ax2.legend(loc='upper left')

# Ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()