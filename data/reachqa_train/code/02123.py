import matplotlib.pyplot as plt
import numpy as np

# Define regions and languages
regions = ['North America', 'Europe', 'Asia', 'South America']
languages = ['English', 'Spanish', 'Mandarin']

# Language proficiency data as percentage for each region
proficiency_data = np.array([
    [75, 20, 5],    # North America
    [65, 25, 10],   # Europe
    [40, 10, 50],   # Asia
    [55, 40, 5]     # South America
])

# Colors for each language
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create a percentage bar chart
bar_width = 0.5
bar_positions = np.arange(len(regions))

# Stack the bars for each language
bottoms = np.zeros(len(regions))
for i, language in enumerate(languages):
    ax.bar(bar_positions, proficiency_data[:, i], color=colors[i], edgecolor='white', width=bar_width, label=language, bottom=bottoms)
    bottoms += proficiency_data[:, i]

# Add percentage annotations
for i in range(len(regions)):
    cumulative_percentage = 0
    for j in range(len(languages)):
        midpoint = cumulative_percentage + proficiency_data[i, j] / 2
        ax.text(i, midpoint, f"{proficiency_data[i, j]}%", ha='center', va='center', color='white', fontweight='bold')
        cumulative_percentage += proficiency_data[i, j]

# Set chart title and labels
ax.set_title('Global Language Proficiency Among Students\nby Region (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Proficiency (%)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(regions)

# Fix the y-axis limit to a consistent 0-100%
ax.set_ylim(0, 100)

# Add legend
ax.legend(title='Languages', loc='upper right', fontsize=10, title_fontsize='11')

# Minimal grid configuration
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()