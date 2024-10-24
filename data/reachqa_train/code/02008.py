import matplotlib.pyplot as plt
import numpy as np

# List of most translated literary works
works = [
    "The Little Prince",
    "Pinocchio",
    "The Adventures of Huckleberry Finn",
    "Harry Potter Series",
    "Alice in Wonderland",
    "Don Quixote",
    "The Bible"
]

# Corresponding number of translations (artificial data)
translations = [300, 260, 275, 350, 150, 250, 335]

# Create the horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(works)))

bars = ax.barh(works, translations, color=colors, height=0.6, alpha=0.85)

# Title and labels
ax.set_title("The World's Most Translated Literary Works:\nA Global Journey Through Languages", 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Number of Languages', fontsize=12)
ax.set_ylabel('Literary Works', fontsize=12)

# Add value labels to the end of each bar
for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', 
            va='center', ha='left', fontsize=11)

# Customize tick parameters for better readability
ax.tick_params(axis='y', labelsize=10, pad=10)
ax.set_xlim(0, max(translations) + 50)

# Add vertical grid lines to improve readability
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()