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

# Calculate average annual growth for each language
annual_growth = np.mean(np.diff(publications, axis=1) / publications[:, :-1] * 100, axis=1)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Horizontal bar chart for total publications
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']
bars = ax1.barh(languages, total_publications, color=colors, edgecolor='black', height=0.6)

# Add labels to the bars
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center', fontsize=10, fontweight='bold')

# Set titles and labels
ax1.set_title("Revival in Print: Academic Publications\nand Growth on Ancient Languages (2018-2022)",
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Total Publications", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 700)

# Create secondary axis for growth rates
ax2 = ax1.twiny()
ax2.plot(annual_growth, languages, color='navy', marker='o', linestyle='--', label='Avg Annual Growth (%)')
ax2.set_xlabel('Average Annual Growth (%)', fontsize=12)
ax2.set_xlim(0, 50)  # Set a reasonable limit for percentage growth

# Add a legend
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()