import matplotlib.pyplot as plt
import numpy as np

# Define languages and sectors
languages = ['English', 'Spanish', 'Chinese', 'French', 'JavaScript', 'Python', 'C++']
sectors = ['Social Media', 'Programming', 'Business Communication', 'Technical Documentation']

# Data: Percentage representation of languages in each sector
# Rows correspond to languages and columns correspond to sectors
language_data = np.array([
    [90, 20, 70, 50],  # English
    [60, 5, 30, 10],   # Spanish
    [40, 10, 20, 15],  # Chinese
    [50, 5, 40, 30],   # French
    [10, 80, 5, 10],   # JavaScript
    [5, 70, 5, 60],    # Python
    [0, 40, 5, 30]     # C++
])

# Create the heatmap
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.imshow(language_data, cmap='YlGnBu', aspect='auto', interpolation='nearest')

# Add color bar for reference
colorbar = fig.colorbar(cax, ax=ax, orientation='vertical', shrink=0.8)
colorbar.set_label('Usage Percentage', fontsize=12)

# Set labels for axes
ax.set_xticks(np.arange(len(sectors)))
ax.set_yticks(np.arange(len(languages)))
ax.set_xticklabels(sectors, rotation=45, ha='right', fontsize=12)
ax.set_yticklabels(languages, fontsize=12)

# Add text annotations for clarity
for (i, j), val in np.ndenumerate(language_data):
    ax.text(j, i, f'{val}%', ha='center', va='center', color='black', fontsize=10)

# Title and axis labels
plt.title("Language Utilization Across\nDigital Communication Sectors", fontsize=16, weight='bold', pad=20)
plt.xlabel("Communication Sectors", fontsize=14)
plt.ylabel("Languages", fontsize=14)

# Ensure no overlapping and neat presentation
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the heatmap
plt.show()