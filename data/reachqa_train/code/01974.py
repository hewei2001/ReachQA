import matplotlib.pyplot as plt
import numpy as np

# Data for publications from 2018 to 2022
years = np.array(['2018', '2019', '2020', '2021', '2022'])
languages = ['Latin', 'Ancient Greek', 'Sanskrit', 'Classical Chinese', 'Old Norse']

# Number of academic papers published for each language each year
publications = np.array([
    [120, 130, 150, 160, 180],  # Latin
    [110, 120, 125, 140, 150],  # Ancient Greek
    [80, 85, 90, 100, 110],     # Sanskrit
    [90, 100, 105, 110, 115],   # Classical Chinese
    [70, 75, 80, 85, 90]        # Old Norse
])

# Sum the total publications for each language
total_publications = np.sum(publications, axis=1)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 7))

# Create the bars
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']
bars = ax.barh(languages, total_publications, color=colors, edgecolor='black', height=0.6)

# Add title and labels
ax.set_title("Revival in Print: Academic Publications\non Ancient Languages (2018-2022)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Number of Publications", fontsize=12)
ax.set_yticks(np.arange(len(languages)))
ax.set_yticklabels(languages, fontsize=11)

# Add the data labels to the bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center', fontsize=10, fontweight='bold')

# Add vertical grid lines for easier reading
ax.xaxis.grid(True, linestyle='--', alpha=0.6)

# Set limits for the x-axis
ax.set_xlim(0, 700)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()