import matplotlib.pyplot as plt
import numpy as np

# Data: Classic novels and their social media mentions (in thousands)
novels = [
    "Pride and Prejudice",
    "1984",
    "To Kill a Mockingbird",
    "Moby-Dick",
    "War and Peace",
    "The Great Gatsby",
    "Crime and Punishment",
    "The Catcher in the Rye",
    "Brave New World",
    "Jane Eyre"
]
mentions = np.array([50, 75, 85, 40, 60, 90, 55, 70, 65, 80])

# Sort data to make the chart clearer
sorted_indices = np.argsort(mentions)
novels = np.array(novels)[sorted_indices]
mentions = mentions[sorted_indices]

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
bars = ax.barh(novels, mentions, color=plt.cm.viridis(np.linspace(0, 1, len(novels))), edgecolor='black')

# Add titles and labels
ax.set_title('Classic Literature Popularity in the 21st Century\nSocial Media Mentions', fontsize=16, fontweight='bold')
ax.set_xlabel('Social Media Mentions (in thousands)', fontsize=12)

# Adding annotations to highlight the mention count for each novel
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{int(width)}k', va='center', ha='left', fontsize=10, color='black')

# Highlight top three novels by changing their color
top_novels_indices = sorted_indices[-3:]
for idx in top_novels_indices:
    bars[idx].set_color('#FF4500')

# Adjust y-ticks for better alignment and readability
ax.tick_params(axis='y', which='major', labelsize=10)

# Add gridlines for easier value estimation
ax.xaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Use tight layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()