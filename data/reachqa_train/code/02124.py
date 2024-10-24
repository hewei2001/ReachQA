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

# Initialize subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stacked Bar Chart: Language proficiency by region
bar_width = 0.5
bar_positions = np.arange(len(regions))
bottoms = np.zeros(len(regions))

for i, language in enumerate(languages):
    ax1.bar(bar_positions, proficiency_data[:, i], color=colors[i], edgecolor='white',
            width=bar_width, label=language, bottom=bottoms)
    bottoms += proficiency_data[:, i]

# Percentage annotations for the bar chart
for i in range(len(regions)):
    cumulative_percentage = 0
    for j in range(len(languages)):
        midpoint = cumulative_percentage + proficiency_data[i, j] / 2
        ax1.text(i, midpoint, f"{proficiency_data[i, j]}%", ha='center', va='center', color='white', fontweight='bold')
        cumulative_percentage += proficiency_data[i, j]

# Set labels and title for the bar chart
ax1.set_title('Global Language Proficiency\nAmong Students by Region (2023)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Proficiency (%)', fontsize=12)
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(regions, rotation=45, ha='right')
ax1.set_ylim(0, 100)
ax1.legend(title='Languages', loc='upper right', fontsize=10, title_fontsize='11')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Pie Chart: Overall language proficiency distribution
total_proficiency = np.sum(proficiency_data, axis=0)
ax2.pie(total_proficiency, labels=languages, autopct='%1.1f%%', startangle=90, colors=colors, 
        wedgeprops={'edgecolor': 'black'})

# Set title for the pie chart
ax2.set_title('Overall Language Proficiency\nDistribution (2023)', fontsize=14, fontweight='bold')

# Adjust layout and display
plt.tight_layout()
plt.show()